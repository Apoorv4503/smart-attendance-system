from fastapi import FastAPI
from .database import engine
from .models import Base
from .routes.students import router as students_router

app = FastAPI(title="Smart Attendance System API")

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Smart Attendance System Backend Running 🚀"}

app.include_router(students_router)