from fastapi import FastAPI
from infrastructure.adapter.incoming.request_controller import router

app = FastAPI(title="Pomodoro Session API")

app.include_router(router)