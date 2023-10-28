// assign.js
const express = require('express');
const bodyParser = require('body-parser');
const mqtt = require('mqtt');
const amqp = require('amqplib');

const app = express();
const port = 3000;

const mqttBroker = 'mqtt://localhost';
const mqttTopic = 'topico/dados';

const rabbitMQUrl = 'amqp://localhost';
const queueName = 'localizacao';

let rabbitMQConfigured = false;

async function setupRabbitMQ() {
    try {
        if (!rabbitMQConfigured) {
            const connection = await amqp.connect(rabbitMQUrl);
            const channel = await connection.createChannel();
            await channel.assertQueue(queueName, { durable: true });
            console.log(`Fila RabbitMQ '${queueName}' criada e pronta para receber mensagens.`);
            rabbitMQConfigured = true;
        }
    } catch (error) {
        console.error('Erro ao configurar RabbitMQ:', error.message);
    }
}

app.on('receber-dados', async (data) => {
    const id = data.id;
    const coordenadas = data.coordenadas;

    await setupRabbitMQ();

    try {
        const connection = await amqp.connect(rabbitMQUrl);
        const channel = await connection.createChannel();

        console.log(`Enviando dados para a fila RabbitMQ '${queueName}'...`);

        await channel.sendToQueue(queueName, Buffer.from(JSON.stringify({ id, coordenadas })), { persistent: true });
    } catch (error) {
        console.error('Erro ao enviar dados para a fila RabbitMQ:', error.message);
    }
});

const client = mqtt.connect(mqttBroker);

client.on('connect', () => {
    console.log('Conectado ao broker MQTT - Assign');

    client.subscribe(mqttTopic);

    client.on('message', (topic, message) => {
        try {
            const data = JSON.parse(message.toString());
            app.emit('receber-dados', data);
        } catch (error) {
            console.error('Erro ao processar mensagem MQTT:', error.message);
        }
    });
});

module.exports = { start: () => app.listen(port, () => console.log(`Servidor API iniciado em http://localhost:${port}`)) };
