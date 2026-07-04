from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Request(BaseModel):
    request: str


@app.post("/agent")
def agent(req: Request):

    return {
        "message": req.request
    }