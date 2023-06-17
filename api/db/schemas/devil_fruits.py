def devil_fruit_schema(devil_fruit) -> dict:
    """
    Helper function that converts a devil fruit object into a dictionary schema.

    Args:
        devil_fruit (dict): A dictionary representing a devil fruit object.

    Returns:
        dict: A dictionary containing selected fields from the devil fruit object.
            The dictionary schema includes the following keys:
            - 'devil_fruit_name': The name of the devil fruit.
            - 'devil_fruit_type': The type or category of the devil fruit.
            - 'current_user': The current user of the devil fruit.
            - 'devil_fruit_img': The image URL of the devil fruit.

    """
    return {"devil_fruit_name": devil_fruit["devil_fruit_name"],
            "devil_fruit_type": devil_fruit["devil_fruit_type"],
            "current_user": devil_fruit["current_user"],
            "devil_fruit_img": devil_fruit["devil_fruit_img"]}

def devil_fruits_schema(devil_fruits) -> list:
    """
    Helper function that converts a list of devil fruit objects into a list of dictionary schemas.

    Args:
        devil_fruits (list): A list of devil fruit objects, where each object is a dictionary.

    Returns:
        list: A list of dictionary schemas, where each dictionary represents a devil fruit.

    """
    return [devil_fruit_schema(devil_fruit) for devil_fruit in devil_fruits]
