from fastapi import FastAPI
from random import choice
from loader import iload

app = FastAPI()

random_insults = iload("random")


@app.get("/insult/random/{name}")
async def get_insult(name: str):
    insult = choice(random_insults).format(name)
    data = {
        "status": "ok",
        "insult": insult
    }
    return data