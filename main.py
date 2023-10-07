import uvicorn
import os

from routes import user, cliente

from fastapi import FastAPI

from config import get_settings

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

setting = get_settings()

os.environ["DB_USER"] = setting.db_user
os.environ["DB_PASS"] = setting.db_pass
os.environ["DB_HOST"] = setting.db_host
os.environ["DB_PORT"] = setting.db_port

app.include_router(cliente.router)
app.include_router(user.router)

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8005, log_level="info", reload=True)
