const mqtt = require('mqtt');
const axios = require('axios');

// Configurações MQTT
const mqttBroker = 'mqtt://localhost'; // Substitua pelo seu broker MQTT
const mqttTopic = 'topico/dados';

// Configurações da API com fila
const apiUrl = 'https://sua-api.com/receber-dados'; // Substitua pela URL da sua API

// Cria um cliente MQTT
const client = mqtt.connect(mqttBroker);

// Evento chamado quando o cliente MQTT se conecta ao broker
client.on('connect', () => {
  console.log('Conectado ao broker MQTT');

  // Subscreve ao tópico MQTT
  client.subscribe(mqttTopic);
});

// Evento chamado quando uma mensagem é recebida no tópico especificado
client.on('message', async (topic, message) => {
  try {
    // Decodificar a mensagem JSON recebida
    const data = JSON.parse(message.toString());

    // Enviar os dados para a API com fila usando Axios
    const response = await axios.post(apiUrl, data);

    // Verificar o status da resposta
    if (response.status === 200) {
      console.log('Dados enviados com sucesso para a API');
    } else {
      console.error('Erro ao enviar dados para a API. Código de status:', response.status);
    }
  } catch (error) {
    console.error('Erro ao processar mensagem MQTT:', error.message);
  }
});

// Lidar com erros de conexão MQTT
client.on('error', (error) => {
  console.error('Erro de conexão MQTT:', error);
});
