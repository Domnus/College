// index.js

// Require dos módulos necessários
const server = require('./rastreio-api');
const publish = require('./publish');
const assign = require('./assign');

// Porta para o servidor Express
const port = 3001;

// Iniciar o servidor Express
// server.listen(port, () => {
//   console.log(`Servidor de Rastreamento iniciado em http://localhost:${port}`);
// });

// Iniciar a publicação MQTT
publish.start();

// Atribuir a recepção de dados MQTT
assign.start();
