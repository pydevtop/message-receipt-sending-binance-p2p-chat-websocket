"""
================================================================================
Project: Message Sending Binance P2P Chat WebSocket
Author : pydevtop
GitHub : https://github.com/pydevtop/message-sending-binance-p2p-chat-websocket
Date   : 2025-09-09
Site: https://py-dev.top
================================================================================

Description:
This script connects to Binance P2P chat via WebSocket and allows sending messages.


Usage:
1. Set your Binance API key and secret below.
2. Run this script: python main.py
================================================================================
"""
import requests
import hmac, hashlib
import threading
import os
import json
import uuid
import websocket
from time import sleep, asctime, time
from config import Config

setting = Config()


def getServerTime():

    timestamp = int(time() * 1000)
    return timestamp


def getSignatureTrader():
    query_string = f"timestamp={getServerTime()}"
    secret = setting.api_secret
    return hmac.new(secret.encode("utf-8"), query_string.encode("utf-8"), hashlib.sha256).hexdigest()


##################
## Binance Chat ##
##################

def retrieveChatCredential():

    base_url = "https://api.binance.com"

    endpoint = "/sapi/v1/c2c/chat/retrieveChatCredential"

    headers = {
        "clientType": "web",
        "X-MBX-APIKEY": setting.api_key
    }

    url = f"{base_url}{endpoint}?{getServerTime()}&signature={getSignatureTrader()}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return None

res_detail = retrieveChatCredential()

if res_detail:
    chatWssUrl = res_detail['data']['chatWssUrl']
    listenKey = res_detail['data']['listenKey']
    listenToken = res_detail['data']['listenToken']
    chat_wss_url = f"{chatWssUrl}/{listenKey}?token={listenToken}&clientType=web"

else:
    raise Exception("Failed to obtain credentials for WebSocket.")

def generate_uuid():
    return str(uuid.uuid4())



def send_message(content, order_no):
    if ws_connection:
        message_uuid = generate_uuid()
        response_message = {
            "type": "text",
            "uuid": message_uuid,
            "orderNo": order_no,
            "content": content,
            "self": True,
            "clientType": "web",
            "createTime": getServerTime(),
            "sendStatus": 0
        }


        try:

           ws_connection.send(json.dumps(response_message))
           print(f"Notify Binance Chat mes:{content} #{order_no}")
        except Exception as e:
            print(f"Message sent error: {str(e)}")




def send_receipt(order_no: str, file_path: str):

    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    image_name = os.path.basename(file_path)

    headers = {
        "clientType": "web",
        "X-MBX-APIKEY": setting.api_key
    }

    parameters = {
        "timestamp": getServerTime(),
        "signature": getSignatureTrader()
    }

    payload = {"imageName": image_name}

    resp = requests.post(
        "https://api.binance.com/sapi/v1/c2c/chat/image/pre-signed-url",
        json=payload,
        headers=headers,
        params=parameters
    )
    resp_json = resp.json()
    print(f"Pre-signed URL response: {resp_json}")

    if not resp_json.get("success"):
        print(f"Failed to get pre-signed URL: {resp_json}")
        return

    uploadUrl = resp_json["data"]["uploadUrl"]
    image_url = resp_json["data"]["imageUrl"]

    with open(file_path, 'rb') as f:
        response = requests.put(
            uploadUrl,
            data=f,
            headers={"Content-Type": "image/jpeg"}
        )

    from PIL import Image
    im = Image.open(file_path)
    width, height = im.size

    message_uuid = generate_uuid()

    response_message = {
        "uuid": message_uuid,
        "type": "image",
        "orderNo": order_no,
        "createTime": getServerTime(),
        "thumbnailUrl": image_url,
        "imageUrl": image_url,
        "imageType": "jpeg",
        "self": True,
        "clientType": "web",
        "width": width,
        "height": height,
        "sendStatus": 0
    }

    try:
        ws_connection.send(json.dumps(response_message))
        print(f"Receipt sent for order {order_no}: {image_url}")
    except Exception as e:
        print(f"send_receipt error: {str(e)}")



def on_open(ws):
    global ws_connection
    ws_connection = ws
    print("WebSocket connection  established for Chat")

    print("WebSocket connection established for Chat")


def on_message(ws, message):
    try:
        parsed_message = json.loads(message)
        print(f"parsed_message: {parsed_message}")
    except json.JSONDecodeError:
        print("Error JSON:", message)
        print(f"Error JSON:: {message}")

def on_error(ws, error):
    print(f"Error WebSocket: {error}")
    print("Error WebSocket:", error)

def on_close(ws, close_status_code, close_msg):
    global reconnect_attempts
    print("WebSocket connection closed.", close_msg)

    if reconnect_attempts < 5:
        reconnect_attempts += 1
        print(f"Attempting to reconnect ({reconnect_attempts})...")
        sleep(5)
        connect_to_websocket()
    else:
        print("The maximum number of reconnection attempts has been reached.")

reconnect_attempts = 0
ws_connection = None

def connect_to_websocket():
    global reconnect_attempts, ws
    reconnect_attempts = 0
    ws = websocket.WebSocketApp(
        chat_wss_url,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.run_forever()


######################
## Binance Chat END ##
######################

if __name__ == "__main__":

    websocket_thread = threading.Thread(target=connect_to_websocket)
    websocket_thread.start()
    sleep(2)
    send_message(setting.notify_seller_text, setting.order_no)
    file_path = r"C:\webSocetBinance\receipt.jpg"
    send_receipt(setting.order_no, file_path)




