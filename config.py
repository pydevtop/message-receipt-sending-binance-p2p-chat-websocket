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

================================================================================
"""
import os
from configparser import ConfigParser

current_dir = os.path.dirname(os.path.abspath(__file__))

config_path = os.path.join(current_dir, '', 'config.ini')


if not os.path.exists(config_path):
    raise FileNotFoundError(f"Configuration file not found at path {config_path}")

class Config:
    def __init__(self):
        self.cp = ConfigParser()
        self.cp.read(config_path, encoding='utf-8-sig')

        '''setting'''

        self.api_key = self.cp['setting']['api_key']
        self.api_secret = self.cp['setting']['api_secret']
        self.notify_seller_text = self.cp['setting']['notify_seller_text']
        self.order_no = self.cp['setting']['order_no']






