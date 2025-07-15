from fastapi import FastAPI
from app.routers import places
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Tripper API",
    description="Day trip planner"
)

app.include_router(places.router)

@app.get("/")
def root():
    return {"health": "ok"}
