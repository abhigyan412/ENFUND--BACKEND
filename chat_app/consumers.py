import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings  
from channels.layers import get_channel_layer
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.channel_layer = get_channel_layer() 
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

       
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
       
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]
        email = data.get("email", "").strip().lower() 

        
        if email not in settings.ALLOWED_CHAT_USERS:
            return  

        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "email": email,
            }
        )

    async def chat_message(self, event):
       
        await self.send(text_data=json.dumps({"message": event["message"], "email": event["email"]}))
