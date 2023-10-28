const express = require('express');
const bodyParser = require('body-parser');
const uuid = require('uuid');
const moment = require('moment');
const http = require('http');
const socketIo = require('socket.io');
const sqlite3 = require('sqlite3').verbose();
const amqp = require('amqplib');

// Crie uma nova instância do banco de dados em memória (pode ser alterado para um arquivo se necessário)
const db = new sqlite3.Database(':memory:');

// Criação da tabela Dispositivo e Localizacao
db.serialize(() => {
  db.run('CREATE TABLE Dispositivo (id TEXT PRIMARY KEY, nome TEXT, codigo TEXT, ativo BOOLEAN)');
  db.run('CREATE TABLE Localizacao (id TEXT PRIMARY KEY, id_dispositivo TEXT, latitude REAL, longitude REAL, data_hora DATETIME)');

  // População inicial ou outras operações de configuração podem ser adicionadas aqui

  console.log('Banco de dados SQLite pronto');
});

const app = express();
const port = 3001;
const server = http.createServer(app);
const io = socketIo(server);

app.use(bodyParser.json());

// Middleware para limpar a cache diariamente
app.use((req, res, next) => {
  if (!req.app.locals.cacheCleared) {
    const now = moment();
    const midnight = moment().endOf('day');
    const timeUntilMidnight = midnight.diff(now);

    setTimeout(() => {
      req.app.locals.cache = {};
      req.app.locals.cacheCleared = true;
    }, timeUntilMidnight);

    req.app.locals.cacheCleared = false;
  }

  next();
});

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
    const queue = 'localizacao_queue';

    const connection = await amqp.connect(queueUrl);
    const channel = await connection.createChannel();
    await channel.assertQueue(queue, { durable: true });

    console.log('Consumidor aguardando mensagens...');

    // Função para processar uma mensagem
    const processarMensagem = async (mensagem) => {
      try {
        // Adicione aqui a lógica para processar a mensagem
        console.log('Mensagem recebida:', mensagem.content.toString());
      } catch (error) {
        console.error('Erro ao processar mensagem:', error.message);
      }
    };

    // Função para consumir a fila
    const consumir = async () => {
      const mensagem = await channel.get(queue);

      if (mensagem) {
        await processarMensagem(mensagem);
      }
    };

    // Consumir a fila a cada 3 segundos
    setInterval(consumir, 3000);
  } catch (error) {
    console.error('Erro ao iniciar o consumidor:', error.message);
  }
}

// Iniciar o consumo da fila RabbitMQ
consumirFilaRabbitMQ();

// Rota para receber dados de localização
app.post('/receber-localizacao', async (req, res) => {
  try {
    const { id_dispositivo, latitude, longitude } = req.body;

    // Verificar se o dispositivo existe e está ativo
    const dispositivo = await getDispositivoById(id_dispositivo);

    if (!dispositivo || !dispositivo.ativo) {
      return res.status(404).json({ error: 'Dispositivo não encontrado ou inativo' });
    }

    // Salvar no banco de dados
    const novaLocalizacao = await saveLocalizacao(id_dispositivo, latitude, longitude);

    res.status(200).json({ message: 'Localização recebida com sucesso' });
  } catch (error) {
    console.error('Erro ao receber localização:', error.message);
    res.status(500).json({ error: 'Erro interno do servidor' });
  }
});


// Rota para receber dados de localização da fila
app.post('/receber-localizacao-fila', async (req, res) => {
  try {
    const { id_dispositivo, latitude, longitude } = req.body;

    // Enviar dados para a fila RabbitMQ
    await enviarParaFilaRabbitMQ({ id_dispositivo, latitude, longitude });

    res.status(200).json({ message: 'Localização enviada para a fila com sucesso' });
  } catch (error) {
    console.error('Erro ao receber localização pela fila:', error.message);
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

// Rota para registrar um novo dispositivo
app.post('/dispositivos', async (req, res) => {
  try {
    const { nome, codigo } = req.body;

    const novoDispositivo = await saveDispositivo(nome, codigo);

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

// Rota para obter todos os dispositivos
app.get('/dispositivos', async (req, res) => {
  try {
    const dispositivos = await getAllDispositivos();
    res.json(dispositivos);
  } catch (error) {
    console.error('Erro ao obter dispositivos:', error.message);
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

// Rota para receber dados de localização
app.post('/receber-localizacao', async (req, res) => {
  try {
    const { id_dispositivo, latitude, longitude } = req.body;

    // Salvar no banco de dados
    const novaLocalizacao = await saveLocalizacao(id_dispositivo, latitude, longitude);

    // Emitir a última localização para os clientes inscritos
    emitirUltimaLocalizacao(id_dispositivo);

    res.status(200).json({ message: 'Localização recebida com sucesso' });
  } catch (error) {
    console.error('Erro ao receber localização:', error.message);
    res.status(500).json({ error: 'Erro interno do servidor' });
  }
});

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
async function saveLocalizacao(id_dispositivo, latitude, longitude) {
  return new Promise((resolve, reject) => {
    const id_localizacao = uuid.v4();
    const data_hora = moment().format('YYYY-MM-DD HH:mm:ss');

    db.run(
      'INSERT INTO Localizacao (id, id_dispositivo, latitude, longitude, data_hora) VALUES (?, ?, ?, ?, ?)',
      [id_localizacao, id_dispositivo, latitude, longitude, data_hora],
      (err) => {
        if (err) {
          reject(err);
        } else {
          resolve({ id: id_localizacao, id_dispositivo, latitude, longitude, data_hora });
        }
      }
    );
  });
}

// Obter última localização de um dispositivo
async function getUltimaLocalizacao(id_dispositivo) {
  return new Promise((resolve, reject) => {
    db.get(
      'SELECT * FROM Localizacao WHERE id_dispositivo = ? ORDER BY data_hora DESC LIMIT 1',
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
async function saveDispositivo(nome, codigo) {
  return new Promise((resolve, reject) => {
    const id_dispositivo = uuid.v4();

    db.run(
      'INSERT INTO Dispositivo (id, nome, codigo, ativo) VALUES (?, ?, ?, true)',
      [id_dispositivo, nome, codigo],
      (err) => {
        if (err) {
          reject(err);
        } else {
          resolve({ id: id_dispositivo, nome, codigo, ativo: true });
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
async function getAllDispositivos() {
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
