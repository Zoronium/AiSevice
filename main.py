from enum import Enum
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

from textCompl import TextGen

app = FastAPI()


class ModelEnum(str, Enum):
    gpt2 = "gpt2"
    gpt2_story = "pranavpsv/gpt2-genre-story-generator"
    gpt2Distil = "distilgpt2"
    gpt2l = "gpt2-large"


def Choice(model):
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


@app.post("/textgen/")
def readItem(userinput: UserInput, model: ModelEnum | None):

    generateText = TextGen(
        userinput.inputText, userinput.returnSeq, userinput.maxLen, model.value
    )
    return {
        "YourInput": userinput,
        "Model": model,
        "output": {"Prediction": generateText},
    }


# @app.put("/items/{item_id}")
# def upgardeItems(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}
