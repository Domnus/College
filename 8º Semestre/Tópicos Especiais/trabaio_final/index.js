// index.js

// Require dos módulos necessários
const rastreio = require('./rastreio/rastreio-api');
const metriscas = require('./metricas/metricas-api');
const publish = require('./publish');
const assign = require('./assign');

// Iniciar a publicação MQTT
publish.start();

// Atribuir a recepção de dados MQTT
assign.start();
