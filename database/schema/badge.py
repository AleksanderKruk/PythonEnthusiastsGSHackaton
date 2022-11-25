from pydantic import BaseModel
import uuid


class Badge(BaseModel):
    id: uuid.UUID
    name: str
    icon_url: str
