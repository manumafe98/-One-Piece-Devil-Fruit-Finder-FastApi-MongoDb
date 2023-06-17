from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import main_app

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(main_app.router)




