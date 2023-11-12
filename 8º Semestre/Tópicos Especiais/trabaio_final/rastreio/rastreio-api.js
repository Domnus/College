const express = require('express');
const bodyParser = require('body-parser');
const uuid = require('uuid');
const moment = require('moment');
const http = require('http');
const socketIo = require('socket.io');
const amqp = require('amqplib');
const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');
const { v4: uuidv4 } = require('uuid');
const db = require('../db');  // Importa o arquivo db.js
const cors = require('cors');
const geolib = require('geolib');

const protoPath = '/home/bentocarlos/Documents/College/8º Semestre/Tópicos Especiais/trabaio_final/rastreio/rastreio.proto';

const metricsProto = grpc.loadPackageDefinition(
  protoLoader.loadSync(protoPath)
);

const metricsClient = new metricsProto.MetricsService('localhost:50051', grpc.credentials.createInsecure());

const app = express();
const port = 3001;
const server = http.createServer(app);
const io = socketIo(server);

app.use(bodyParser.json());
app.use(cors())

// Middleware para limpar a cache diariamente
app.use((req, res, next) => {
  // Inicialize a cache se não estiver definida
  req.app.locals.cache = req.app.locals.cache || {};

  if (!req.app.locals.cacheCleared) {
    const now = moment();
    const midnight = moment().endOf('day');
    const timeUntilMidnight = midnight.diff(now);

    setTimeout(() => {
      req.app.locals.cache.allDispositivos = null; // Limpe a cache
      req.app.locals.cacheCleared = true;
    }, timeUntilMidnight);

    req.app.locals.cacheCleared = false;
  }

  next();
});

// Rota para obter todos os dispositivos
app.get('/dispositivos', async (req, res) => {
  try {
    const dispositivos = await getAllDispositivos(req, res);

    // Responda com os dispositivos da cache
    res.json(dispositivos);
  } catch (error) {
    console.error('Erro ao obter todos os dispositivos:', error.message);
    res.status(500).json({ error: 'Erro interno do servidor' });
  }
});

// Rota para obter um dispositivo específico
app.get('/dispositivos/:id_dispositivo', async (req, res) => {
  try {
    const { id_dispositivo } = req.params;

    // Verifique se a cache está definida e se o dispositivo específico está presente na cache
    if (req.app.locals.cache.allDispositivos && req.app.locals.cache.allDispositivos[id_dispositivo]) {
      // Se estiver presente na cache, responda com o dispositivo da cache
      res.json(req.app.locals.cache.allDispositivos[id_dispositivo]);
    } else {
      // Se não estiver na cache, busque no banco de dados e armazene na cache
      const dispositivo = await getDispositivo(id_dispositivo);

      if (dispositivo.length === 0) {
        return res.status(404).json({ error: 'Dispositivo não encontrado' });
      }

      // Armazene o dispositivo na cache
      req.app.locals.cache.allDispositivos = {
        ...req.app.locals.cache.allDispositivos,
        [id_dispositivo]: dispositivo,
      };

      // Responda com o dispositivo buscado no banco de dados
      res.json(dispositivo);
    }
  } catch (error) {
    console.error('Erro ao obter um dispositivo específico:', error.message);
    res.status(500).json({ error: 'Erro interno do servidor' });
  }
});

// Rota para registrar um novo dispositivo
app.post('/dispositivos', async (req, res) => {
  try {
    const { nome, codigo, marca } = req.body;

    const novoDispositivo = await saveDispositivo(nome, codigo, marca);

    res.status(201).json(novoDispositivo);
  } catch (error) {
    console.error('Erro ao registrar dispositivo:', error.message);
    res.status(500).json({ error: 'Erro interno do servidor' });
  }
});

// Rota para alterar o estado de ativo de um dispositivo
app.patch('/dispositivos/:id_dispositivo', async (req, res) => {
  try {
    const { id_dispositivo } = req.params;
    const { ativo } = req.body;

    const resultado = await updateAtivoDispositivo(id_dispositivo, ativo);

    if (!resultado) {
      return res.status(404).json({ error: 'Dispositivo não encontrado' });
    }

    res.json(resultado);
  } catch (error) {
    console.error('Erro ao alterar estado de ativo do dispositivo:', error.message);
    res.status(500).json({ error: 'Erro interno do servidor' });
  }
});

// Rota para remover um dispositivo
app.delete('/dispositivos/:id_dispositivo', async (req, res) => {
  try {
    const { id_dispositivo } = req.params;

    const resultado = await deleteDispositivo(id_dispositivo);

    if (!resultado) {
      return res.status(404).json({ error: 'Dispositivo não encontrado' });
    }

    res.json({ message: 'Dispositivo removido com sucesso' });
  } catch (error) {
    console.error('Erro ao remover dispositivo:', error.message);
    res.status(500).json({ error: 'Erro interno do servidor' });
  }
});

// Função para enviar localização para a API de Métricas
function enviarLocalizacaoParaMetrics(id_dispositivo, latitude, longitude, marca) {
  const localizacao = {
    id_dispositivo: id_dispositivo,
    latitude: latitude,
    longitude: longitude,
    marca: marca,
  };

  metricsClient.RegistrarLocalizacao(localizacao, (error, response) => {
    if (!error) {
      console.log('Localização registrada com sucesso na API de Métricas');
    } else {
      console.error('Erro ao registrar localização:', error.message);
    }
  });
}

// Rota para obter histórico de localização com Hateoas
app.get('/historico/:id_dispositivo', async (req, res) => {
  try {
    const { id_dispositivo } = req.params;

    const historico = await getHistoricoLocalizacao(id_dispositivo);

    const historicoComHateoas = historico.map((localizacao) => {
      return {
        ...localizacao,
        links: [
          {
            rel: 'self',
            href: `${req.protocol}://${req.get('host')}/historico/${localizacao.id}`,
          },
        ],
      };
    });

    res.json(historicoComHateoas);
  } catch (error) {
    console.error('Erro ao obter histórico de localização:', error.message);
    res.status(500).json({ error: 'Erro interno do servidor' });
  }
});

async function consumirFilaRabbitMQ() {
  try {
    const queueUrl = 'amqp://localhost';
    const queue = 'localizacao';

    const connection = await amqp.connect(queueUrl);
    const channel = await connection.createChannel();
    await channel.assertQueue(queue, { durable: true });

    // Função para processar uma mensagem
    const processarMensagem = async (mensagem) => {
      try {
        const dados = JSON.parse(mensagem.content.toString());
        const { latitude, longitude } = dados.coordenadas;
        const id_localizacao = dados.id;
        const id_dispositivo = dados.idDispositivo;

        return { id_dispositivo, id_localizacao, latitude, longitude }
      } catch (error) {
        console.error('Erro ao processar mensagem:', error.message);
        return null;
      }
    };

    // Função para consumir a fila
    const consumir = async () => {
      const mensagem = await channel.get(queue);

      if (mensagem) {
        const localizacao = await processarMensagem(mensagem);
        // Acknowledge (informar que a mensagem foi processada com sucesso)
        channel.ack(mensagem);

        // Retorna as informações da localização salva
        return localizacao;
      }

      return null; // Retorna null se não houver mensagem na fila
    };

    // Consumir a fila continuamente
    return consumir();
  } catch (error) {
    console.error('Erro ao iniciar o consumidor:', error.message);
  }
}

// Rota para receber dados de localização
app.post('/salvar-localizacao', async (req, res) => {
  try {
    const localizacao = await consumirFilaRabbitMQ();

    var { id_dispositivo, id_localizacao, latitude, longitude } = localizacao;

    // Verificar se o dispositivo existe e está ativo
    const dispositivo = await getDispositivoById(id_dispositivo);

    if (dispositivo.length <= 0) {
      return res.status(404).json({ error: 'Dispositivo não encontrado ou inativo' });
    }

    // const ultimaLocalizacao = await getUltimaLocalizacao(id_dispositivo);

    // var distancia = 0;

    // if (ultimaLocalizacao) {
    //   // Calcula a distância usando a fórmula de Haversine
    //   var distancia = geolib.getDistance(
    //     { latitude: ultimaLocalizacao.latitude, longitude: ultimaLocalizacao.longitude },
    //     { latitude, longitude } 
    //   ) / 1000;
    // }

    // // Salvar no banco de dados
    // const localizacaoSalva = await saveLocalizacao(id_localizacao, id_dispositivo, latitude, longitude, distancia);

    // Enviar para a API de Métricas usando gRPC
    const grpcLocalizacao = {
      id: id_localizacao,
      idDispositivo: id_dispositivo,
      latitude: latitude,
      longitude: longitude,
    };

    metricsClient.RegistrarLocalizacao(grpcLocalizacao, (error, response) => {
      if (!error) {
        console.log('Localização registrada com sucesso na API de Métricas');
      } else {
        console.error('Erro ao registrar localização:', error.message);
      }
    });

    res.status(200).json({ message: 'Localização recebida com sucesso' });
  } catch (error) {
    console.error('Erro ao receber localização:', error.message);
    res.status(500).json({ error: 'Erro interno do servidor' });
  }
});

// Nova rota para obter a última localização de um dispositivo
app.get('/ultima-localizacao/:id_dispositivo', async (req, res) => {
  try {
    const { id_dispositivo } = req.params;

    const ultimaLocalizacao = await getUltimaLocalizacao(id_dispositivo);

    if (!ultimaLocalizacao) {
      return res.status(404).json({ error: 'Nenhuma localização encontrada para o dispositivo' });
    }

    res.json(ultimaLocalizacao);
  } catch (error) {
    console.error('Erro ao obter última localização:', error.message);
    res.status(500).json({ error: 'Erro interno do servidor' });
  }
});

// WebSocket para fornecer a última localização em tempo real
io.on('connection', (socket) => {
  console.log('Cliente conectado');

  // Evento para se inscrever na última localização de um dispositivo
  socket.on('subscribe', (id_dispositivo) => {
    console.log(`Cliente se inscreveu para dispositivo: ${id_dispositivo}`);

    // Adiciona o cliente a uma sala com o ID do dispositivo
    socket.join(id_dispositivo);
  });

  // Evento para cancelar a inscrição na última localização de um dispositivo
  socket.on('unsubscribe', (id_dispositivo) => {
    console.log(`Cliente cancelou inscrição para dispositivo: ${id_dispositivo}`);

    // Remove o cliente da sala com o ID do dispositivo
    socket.leave(id_dispositivo);
  });
});

// Função para emitir a última localização para os clientes inscritos
const emitirUltimaLocalizacao = async (id_dispositivo) => {
  try {
    const ultimaLocalizacao = await getUltimaLocalizacao(id_dispositivo);

    if (ultimaLocalizacao) {
      io.to(id_dispositivo).emit('ultimaLocalizacao', ultimaLocalizacao);
    }
  } catch (error) {
    console.error('Erro ao obter e emitir última localização:', error.message);
  }
};

// Função para atualizar a última localização quando uma nova localização é recebida
const atualizarUltimaLocalizacao = (id_dispositivo, localizacao) => {
  io.to(id_dispositivo).emit('ultimaLocalizacao', localizacao);
};

// Iniciar o servidor
server.listen(port, () => {
  console.log(`Servidor de Rastreamento iniciado em http://localhost:${port}`);
});

// Funções auxiliares

// Obter histórico de localização
async function getHistoricoLocalizacao(id_dispositivo) {
  return new Promise((resolve, reject) => {
    db.all('SELECT * FROM Localizacao WHERE id_dispositivo = ?', [id_dispositivo], (err, rows) => {
      if (err) {
        reject(err);
      } else {
        resolve(rows);
      }
    });
  });
}

// Salvar nova localização no banco de dados
async function saveLocalizacao(id_localizacao, id_dispositivo, latitude, longitude, distancia) {
  return new Promise((resolve, reject) => {
    const data = moment().format('YYYY-MM-DD HH:mm:ss');

    db.run(
      'INSERT INTO Localizacao (id, id_dispositivo, latitude, longitude, data, distancia) VALUES (?, ?, ?, ?, ?, ?)',
      [id_localizacao, id_dispositivo, latitude, longitude, data, distancia],
      (err) => {
        if (err) {
          reject(err);
        } else {
          resolve({ id: id_localizacao, id_dispositivo, latitude, longitude, data, distancia });
        }
      }
    );
  });
}

// Obter última localização de um dispositivo
async function getUltimaLocalizacao(id_dispositivo) {
  return new Promise((resolve, reject) => {
    db.get(
      'SELECT * FROM Localizacao WHERE id_dispositivo = ? ORDER BY data DESC LIMIT 1',
      [id_dispositivo],
      (err, row) => {
        if (err) {
          reject(err);
        } else {
          resolve(row);
        }
      }
    );
  });
}

// Salvar novo dispositivo no banco de dados
async function saveDispositivo(nome, codigo, marca) {
  return new Promise((resolve, reject) => {
    const id_dispositivo = uuid.v4();

    db.run(
      'INSERT INTO Dispositivo (id, nome, codigo, ativo, marca) VALUES (?, ?, ?, true, ?)',
      [id_dispositivo, nome, codigo, marca],
      (err) => {
        if (err) {
          reject(err);
        } else {
          resolve({ id: id_dispositivo, nome, codigo, ativo: true, marca });
        }
      }
    );
  });
}

// Atualizar estado de ativo de um dispositivo
async function updateAtivoDispositivo(id_dispositivo, ativo) {
  return new Promise((resolve, reject) => {
    db.run(
      'UPDATE Dispositivo SET ativo = ? WHERE id = ? RETURNING *',
      [ativo, id_dispositivo],
      (err) => {
        if (err) {
          reject(err);
        } else {
          db.get('SELECT * FROM Dispositivo WHERE id = ?', [id_dispositivo], (err, row) => {
            if (err) {
              reject(err);
            } else {
              resolve(row);
            }
          });
        }
      }
    );
  });
}

// Remover dispositivo do banco de dados
async function deleteDispositivo(id_dispositivo) {
  return new Promise((resolve, reject) => {
    db.run('DELETE FROM Dispositivo WHERE id = ? RETURNING *', [id_dispositivo], (err) => {
      if (err) {
        reject(err);
      } else {
        resolve({ message: 'Dispositivo removido com sucesso' });
      }
    });
  });
}

// Obter todos os dispositivos
async function getAllDispositivos(req, res) {
  try {
    // Verificar se está no cache
    if (req.app.locals.cache && req.app.locals.cache.allDispositivos) {
      console.log('Obtendo todos os dispositivos do cache.');
      return req.app.locals.cache.allDispositivos;
    }

    // Se não estiver no cache, buscar no banco de dados
    const dispositivos = await fetchAllDispositivosFromDB();

    // Armazenar no cache
    req.app.locals.cache.allDispositivos = dispositivos;

    return dispositivos;
  } catch (error) {
    console.error('Erro ao obter todos os dispositivos:', error.message);
    res.status(500).json({ error: 'Erro interno do servidor' });
  }
}

// Função para buscar todos os dispositivos no banco de dados
async function fetchAllDispositivosFromDB() {
  return new Promise((resolve, reject) => {
    db.all('SELECT * FROM Dispositivo', (err, rows) => {
      if (err) {
        reject(err);
      } else {
        resolve(rows);
      }
    });
  });
}

async function getDispositivo(codigo) {
  return new Promise((resolve, reject) => {
    db.all('SELECT * FROM Dispositivo WHERE codigo = ?', [codigo], (err, rows) => {
      if (err) {
        reject(err);
      } else {
        resolve(rows);
      }
    });
  });
}

async function getDispositivoById(id) {
  return new Promise((resolve, reject) => {
    db.all('SELECT * FROM Dispositivo WHERE id = ? AND ativo = True', [id], (err, rows) => {
      if (err) {
        reject(err);
      } else {
        resolve(rows);
      }
    });
  });
}