from fastapi import FastAPI

app = FastAPI(
    title="Tripper API",
    description="Day trip planner"
)

@app.get("/")
def root():
    return {"health": "ok"}
