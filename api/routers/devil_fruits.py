from db.client import db_client
from fastapi import APIRouter, HTTPException, status
from db.models.devil_fruits import DevilFruitsModel
from db.schemas.devil_fruits import devil_fruit_schema, devil_fruits_schema

router = APIRouter(prefix="/devil_fruits", 
                   tags=["devil_fruits"], 
                   responses={status.HTTP_404_NOT_FOUND: {"error": "Something went wrong"}})


@router.get("/", response_model=list[DevilFruitsModel], status_code=status.HTTP_200_OK)
async def get_all_devil_fruits():
    """
    Retrieve all devil fruits.

    Returns:
    - list[DevilFruitsModel]: List of devil fruits.
    """
    return devil_fruits_schema(db_client.devil_fruits.find())


@router.post("/", response_model=DevilFruitsModel, status_code=status.HTTP_201_CREATED)
async def add_a_devil_fruit(devil_fruit: DevilFruitsModel):
    """
    Add a new devil fruit.

    Args:
    - devil_fruit (DevilFruitsModel): The devil fruit to add.

    Returns:
    - DevilFruitsModel: The newly added devil fruit.

    Raises:
    - HTTPException: If the devil fruit already exists (status code 400).

    """
    found = db_client.devil_fruits.find_one({"devil_fruit_name": devil_fruit.devil_fruit_name})
    if found:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The devil fruit already exists")

    devil_fruit_dict = dict(devil_fruit)
    id = db_client.devil_fruits.insert_one(devil_fruit_dict).inserted_id

    new_devil_fruit = devil_fruit_schema(db_client.devil_fruits.find_one({"_id": id}))

    return DevilFruitsModel(**new_devil_fruit)


@router.get("/{devil_fruit}", status_code=status.HTTP_200_OK)
async def get_a_devil_fruit(devil_fruit: str):
    """
    Get details of a specific devil fruit by name.

    Args:
    - devil_fruit (str): Name of the devil fruit.

    Returns:
    - dict: Details of the devil fruit.
    """
    return search_devil_fruit_by_name(devil_fruit)


@router.delete("/{devil_fruit}", status_code=status.HTTP_200_OK)
async def delete_a_devil_fruit(devil_fruit: str):
    """
    Delete a specific devil fruit by name.

    Args:
    - devil_fruit (str): Name of the devil fruit to delete.

    Returns:
    - dict: A dictionary with a success message.
    """
    found_devil_fruit = search_devil_fruit_by_name(devil_fruit)
    db_client.devil_fruits.delete_one({"devil_fruit_name": found_devil_fruit.devil_fruit_name})
    return {"message": "Devil fruit deleted succesfully"}


@router.put("/{devil_fruit}", response_model=DevilFruitsModel, status_code=status.HTTP_200_OK)
async def update_a_devil_fruit(devil_fruit: str, devil_fruit_model: DevilFruitsModel):
    """
    Update a specific devil fruit by name.

    Args:
    - devil_fruit (str): Name of the devil fruit to update.
    - devil_fruit_model (DevilFruitsModel): Updated devil fruit details.

    Returns:
    - dict: Updated details of the devil fruit.

    Raises:
    - HTTPException: If the devil fruit is not found and cannot be updated.
    """
    devil_fruit_dict = dict(devil_fruit_model)

    try:
        db_client.devil_fruits.find_one_and_replace({"devil_fruit_name": devil_fruit}, devil_fruit_dict)
        return search_devil_fruit_by_name(devil_fruit)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Devil fruit was not found so cannot be updated")


@router.patch("/{devil_fruit}", response_model=DevilFruitsModel, status_code=status.HTTP_200_OK)
async def patch_a_devil_fruit(devil_fruit: str, devil_fruit_data: dict):
    """
    Patch/update a specific devil fruit by name with partial data.

    Args:
    - devil_fruit (str): Name of the devil fruit to patch/update.
    - devil_fruit_data (dict): Partial data to update the devil fruit.

    Returns:
    - dict: Updated details of the devil fruit.

    Raises:
    - HTTPException: If the devil fruit is not found and cannot be updated.
    """
    try:
        attribute_to_update = next(iter(devil_fruit_data))
        new_attribute_value = devil_fruit_data[attribute_to_update]

        update_query = {"$set": {attribute_to_update: new_attribute_value}}

        db_client.devil_fruits.find_one_and_update({"devil_fruit_name": devil_fruit}, update_query)
        return search_devil_fruit_by_name(devil_fruit)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Devil fruit was not found so cannot be updated")


def search_devil_fruit_by_name(devil_fruit: str):
    """
    Search for a devil fruit by its name.

    Args:
    - devil_fruit (str): Name of the devil fruit to search.

    Returns:
    - DevilFruitsModel: Details of the devil fruit.

    Raises:
    - HTTPException: If the devil fruit is not found.
    """
    try:
        devil_fruit = db_client.devil_fruits.find_one({"devil_fruit_name": devil_fruit})
        return DevilFruitsModel(**devil_fruit_schema(devil_fruit))
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Devil fruit not found")


# TODO dockerize the api and the mongodb
# TODO add information to the readme