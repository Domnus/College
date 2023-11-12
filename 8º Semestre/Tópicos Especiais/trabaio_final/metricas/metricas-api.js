const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');
const { ApolloServer, gql } = require('apollo-server');
const moment = require('moment');
const geolib = require('geolib');

const db = require('../db');

const ADDRESS = 'localhost'
const PORT = 50051

// Carregar o arquivo de definição gRPC
const protoPath = '/home/bentocarlos/Documents/College/8º Semestre/Tópicos Especiais/trabaio_final/metricas/metrics.proto';
const packageDefinition = protoLoader.loadSync(protoPath);

const rastreioProto = grpc.loadPackageDefinition(packageDefinition).rastreio;

const metricsService = {
  RegistrarLocalizacao: (call, callback) => {
    const { id, idDispositivo, latitude, longitude } = call.request;

    // Obter a última localização do dispositivo no banco de dados
    const queryUltimaLocalizacao = 'SELECT latitude, longitude FROM Localizacao WHERE id_dispositivo = ? ORDER BY data DESC LIMIT 1';
    const paramsUltimaLocalizacao = [idDispositivo];

    db.get(queryUltimaLocalizacao, paramsUltimaLocalizacao, (err, ultimaLocalizacao) => {
      if (err) {
        console.error('Erro ao obter última localização do banco de dados:', err);
        return callback(err, null);
      }

      if (ultimaLocalizacao) {
        // Calcular a distância usando a fórmula de Haversine
        var distancia = geolib.getDistance(
          { latitude: ultimaLocalizacao.latitude, longitude: ultimaLocalizacao.longitude },
          { latitude, longitude }
        );

        distancia = distancia / 1000; // converter para km

        // Inserir a nova localização no banco de dados
        const sql = 'INSERT INTO Localizacao (id, id_dispositivo, latitude, longitude, data, distancia) VALUES (?, ?, ?, ?, DATETIME("now", "localtime"), ?)';
        const params = [id, idDispositivo, latitude, longitude, distancia];

        db.run(sql, params, (err) => {
          if (err) {
            console.error('Erro ao registrar localização no banco de dados:', err);
            return callback(err, null);
          }

          console.log('Localização registrada com sucesso no banco de dados');
          callback(null, {});
        });
      } else {
        // Esta é a primeira localização do dispositivo, apenas insira no banco de dados
        const sql = 'INSERT INTO Localizacao (id, id_dispositivo, latitude, longitude, data, distancia) VALUES (?, ?, ?, ?, DATETIME("now", "localtime"), 0)';
        const params = [id, idDispositivo, latitude, longitude];

        db.run(sql, params, (err) => {
          if (err) {
            console.error('Erro ao registrar localização no banco de dados:', err);
            return callback(err, null);
          }

          console.log('Localização registrada com sucesso no banco de dados');
          callback(null, {});
        });
      }
    });
  },
};

const server = new grpc.Server();
server.addService(rastreioProto.MetricsService.service, metricsService);
server.bindAsync(`${ADDRESS}:${PORT}`, grpc.ServerCredentials.createInsecure(),
  (err, port) => {
    server.start();
    if (err) {
      console.log(err)
    }
    console.log(`Servidor gRPC da API de Métricas iniciado em ${ADDRESS}:${PORT}`);
  });

// Implementar o servidor Apollo GraphQL
const typeDefs = gql`
  type Dispositivo {
    id: String
    id_dispositivo: String
    quantidade_posicao: Int
    total_km: Float
  }

  type Marca {
    quantidade_dispositivo: Int
    marca: String
    quantidade_posicao: Int
    total_km: Float
  }

  type Geral {
    quantidade_dispositivo: Int
    quantidade_posicao: Int
    total_km: Float
  }

  type Query {
    consultaDispositivo(id_dispositivo: String, dia: String): Dispositivo
    consultaMarca(marca: String, dia: String): Marca
    consultaGeral(dia: String): Geral
  }
`;

const resolvers = {
  Query: {
    consultaDispositivo: async (_, { id_dispositivo, dia }) => {
      const query = `
        SELECT
          d.id AS id_dispositivo,
          d.marca,
          COUNT(*) AS quantidade_posicao,
          SUM(l.distancia) AS total_km
        FROM Localizacao l
        LEFT JOIN Dispositivo d ON l.id_dispositivo = d.id
        WHERE d.id = ? AND strftime('%Y-%m-%d', l.data) = ?
        GROUP BY d.id;
      `;

      const params = [id_dispositivo, dia];

      const resultado = await runQuery(query, params);

      if (resultado === undefined) {
        return {
          id_dispositivo,
          quantidade_posicao: 0,
          total_km: 0,
        };
      }

      return {
        id_dispositivo: resultado.id_dispositivo,
        quantidade_posicao: resultado.quantidade_posicao || 0,
        total_km: resultado.total_km || 0,
      };
    },

    consultaMarca: async (_, { marca, dia }) => {
      const query = `
      SELECT
        d.marca,
        COUNT(DISTINCT d.id) AS quantidade_dispositivo,
        COUNT(*) AS quantidade_posicao,
        SUM(l.distancia) AS total_km
      FROM Localizacao l
      LEFT JOIN Dispositivo d ON l.id_dispositivo = d.id
      WHERE d.marca = ? AND strftime('%Y-%m-%d', l.data) = ?
      GROUP BY 1;
      `;

      const params = [marca, dia];

      const resultado = await runQuery(query, params);

      if (resultado === undefined) {
        return {
          quantidade_dispositivo: 0,
          marca,
          quantidade_posicao: 0,
          total_km: 0,
        };
      }

      return {
        quantidade_dispositivo: resultado.quantidade_dispositivo || 0,
        marca: resultado.marca,
        quantidade_posicao: resultado.quantidade_posicao || 0,
        total_km: resultado.total_km || 0,
      };
    },

    consultaGeral: async (_, { dia }) => {
      const query = `
        SELECT
          COUNT(DISTINCT d.id) AS quantidade_dispositivo,
          COUNT(*) AS quantidade_posicao,
          SUM(l.distancia) AS total_km
        FROM Localizacao l
        LEFT JOIN Dispositivo d ON l.id_dispositivo = d.id
        WHERE strftime('%Y-%m-%d', l.data) = ?
      `;

      const params = [dia];

      const resultado = await runQuery(query, params);

      if (resultado === undefined) {
        return {
          quantidade_dispositivo: 0,
          quantidade_posicao: 0,
          total_km: 0,
        };
      }

      return {
        quantidade_dispositivo: resultado.quantidade_dispositivo || 0,
        quantidade_posicao: resultado.quantidade_posicao || 0,
        total_km: resultado.total_km || 0,
      };
    },
  },
};

async function runQuery(query, params) {
  return new Promise((resolve, reject) => {
    db.get(query, params, (err, row) => {
      if (err) {
        console.error('Erro ao executar consulta no banco de dados:', err);
        reject(err);
      } else {
        console.log('Resultado da consulta:', row);
        resolve(row);
      }
    });
  });
}

const serverGraphQL = new ApolloServer({ typeDefs, resolvers });
serverGraphQL.listen().then
