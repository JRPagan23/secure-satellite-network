 Secure Satellite Networking

This is **Project 6** in my end-to-end satellite cybersecurity series. This module establishes a **secure satellite-ground MQTT communication system** using TLS with certificate-based mutual authentication.

---

## Features

- Encrypted MQTT communication over port `8883` using TLS
- X.509 certificate-based mutual authentication (CA-signed)
- Simulated telemetry broadcast: battery %, temperature
- `mosquitto_sub` used as the secure ground station listener
- Built entirely in Python with Paho MQTT client

---

## Project Structure

secure-satellite-network/
├── ca.crt # Root Certificate Authority
├── ca.key # CA private key
├── satellite.crt # Satellite client certificate
├── satellite.key # Satellite private key
├── ground.crt # Ground station certificate
├── ground.key # Ground station private key
├── mosquitto.conf # Mosquitto broker TLS configuration
├── satellite_node.py # Python script simulating the satellite
├── ground_station/ # Placeholder for future GUI/CLI tools
├── README.md


---

##  How to Run

### 1. Start the MQTT Broker with TLS

```bash
mosquitto -c mosquitto.conf
Make sure the paths to ca.crt, ground.crt, and ground.key are correctly set in mosquitto.conf.
2. Launch the Satellite Telemetry Node
cd satellite
python3 satellite_node.py
This will simulate the satellite sending encrypted telemetry messages every few seconds.

3. Receive Data as Ground Station
mosquitto_sub -h localhost -p 8883 \
  --cafile ../ca.crt \
  --cert ../ground.crt \
  --key ../ground.key \
  -t "satellite/data"
Certificate Security

All certificates used in this project are signed by a custom root Certificate Authority (CA). The broker (mosquitto) is configured to require client certificates, enforcing mutual authentication for all connected nodes.

 Sample Output

Telemetry: battery=83%, temp=24C
Telemetry: battery=82%, temp=23C
Telemetry: battery=81%, temp=23C
Project Goals

This project simulates how secure telemetry is transmitted from a spacecraft (or satellite) to a ground station. It demonstrates:

TLS encryption in IoT/satellite communication
Secure certificate generation and validation
Broker authentication enforcement

Author

Jorge Rodriguez
Cybersecurity Student @ STCC | Focused on satellite and interdimensional communications
GitHub: JRPagan2399

Keywords

MQTT · TLS · Cybersecurity · Satellites · IoT · Paho MQTT · Mosquitto · Python
