from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import get_predict
from app.model.model import __version__ as version


app = FastAPI()


class In(BaseModel):
    text: str


class Out(BaseModel):
    language: str


@app.get("/")
def home():
    return {"Check": "Ok", "version": version}


@app.post("/predict", response_model=Out)
def predict(payload: In):
    result = get_predict(payload.text)
    return {"result": result}

