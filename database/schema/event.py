from pydantic import BaseModel
import uuid


class Event(BaseModel):
    id: uuid.UUID
    name: str
    start_iso: str
    end_iso: str

