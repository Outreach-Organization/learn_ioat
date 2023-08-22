import serial
import time
import paho.mqtt.client as mqtt


ser = serial.Serial('/dev/ttyACM0',9600,timeout=5)
#ser.flushInput()
#ser.flushOutput()
#ser.write("get") 

# sleep(1) for 100 millisecond delay
# 100ms dely
#time.sleep(.1)
#print ser.read()



# MQTT Configuration
BROKER_HOST = "localhost"
BROKER_PORT = 1883
TOPIC = "plant/moistureLevel"


# MQTT client setup
mqtt_client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    """Callback function when the MQTT client connects to the broker."""
    print("Connected to MQTT broker")
    client.subscribe("plant/command")


def on_message(client, userdata, msg):
    """Callback function when a message is received on a subscribed topic."""
    print(msg.payload.decode())
    if msg.topic == "plant/command":
        command = msg.payload.decode()
        if command == "start":
            ser.write(b'led_on')
        elif command == "stop":
            ser.write(b'led_off')
    else:
        print("Received message on topic:", msg.topic)
        print("Message:", msg.payload.decode())

# Set the callback functions
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

# Connect to the MQTT broker
mqtt_client.connect(BROKER_HOST, BROKER_PORT)

# Start the MQTT client loop
mqtt_client.loop_start()

# Main loop
while True:
    line = ser.readline().decode().strip()  # read input from Arduino
    if line.isdigit():
        value = int(line)
        print("Arduino moisture level:", value)
        mqtt_client.publish(TOPIC, value)

