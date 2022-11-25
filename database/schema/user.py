from pydantic import BaseModel
import uuid


class user(BaseModel):

    id: uuid.UUID
    nick: str
    phone_number: str
    country: str
    city: str
    points: int
    address: str
    email: str
    password: str
    badges: list[Badge]

