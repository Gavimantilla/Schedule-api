# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import Response
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/subjects")
def get_subject_data():
    filepath = os.path.join(os.path.dirname(__file__), "shared_data", "subject_data.json")
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        return Response(content=content, media_type="application/json; charset=utf-8")
    return {"error": "subject_data.json no encontrado"}
