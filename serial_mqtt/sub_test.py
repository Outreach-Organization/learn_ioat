import paho.mqtt.client as mqtt

# MQTT Configuration
BROKER_HOST = "localhost"
BROKER_PORT = 1883
TOPIC = "plant/moistureLevel"

# Callback function when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe(TOPIC)

# Callback function when a message is received on a subscribed topic
def on_message(client, userdata, msg):
    print("Received message on topic %s: %s" % (msg.topic, msg.payload.decode()))

# Create an MQTT client instance
client = mqtt.Client()

# Set the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(BROKER_HOST, BROKER_PORT)

# Start the MQTT client loop to listen for incoming messages
client.loop_forever()
