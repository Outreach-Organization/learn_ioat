import React, { useState, useEffect } from 'react';
import { Card, Button } from 'antd';
import mqtt from 'mqtt';

const Connection = ({ connectBtn }) => {
  const [connected, setConnected] = useState(false);
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    const client = mqtt.connect({
      protocol: 'ws',
      hostname: 'localhost',
      port: 8084,
    });

    client.on('connect', () => {
      setConnected(true);
      client.subscribe('python/mqtt');
    });

    client.on('message', (topic, message) => {
      const newMessage = {
        topic,
        message: message.toString(),
      };
      setMessages((prevMessages) => [...prevMessages, newMessage]);
    });

    client.on('close', () => {
      setConnected(false);
    });

    return () => {
      client.end();
    };
  }, []);

  return (
    <Card title="Connection Status">
      <p>Connected: {connected ? 'Yes' : 'No'}</p>
      <div>
        <h4>Subscribed Messages:</h4>
        {messages.map((message, index) => (
          <div key={index}>
            <p>Topic: {message.topic}</p>
            <p>Message: {message.message}</p>
          </div>
        ))}
      </div>
    </Card>
  );
};

export default Connection;

