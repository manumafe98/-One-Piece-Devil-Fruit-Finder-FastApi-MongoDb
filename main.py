from fastapi import FastAPI
from routers import devil_fruits

app = FastAPI()
app.include_router(devil_fruits.router)

