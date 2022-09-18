import os
from time import time

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # suppress tensorflow debug prompt

from transformers import pipeline, set_seed


def TextGen(
    inputText: str,
    returnSeq: int,
    maxLen: int,
    modeltype="distilgpt2",
    **seed: int | None
) -> str:

    generator = pipeline("text-generation", model=str(modeltype))

    # set_seed(69)

    textGen = generator(
        inputText,
        max_length=maxLen,
        num_return_sequences=returnSeq,
    )
    return textGen


if __name__ == "__main__":
    with open("outputs.txt", "a") as file:
        st = time()
        x = 0
        for i in TextGen("once upon a time,", 2, 100):
            print(i)
            # file.write('<|startoftext|>============================ \n ')
            # file.write(str(x)+ ' '+str(i["generated_text"])+ '<|endoftext|>\n')
            # x+=1
        et = time()
        elapsed_time = et - st
        print("Execution time:", elapsed_time, "seconds")
