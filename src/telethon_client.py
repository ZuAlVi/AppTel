import os

import qrcode
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.auth import ExportLoginTokenRequest, ImportLoginTokenRequest
from telethon.tl.functions.messages import GetHistoryRequest

load_dotenv()

API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')


class TelegramService:
    def __init__(self, phone):
        self.phone = phone
        self.client = None
        self.token = None

    async def generate_qr_code(self):
        self.client = TelegramClient(StringSession(), API_ID, API_HASH)
        await self.client.connect()
        result = await self.client(ExportLoginTokenRequest(api_id=API_ID,
                                                           api_hash=API_HASH,
                                                           except_ids=[]))
        self.token = result.token
        qr_data = self.token.hex()
        img = qrcode.make(qr_data)
        imq_path = f'qr_{self.phone}.png'
        img.save(imq_path)
        return imq_path

    async def check_login(self):
        if not self.client.is_user_authorized():
            try:
                await self.client(ImportLoginTokenRequest(token=self.token))
                await self.client.disconnect()
                return 'logined'
            except:
                return 'waiting_qr_login'
        return 'logined'

    async def get_messages(self, username):
        await self.client.connect()
        entity = await self.client.get_entity(username)
        history = await self.client(
            GetHistoryRequest(peer=entity, limit=50, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0,
                              hash=0))
        messages = [{'username': msg.sender_id, 'is_self': msg.out, 'message_text': msg.message} for msg in
                    history.messages]
        await self.client.disconnect()
        return messages

    async def send_message(self, username, message_text):
        await self.client.connect()
        await self.client.send_message(username, message_text)
        await self.client.disconnect()
        return 'ok'

    async def send_media(self, username, file_path, media_type):
        await self.client.connect()
        entity = await self.client.get_entity(username)

        if media_type == 'photo':
            await self.client.send_file(entity, file_path, caption="Here is a photo")
        elif media_type == 'video':
            await self.client.send_file(entity, file_path, caption="Here is a video")
        elif media_type == 'document':
            await self.client.send_file(entity, file_path, caption="Here is a document")

        await self.client.disconnect()
        return 'ok'
