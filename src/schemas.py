from pydantic import BaseModel


class LoginRequest(BaseModel):
    phone: str


class SendMessageRequest(BaseModel):
    message_text: str
    from_phone: str
    username: str


class SendMediaRequest(BaseModel):
    from_phone: str
    username: str
    media_type: str
    file_path: str
