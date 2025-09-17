from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routers import admin, places, postcode

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tripper API", description="Day trip planner")

app.include_router(places.router)
app.include_router(postcode.router)
app.include_router(admin.router)

origins = ["http://localhost:5173", "https://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"health": "ok"}
