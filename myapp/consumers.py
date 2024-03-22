# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import DailyRecord

class QRListConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("attendance_updates", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("attendance_updates", self.channel_name)

    async def send_attendance_updates(self, event):
        await self.send(text_data=json.dumps(event["message"]))
