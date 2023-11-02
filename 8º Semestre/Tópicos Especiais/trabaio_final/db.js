const sqlite3 = require('sqlite3').verbose();

// Crie uma nova instância do banco de dados em memória (pode ser alterado para um arquivo se necessário)
const db = new sqlite3.Database('file:memory:');

// Criação da tabela Dispositivo e Localizacao
db.serialize(() => {
  db.run('CREATE TABLE Dispositivo (id TEXT PRIMARY KEY, nome TEXT, codigo TEXT, ativo BOOLEAN, marca TEXT)');
  db.run('CREATE TABLE Localizacao (id TEXT PRIMARY KEY, id_dispositivo TEXT, latitude REAL, longitude REAL, data DATE, distancia REAL)');

  // População inicial ou outras operações de configuração podem ser adicionadas aqui

  console.log('Banco de dados SQLite pronto');
});

module.exports = db;
