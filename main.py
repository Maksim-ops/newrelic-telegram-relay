from flask import Flask, request
from flask_restful import Resource, Api
from telegram import send_telegram_message
import json
import os

app = Flask(__name__)
api = Api(app)


with open('config/telegram.json') as f:
    telegram_config = json.load(f)

token = telegram_config['botToken']
chat_ids = telegram_config['receiverChatIds']


class WebHook(Resource):
    def post(self):
        payload = request.json
        print('Received webhook.')
        print(payload)
        for chat_id in chat_ids:
            print('Sending message to telegram chat: ' + chat_id)
            state = payload.get('current_state')
            if state == 'open':
                state_title = '🚨 ' + \
                    payload.get('event_type') + ' ' + state
            else:
                state_title = '✅ ' + \
                    payload.get('event_type') + ' ' + state
            message = "*" + state_title + '*\n' \
                '*Policy*: ' + payload.get('policy_name') + '\n' \
                '*Details*: ' + payload.get('details') + '\n' \
                '*Time*: ' + payload.get('timestamp_utc_string') + '\n' \
                '[Chart](' + payload.get('violation_chart_url') + ')'
            send_telegram_message(token, chat_id, message)
        return 'OK'


api.add_resource(WebHook, '/webhook')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('APP_PORT', 5000))
    app.run(host='0.0.0.0', port=port)
