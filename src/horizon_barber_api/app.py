from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from horizon_barber_api.routers.user_router import user_router

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user_router, prefix="/users", tags=["User"])
