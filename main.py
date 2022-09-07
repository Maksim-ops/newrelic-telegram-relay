from flask import Flask, request
from flask_restful import Resource, Api
from telegram import send_telegram_message
import json
import os

app = Flask(__name__)
api = Api(app)

with open('config/telegram.json') as f:
    telegram_config = json.load(f)

bot_token = telegram_config['botToken']
chat_id = telegram_config['chatId']

class WebHook(Resource):
    def post(self):
        payload = request.json
        print('Received webhook.')
        print(payload)
        if hasattr(payload, 'bot_token'):
            bot_token_loc = payload.get('bot_token')
        else:
            bot_token_loc = bot_token
        if hasattr(payload, 'chat_id'):
            chat_id_loc = payload.get('chat_id')
        else:
            chat_id_loc = chat_id
        print('Sending message to telegram chat: ' + chat_id_loc)
        try:
            res = send_telegram_message(bot_token_loc, chat_id_loc, json.dumps(payload))
            return res
        except Exception as e:
            return e

api.add_resource(WebHook, '/webhook')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
