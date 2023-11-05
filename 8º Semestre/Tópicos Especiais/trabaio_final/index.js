// index.js

const express = require('express');
const path = require('path');
const cors = require('cors');

const app = express();
const port = 3002;

// Require dos módulos necessários
const rastreio = require('./rastreio/rastreio-api');
const metricas = require('./metricas/metricas-api');
const publish = require('./publish');
const assign = require('./assign');

app.use(cors());

// Servir os arquivos estáticos na pasta public
app.use(express.static(path.join(__dirname, 'public')));

// Rota para servir o arquivo index.html
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Iniciar o servidor
app.listen(port, () => {
  console.log(`Servidor iniciado em http://localhost:${port}`);
});

app.get('/app.js', (req, res) => {
  res.setHeader('Content-Type', 'application/javascript');
  // Restante do código para enviar o conteúdo do arquivo app.js
});

// Iniciar a publicação MQTT
publish.start();

// Atribuir a recepção de dados MQTT
assign.start();
