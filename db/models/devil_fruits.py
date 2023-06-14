from pydantic import BaseModel


class DevilFruitsModel(BaseModel):
    devil_fruit_name: str
    devil_fruit_type: str
    current_user: str
    devil_fruit_img: str
