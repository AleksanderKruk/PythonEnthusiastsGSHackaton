#from pydantic import BaseModel
import uuid


class Gadgets:
    id: uuid.UUID
    name: str
    point_cost: int
    image_url: str
   
    def __init__(self, uuid: uuid, name: str, point_cost: int, image_url: str):
        self.id = uuid
        self.name = name
        self.point_cost = point_cost
        self.image_url = image_url

    def insert(self, id: uuid.UUID, name: str=None, point_cost: int=None, image_url: str=None):
        name = "NULL" if name is None else name
        point_cost = "NULL" if point_cost is None else str(point_cost)
        image_url = "NULL" if image_url is None else image_url
        return f'INSERT INTO GADGETS VALUES({id}, {name}, {point_cost}, {image_url});'

    def delete(self, condition: str):
        return f'DELETE FROM GADGETS WHERE {condition}'

    def update(self, id: uuid=None, name: str=None, point_cost: int=None, image_url: str=None, condition :str = None):
        column1 = f'ID = {id}' if id is not None else ''
        column2 = f'NAME = {name}' if name is not None else ''
        column3 = f'POINT_COST = {point_cost}' if point_cost is not None else ''
        column4 = f'IMAGE_URL = {image_url}' if image_url is not None else ''
        if column4 != '':
            column3 += ','
        if column3 != '':
            column2 += ','
        if column2 != '':
            column1 += ','
        cond = ''
        cond = f'WHERE {cond}' if condition is not None else ''

        return f'UPDATE GADGETS SET {column1} {column2} {column3} {column4} {cond}'
