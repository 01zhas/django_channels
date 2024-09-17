import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.client_ip = self.scope['client'][0]  
        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_value = text_data_json['message_key']

        data = {
            'message_key': message_value,
            'ip': self.client_ip
        }
        self.send(text_data=json.dumps(data))