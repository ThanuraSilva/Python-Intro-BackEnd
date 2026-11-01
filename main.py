from fastapi import FastAPI
from controller.student_controller import router as student_router

app = FastAPI(
    title="student-data-api",
    version= "1.0.0"
)

app.include_router(student_router)

@app.get("/heart-beat")
def heart_beat():
    return {"message":"Student API is Running"}