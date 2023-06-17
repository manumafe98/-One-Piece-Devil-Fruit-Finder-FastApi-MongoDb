from pydantic import BaseModel


class DevilFruitsModel(BaseModel):
    """A Pydantic model representing a Devil Fruit.

    Attributes:
        devil_fruit_name (str): The name of the Devil Fruit.
        devil_fruit_type (str): The type of the Devil Fruit.
        current_user (str): The name of the current user possessing the Devil Fruit.
        devil_fruit_img (str): The image URL of the Devil Fruit.
    """
    devil_fruit_name: str
    devil_fruit_type: str
    current_user: str
    devil_fruit_img: str
