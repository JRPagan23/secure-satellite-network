import ssl
import time
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 8883
TOPIC = "ground/commands"

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("🌍 Ground station connected securely to broker.")
    else:
        print(f"❌ Connection failed with code {rc}")

client = mqtt.Client(client_id="ground1")

client.tls_set(
    ca_certs="../certs/ca.crt",
    certfile="../certs/ground.crt",
    keyfile="../certs/ground.key",
    cert_reqs=ssl.CERT_REQUIRED,
    tls_version=ssl.PROTOCOL_TLS_CLIENT
)

client.on_connect = on_connect

client.connect(BROKER, PORT)
client.loop_start()

# Send a command
try:
    while True:
        cmd = input("📨 Enter command for satellite (or 'exit'): ")
        if cmd.lower() == "exit":
            break
        client.publish(TOPIC, cmd)
        print(f"✅ Sent command: {cmd}")
except KeyboardInterrupt:
    pass

print("📴 Ground station shutting down.")
client.loop_stop()
client.disconnect()
