from fastapi import FastAPI

from app.database import Base, engine
from app.routers import places, postcode

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tripper API", description="Day trip planner")

app.include_router(places.router)
app.include_router(postcode.router)


@app.get("/")
def root():
    return {"health": "ok"}
