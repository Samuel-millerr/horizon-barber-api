from fastapi import FastAPI

from horizon_barber_api.routers.user_router import user_router

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(user_router, prefix="/users", tags=["User"])