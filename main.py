from fastapi import FastAPI
from random import choice
from loader import iload

app = FastAPI()

insults = iload("random")
nouns, adjectives = insults['nouns'], insults['adjectives']

def get_an(word):
    if word[0] in 'aeiou':
        return f"an {word}"
    return f"a {word}"

@app.get("/insult/random/{name}")
async def get_insult(name: str):
    adj, noun = choice(adjectives), choice(nouns)
    insult = f"{name} is {get_an(adj)} {noun}"
    data = {
        "status": "ok",
        "insult": insult
    }
    return data

@app.get("/insult/randomdouble/{name}")
async def get_insult(name: str):
    adj, adj2, noun = choice(adjectives), choice(adjectives), choice(nouns)
    insult = f"{name} is {get_an(adj)} {adj2} {noun}"
    data = {
        "status": "ok",
        "insult": insult
    }
    return data

@app.get("/insult/list/adjectives")
async def get_adj():
    return adjectives

@app.get("/insult/list/nouns")
async def get_nouns():
    return nouns