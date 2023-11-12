// publish.js
const mqtt = require('mqtt');
const { v4: uuidv4 } = require('uuid');

const mqttBroker = 'mqtt://localhost';
const mqttTopic = 'topico/dados';

// Função para gerar coordenadas de latitude e longitude realistas
function getRandomCoordinate() {
    const min = -90; // valor mínimo para latitude
    const max = 90;  // valor máximo para latitude
    const latitude = (Math.random() * (max - min) + min).toFixed(6);
  
    const minLon = -180; // valor mínimo para longitude
    const maxLon = 180;  // valor máximo para longitude
    const longitude = (Math.random() * (maxLon - minLon) + minLon).toFixed(6);
  
    return { latitude, longitude };
}

dispositivos = [
    "160c6b24-9682-41df-9b8d-4d79f53df0c7",
    "601a0205-479b-43f1-822e-1692e3f7f873"
]

// Cria um cliente MQTT
const client = mqtt.connect(mqttBroker);

// Evento chamado quando o cliente MQTT se conecta ao broker
client.on('connect', () => {
    console.log('Conectado ao broker MQTT - Publish');

    // Publica informações a cada segundo
    setInterval(() => {
        // Gera um ID UUID
        const id = uuidv4();

        // Gera latitude e longitude aleatórias
        const coordenadas = getRandomCoordinate();

        // Escolhe um dispositivo aleatório
        const idDispositivo = dispositivos[Math.floor(Math.random() * dispositivos.length)];

        // Monta o payload JSON
        const payload = JSON.stringify({ idDispositivo, id, coordenadas });

        // Publica as informações no tópico MQTT
        client.publish(mqttTopic, payload, { qos: 1 });

        console.log(`Informações publicadas: ${payload}`);
    }, 3000);
});

// Lidar com erros de conexão MQTT
client.on('error', (error) => {
    console.error('Erro de conexão MQTT:', error);
});

// Exporta a função de início
module.exports = { start: () => {} }; // a função start pode ser vazia ou incluir lógica específica, se necessário
