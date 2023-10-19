const express = require('express');
const bodyParser = require('body-parser');
const mqtt = require('mqtt');
const amqp = require('amqplib');

const app = express();
const port = 3000;

// Configurações MQTT
const mqttBroker = 'mqtt://localhost';
const mqttTopic = 'topico/dados';

// Configurações RabbitMQ
const rabbitMQUrl = 'amqp://localhost';
const queueName = 'localizacao';

// Cria um cliente MQTT
const client = mqtt.connect(mqttBroker);

// Middleware para analisar o corpo da solicitação como JSON
app.use(bodyParser.json());

// Conectar ao RabbitMQ e criar a fila
async function setupRabbitMQ() {
  try {
    const connection = await amqp.connect(rabbitMQUrl);
    const channel = await connection.createChannel();
    await channel.assertQueue(queueName, { durable: true });
    console.log(`Fila RabbitMQ '${queueName}' criada e pronta para receber mensagens.`);
  } catch (error) {
    console.error('Erro ao configurar RabbitMQ:', error.message);
  }
}

// Rota para receber dados de localização via MQTT e encaminhar para a fila
app.post('/receber-dados', async (req, res) => {
  const { id, coordenadas } = req.body;

  console.log(coordenadas)

  // Conectar ao RabbitMQ e criar a fila (se ainda não foi configurada)
  await setupRabbitMQ();

  try {
    // Conectar ao RabbitMQ
    const connection = await amqp.connect(rabbitMQUrl);
    const channel = await connection.createChannel();

    // Enviar dados para a fila
    await channel.sendToQueue(queueName, Buffer.from(JSON.stringify({ id, coordenadas })), { persistent: true });

    res.status(200).json({ message: 'Dados recebidos com sucesso' });
  } catch (error) {
    console.error('Erro ao enviar dados para a fila RabbitMQ:', error.message);
    res.status(500).json({ error: 'Erro interno do servidor' });
  }
});

// Conectar ao broker MQTT
client.on('connect', () => {
  console.log('Conectado ao broker MQTT');

  // Subscrever ao tópico MQTT para receber dados de localização
  client.subscribe(mqttTopic);

  // Lidar com mensagens recebidas
  client.on('message', (topic, message) => {
    try {
      const data = JSON.parse(message.toString());
      // Enviar dados para a fila quando uma mensagem é recebida
      app.emit('receber-dados', data);
    } catch (error) {
      console.error('Erro ao processar mensagem MQTT:', error.message);
    }
  });
});

// Iniciar o servidor Express
app.listen(port, () => {
  console.log(`Servidor API iniciado em http://localhost:${port}`);
});
