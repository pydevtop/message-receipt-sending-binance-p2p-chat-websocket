# Message and Receipt Sending Binance P2P Chat WebSocket

![Python](https://img.shields.io/badge/python-3.10+-blue) ![License](https://img.shields.io/badge/license-MIT-green)

## Author

**PyDev**  
GitHub: [https://github.com/message-receipt-sending-binance-p2p-chat-websocket](https://github.com/pydevtop/message-receipt-sending-binance-p2p-chat-websocket)

---

<p align="center"><img width="350" src="https://py-dev.top/images/binance/receipt-sending-binance-p2p-chat-websocket-python_300_600.png"></p>

## Description

This Python project enables automated interaction with Binance P2P chat using WebSocket connections.  
With this tool, you can securely send **text messages** and **receipt images** directly to Binance P2P sellers in real-time.  
It leverages the **Binance API** for authentication, credential retrieval, and WebSocket communication.  

This project is ideal for **crypto traders**, **Binance P2P users**, and developers building **automated trading bots** or **messaging tools** for Binance P2P.  
It provides a reliable framework for integrating WebSocket-based messaging in **Python**, handling automatic reconnections and message tracking with **unique UUIDs**.  

**Key benefits:**

- Real-time messaging with Binance P2P sellers  
- Automated image/receipt sending  
- Stable WebSocket connection with auto-reconnect  
- Easy integration into Python trading bots or notification systems  
- Secure handling of Binance API keys  

This tool is especially useful for anyone building **Binance P2P automation**, **crypto notification systems**, or **DeFi trading platforms**.

---

## Features

- Connect to Binance P2P chat via WebSocket  
- Send text messages automatically to sellers  
- Send receipt images to confirm payments  
- Automatic reconnection on WebSocket disconnects  
- Generate unique UUIDs for all messages  
- Lightweight Python implementation with minimal dependencies  

---

## Installation


#### 1. Install Python

Detailed instructions on how to install Python on Windows: https://py-dev.top/installing-python

### 2. Clone the repository:

```bash
git clone https://github.com/pydevtop/message-receipt-sending-binance-p2p-chat-websocket.git
cd message-receipt-sending-binance-p2p-chat-websocket
```
### 3. Create a virtual environment venv:

```bash
python -m venv venv

```


### 4. Activate the environment:

```bash
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/macOS
```

### 5. Install dependencies:

```bash
pip install -r requirements.txt  

```

### 6. API keys to connect to Binance
We create or take existing API Key and Secret Key to connect to the Binance API on the binance website in your account in the section - API Management

APIKey and Secret Key also need to be copied and added to the bot configuration file config.ini


Go to the C drive folder:


```bash
c:\message-receipt-sending-binance-p2p-chat-websocket
```

Go into the settings of the script itself and open config.ini for editing

Enter the settings into config.ini



## ✅ System Requirements

### 🖥️ Operating System
- Windows 10/11  
- macOS  
- Linux (Ubuntu, Debian, etc.)

### 🐍 Python Version
- Python 3.10 or higher

### 📄 Description
- The bot is written in **pure Python** and is **fully cross-platform**.
- Compatible with all major desktop operating systems.
- Only the **startup method** may vary slightly depending on the platform:
  - `.bat` file for **Windows**
  - `.sh` shell script for **Linux/macOS**


## Readmore
[https://py-dev.top/blog/crypto-exchange-development/binance-p2p-receipt-sending-with-python-websocket](https://py-dev.top/blog/crypto-exchange-development/binance-p2p-receipt-sending-with-python-websocket)


## Contacts
Telegram:  @morgan_sql<br>
Telegram channel: https://t.me/pydevtop

## License and Usage Notice

This project is licensed under the MIT License.