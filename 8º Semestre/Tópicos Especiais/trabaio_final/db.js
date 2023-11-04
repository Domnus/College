const sqlite3 = require('sqlite3').verbose();
const fs = require('fs');

const dbFilePath = './banco.db';

// Verifica se o arquivo do banco de dados já existe
const dbExists = fs.existsSync(dbFilePath);

// Crie uma nova instância do banco de dados usando o arquivo existente ou um novo
const db = new sqlite3.Database(dbFilePath);

// Criação da tabela Dispositivo e Localizacao apenas se o banco de dados for recém-criado
if (!dbExists) {
  db.serialize(() => {
    db.run('CREATE TABLE Dispositivo (id TEXT PRIMARY KEY, nome TEXT, codigo TEXT, ativo BOOLEAN, marca TEXT)');
    db.run('CREATE TABLE Localizacao (id TEXT PRIMARY KEY, id_dispositivo TEXT, latitude REAL, longitude REAL, data DATE, distancia REAL)');

    // População inicial ou outras operações de configuração podem ser adicionadas aqui

    console.log('Banco de dados SQLite pronto');
  });
}

module.exports = db;