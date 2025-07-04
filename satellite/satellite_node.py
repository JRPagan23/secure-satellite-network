import paho.mqtt.client as mqtt
import ssl
import time

BROKER = "localhost"
PORT = 8883
TOPIC = "satellite/data"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)

def on_disconnect(client, userdata, rc):
    print("Disconnected with result code", rc)

client = mqtt.Client(client_id="satellite1")
client.on_connect = on_connect
client.on_disconnect = on_disconnect

# ✅ Replace with actual paths (these are correct for your setup)
client.tls_set(
    ca_certs="/Users/jorgerodriguezpagan/Downloads/secure-satellite-network/ca.crt",
    certfile="/Users/jorgerodriguezpagan/Downloads/secure-satellite-network/satellite.crt",
    keyfile="/Users/jorgerodriguezpagan/Downloads/secure-satellite-network/satellite.key",
    tls_version=ssl.PROTOCOL_TLS_CLIENT
)

client.tls_insecure_set(False)

client.connect(BROKER, PORT)
client.loop_start()

try:
    while True:
        payload = "Telemetry: battery=82%, temp=23C"
        client.publish(TOPIC, payload)
        print("Sent:", payload)
        time.sleep(5)
except KeyboardInterrupt:
    print("Exiting.")
finally:
    client.loop_stop()
    client.disconnect()

