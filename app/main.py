from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.users.routes import router as user_router


app = FastAPI()

app.include_router(router=user_router)

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
