import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import requests
from .models import Devicedata

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        url = "http://13.233.13.254:2222/xenergyData.json"

        response = requests.request("GET", url, headers={}, data={})
        # print(response.json()['records'][0])
        for i in response.json()['records']:
            l = i['tdata'].split(',')
            query = Devicedata.objects.filter(imei=i['vid'],created_on=i['created'])
            if len(query)==0:
                data = Devicedata(imei=i['vid'],datavia=i['datavia'],latitude=l[1],longitude=l[2],cell1v=l[3],cell2v=l[4],cell3v=l[5],cell4v=l[5],cell5v=l[6],cell6v=l[7],cell7v=l[8],cell8v=l[9],cell9v=l[10],cell10v=l[11],cell11v=l[12],cell12v=l[13],cell13v=l[14],cell14v=l[15],avgv=l[16],packv=l[17],current=l[17],soc=l[18],created_on=i['created'])
                data.save()
            else:
                break
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))