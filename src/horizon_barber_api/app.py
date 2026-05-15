from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from horizon_barber_api.routers.barber_service_router import barber_servicer_router
from horizon_barber_api.routers.user_router import user_router
from horizon_barber_api.routers.appointment_router import appointment_router

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
app.include_router(barber_servicer_router, prefix="/barber-services", tags=["Barber"])
app.include_router(appointment_router, prefix="/appointments", tags=["Appointment"])