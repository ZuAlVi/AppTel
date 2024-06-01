from fastapi import FastAPI, HTTPException

from src.database import clients
from src.schemas import LoginRequest, SendMessageRequest, SendMediaRequest
from src.telethon_client import TelegramService

app = FastAPI()


@app.post("/login")
async def login(request: LoginRequest):
    phone = request.phone
    if phone not in clients:
        clients[phone] = TelegramService(phone)
    qr_path = await clients[phone].generate_qr_code()
    return {"qr_link_url": f"http://localhost:8000/{qr_path}"}


@app.get("/check/login")
async def check_login(phone: str):
    if phone not in clients:
        raise HTTPException(status_code=404, detail="Phone not found")
    status = await clients[phone].check_login()
    return {"status": status}


@app.get("/messages")
async def get_messages(phone: str, uname: str):
    if phone not in clients:
        raise HTTPException(status_code=404, detail="Phone not found")
    messages = await clients[phone].get_messages(uname)
    return {"messages": messages}


@app.post("/messages")
async def send_message(request: SendMessageRequest):
    phone = request.from_phone
    if phone not in clients:
        raise HTTPException(status_code=404, detail="Phone not found")
    status = await clients[phone].send_message(request.username, request.message_text)
    return {"status": status}


@app.post("/media")
async def send_media(request: SendMediaRequest):
    phone = request.from_phone
    if phone not in clients:
        raise HTTPException(status_code=404, detail="Phone not found")
    status = await clients[phone].send_media(request.username, request.file_path, request.media_type)
    return {"status": status}

