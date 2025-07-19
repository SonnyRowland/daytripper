from fastapi import FastAPI

from app.database import Base, engine
from app.routers import places

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tripper API", description="Day trip planner")

app.include_router(places.router)


@app.get("/")
def root():
    return {"health": "ok"}
