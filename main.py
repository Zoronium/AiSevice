from enum import Enum
from fastapi import FastAPI , Request 
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from starlette.responses import FileResponse

from textCompl import TextGen

app = FastAPI()
app.mount("/template", StaticFiles(directory="template"), name="template")
class ModelEnum(str, Enum):
    gpt2 = "gpt2"
    gpt2_story = "pranavpsv/gpt2-genre-story-generator"
    gpt2Distil = "distilgpt2"
    gpt2l = "gpt2-large"


class UserInput(BaseModel):
    inputText: str
    returnSeq: int
    maxLen: int
    seed: int | None


@app.get("/")
def readRoot():
    return {"Hello": "World"}


# @app.post("/textgen")
# def readItem(userinput: UserInput):

#     generateText = TextGen(
#         userinput.inputText,
#         userinput.returnSeq,
#         userinput.maxLen
#     )
#     return {
#         "YourInput": userinput,
#          "output": {
#             "Prediction": generateText
#         }
#     }


@app.post("/textgen")
def readItem(userinput: UserInput, model: ModelEnum | None):

    generateText = TextGen(
        userinput.inputText, userinput.returnSeq, userinput.maxLen, model.value
    )
    return {
        "YourInput": userinput,
        "Model": model,
        "output": {"Prediction": generateText},
    }


@app.get("/form" , response_class=HTMLResponse)
def upgardeItems(request: Request):
    return FileResponse('template/base.html')
