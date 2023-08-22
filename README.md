# A Real-time Gaming Framework for IoT and Smart Agriculture Teaching

## Description

The Real-time Gaming Framework for IoT and Smart Agriculture is an educational project that introduces the concepts of IoT, sensor integration, MQTT protocol, and real-time data visualization through an interactive game. This README provides an overview of the framework's components and how to get started.

<img width="1225" alt="Screenshot 2023-08-22 at 11 49 43 AM" src="public/screen.png">

## Table of Contents

- [Getting Started](#getting-started)
  - [IoT Board Tutorial](#iot-board-tutorial)
  - [MQTT Protocol](#mqtt-protocol)
  - [Realtime Data Visualization](#realtime-data-visualization)
- [Gameplay](#gameplay)
  - [Soil Moisture Level Control](#soil-moisture-level-control)
  - [Reward-Based Gaming Control](#reward-based-gaming-control)
- [Usage](#usage)
  - [Clone the Repository](#clone-the-repository)
- [About the Gaming Framework](#about-the-gaming-framework)
- [Implementation Details](#implementation-details)
  - [Arduino Setup](#arduino-setup)
  - [Mosquitto Broker Installation](#mosquitto-broker-installation)
    - [Configure Mosquitto for Websockets](#configure-mosquitto-for-websockets)
  - [Python Setup](#python-setup)
  - [Start the React App](#start-the-react-app)
- [Enjoy the Game](#enjoy-the-game)

## Getting Started

### IoT Board Tutorial

Learn how to connect sensors (e.g., soil moisture) and actuators (e.g., water pump) using an Arduino device. Follow the provided tutorial to understand the hardware setup. Coming soon...

### MQTT Protocol

Explore the MQTT protocol, a widely used data protocol for IoT. Understand its use and implementation in establishing communication between devices. Coming soon...

### Realtime Data Visualization

Learn how to visualize real-time data from sensors. This part of the framework will help you grasp the concept of visualizing data for better understanding.

## Gameplay

### Soil Moisture Level Control

Experience controlling the soil moisture level of a virtual plant. Understand how the framework simulates this interaction and provides feedback.

### Reward-Based Gaming Control

Engage in a reward-based game where taking care of the virtual plant results in earning points and achieving higher levels.

## Usage

### Clone the Repository

To use this framework, clone the repository to your local machine. This will provide you with all the necessary code and resources to set up the game and explore its components.

```bash
git clone https://github.com/Shakoor-Lab-Organization/learn_ioat.git
```

## About the Gaming Framework

The gaming framework is designed to simulate the care of a virtual plant using React, a popular web development library. The game emphasizes monitoring the plant's moisture level and accomplishing goals to progress.

## Implementation Details

### Arduino Setup

1. Install Arduino IDE from https://www.arduino.cc/en/software.
2. Obtain a water pump and soil moisture sensor that are Arduino compatible.
3. Use Arduino IDE to upload the provided code (.ino file) to your Arduino device.

### Mosquitto Broker Installation

Install the Mosquitto broker with the following commands:

```bash
sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
sudo apt-get update
sudo apt-get install mosquitto
```

### Configure Mosquitto for Websockets

To enable websockets for the Mosquitto broker, follow these steps:

1. Open the Mosquitto configuration file using a text editor:

    ```bash
    sudo nano /etc/mosquitto/mosquitto.conf
    ```

2. Add the following lines to enable websockets:

    ```yaml
    listener 1883
    listener 8080
    protocol websockets
    ```

3. Save and close the file.

### Start Mosquitto Broker

Before running the game, you need to start the Mosquitto broker to enable MQTT communication:

1. Start the Mosquitto broker with the provided configuration:

    ```bash
    mosquitto -c /etc/mosquitto/mosquitto.conf
    ```


### Python Setup

Before running the game, ensure you have the necessary Python packages installed:

1. Install Python packages for MQTT and serial connectivity:

    ```bash
    pip install paho-mqtt
    pip install pyserial
    ```

2. Start MQTT client and serial connectivity:

    ```bash
    cd learn_ioat
    cd serial_mqtt
    sudo python serial_pub.py
    ```

### Start the React App

To launch the game's interface, follow these steps:

1. Navigate to the React app directory:

    ```bash
    cd learn_ioat
    npm start
    ```

2. Enjoy the game!

### Enjoy the Game

Congratulations! You have set up the Real-time Gaming Framework for IoT and Smart Agriculture. Explore the different components, learn about IoT concepts, and have fun taking care of your virtual plant. This framework is a great way to learn about IoT in an interactive and engaging manner. Happy learning!

