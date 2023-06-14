from fastapi import APIRouter, HTTPException, status
from db.models.devil_fruits import DevilFruitsModel
from db.client import db_client
from db.schemas.devil_fruits import devil_fruit_schema, devil_fruits_schema

router = APIRouter(prefix="/devil_fruits", 
                   tags=["devil_fruits"], 
                   responses={status.HTTP_404_NOT_FOUND: {"error": "Something went wrong"}})

@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_devil_fruits():
    return {}


@router.post("/", response_model=DevilFruitsModel, status_code=status.HTTP_201_CREATED)
async def add_a_devil_fruit(devil_fruit: DevilFruitsModel):

    devil_fruit_dict = dict(devil_fruit)
    id = db_client.devil_fruits.insert_one(devil_fruit_dict).inserted_id

    new_devil_fruit = devil_fruit_schema(db_client.devil_fruits.find_one({"_id": id}))

    return DevilFruitsModel(**new_devil_fruit)


@router.get("/{devil_fruit}", response_model=DevilFruitsModel, status_code=status.HTTP_200_OK)
async def get_a_devil_fruit(devil_fruit: str):
    db_client.devil_fruits.find_one({"devil_fruit_name": devil_fruit})
    return {}


@router.delete("/{devil_fruit}", status_code=status.HTTP_200_OK)
async def delete_a_devil_fruit(devil_fruit: str):
    return {}


@router.put("/{devil_fruit}", status_code=status.HTTP_200_OK)
async def update_a_devil_fruit(devil_fruit: str):
    return {}


@router.get("/{devil_fruit}", status_code=status.HTTP_200_OK)
async def patch_a_devil_fruit(devil_fruit: str):
    return {}
