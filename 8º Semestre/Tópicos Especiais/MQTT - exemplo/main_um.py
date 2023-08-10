import paho.mqtt.client as mqtt
import random
import time

# Configurações do MQTT
mqtt_broker_host = "localhost"
mqtt_broker_port = 1883
topic = "random_number"

# Função para gerar número aleatório
def generate_random_number():
    return random.randint(1, 100)

# Callback quando a conexão MQTT for estabelecida
def on_connect(client, userdata, flags, rc):
    print("Conectado ao broker MQTT")
    
# Inicialização do cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect

# Conexão ao broker MQTT
client.connect(mqtt_broker_host, mqtt_broker_port, keepalive=60)

# Loop para gerar e publicar números aleatórios
while True:
    random_number = generate_random_number()
    client.publish(topic, random_number)
    print("Número aleatório gerado:", random_number)
    time.sleep(5)  # Espera por 5 segundos
