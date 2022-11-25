from pydantic import BaseModel
import uuid


class Gadget(BaseModel):
    id: uuid.UUID
    point_cost: int
    image_url: str

    def __init__(self, uuid: uuid.UUID, point_cost: int, image_url: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = uuid
        self.point_cost = point_cost
        self.image_url = image_url



