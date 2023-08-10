import paho.mqtt.client as mqtt

# Configurações do MQTT
mqtt_broker_host = "localhost"
mqtt_broker_port = 1883
topic = "random_number"

# Callback quando uma mensagem for recebida no tópico MQTT
def on_message(client, userdata, msg):
    random_number = int(msg.payload)
    print("Número aleatório recebido:", random_number)

# Inicialização do cliente MQTT
client = mqtt.Client()
client.on_message = on_message

# Conexão ao broker MQTT
client.connect(mqtt_broker_host, mqtt_broker_port, keepalive=60)

# Inscrição no tópico MQTT
client.subscribe(topic)

# Loop para manter a conexão ativa
client.loop_forever()
