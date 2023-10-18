const mqtt = require('mqtt');
const axios = require('axios');

// Configurações MQTT
const mqttBroker = 'mqtt://seu_broker_mqtt.com';
const mqttTopic = 'topico/requisicoes';

// Configurações da API com fila
const apiUrl = 'https://sua-api.com/receber-dados';

// Criar um cliente MQTT
const client = mqtt.connect(mqttBroker);

// Evento chamado quando o cliente MQTT se conecta ao broker
client.on('connect', () => {
    console.log('Conectado ao broker MQTT');
    client.subscribe(mqttTopic);
});

// Evento chamado quando uma mensagem é recebida no tópico especificado
client.on('message', (topic, message) => {
    try {
        // Decodificar a mensagem JSON recebida
        const data = JSON.parse(message.toString());

        // Enviar os dados para a API com fila usando Axios
        axios.post(apiUrl, data)
            .then(response => {
                console.log('Dados enviados com sucesso para a API. Status:', response.status);
            })
            .catch(error => {
                console.error('Erro ao enviar dados para a API:', error.message);
            });
    } catch (error) {
        console.error('Erro ao processar mensagem MQTT:', error.message);
    }
});

// Lidar com erros de conexão MQTT
client.on('error', (error) => {
    console.error('Erro de conexão MQTT:', error);
});

