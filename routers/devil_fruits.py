from fastapi import APIRouter, HTTPException, status
from db.client import db_client

router = APIRouter(prefix="/devil_fruits", tags=["devil_fruits"])

router.get("/")
async def get_all_devil_fruits():
    return {}


router.post("/")
async def add_a_devil_fruit():
    return {}


router.get("/{devil_fruit}")
async def get_a_devil_fruit():
    return {}


router.delete("/{devil_fruit}")
async def delete_a_devil_fruit():
    return {}


router.put("/{devil_fruit}")
async def update_a_devil_fruit():
    return {}


router.get("/{devil_fruit}")
async def patch_a_devil_fruit():
    return {}
