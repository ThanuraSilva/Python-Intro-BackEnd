from fastapi import FastAPI
from controller.student_controller import router as student_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="student-data-api",
    version= "1.0.0"
)
# Fix CORS issue

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(student_router)

@app.get("/heart-beat")
def heart_beat():
    return {"message":"Student API is Running"}