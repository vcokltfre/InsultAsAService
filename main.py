from fastapi import FastAPI
from typing import Optional
from random import choice
from loader import iload, nload

app = FastAPI()

insults = iload("random")
names = nload()
nouns, adjectives = insults['nouns'], insults['adjectives']
many_cap = 32

def clamp(min: int, max: int, num: int):
    if num > max: return max
    if num < min: return min
    return num

def get_an(word):
    if word[0] in 'aeiou':
        return f"an {word}"
    return f"a {word}"

def get_one(name):
    adj, noun = choice(adjectives), choice(nouns)
    insult = f"{name} is {get_an(adj)} {noun}"
    data = {
        "status": "ok",
        "insult": insult
    }
    return data

def get_two(name):
    adj, adj2, noun = choice(adjectives), choice(adjectives), choice(nouns)
    insult = f"{name} is {get_an(adj)} {adj2} {noun}"
    data = {
        "status": "ok",
        "insult": insult
    }
    return data

def get_one_many(name, amount: int):
    amount = clamp(1, many_cap, amount)
    insults = [data['insult'] for data in [get_one(name) for _ in range(amount)]]
    data = {
        "status": "ok",
        "insults": insults
    }
    return data

def get_two_many(name, amount: int):
    amount = clamp(1, many_cap, amount)
    insults = [data['insult'] for data in [get_two(name) for _ in range(amount)]]
    data = {
        "status": "ok",
        "insults": insults
    }
    return data

@app.get("/insult/random")
async def get_one_insult():
    return get_one(choice(names))

@app.get("/insult/randomdouble")
async def get_two_insults():
    return get_two(choice(names))

@app.get("/insult/random/{name}/{amount}")
async def get_one_many_named(name: str, amount: int):
    return get_one_many(name, amount)

@app.get("/insult/randomdouble/{name}/{amount}")
async def get_one_many_named(name: str, amount: int):
    return get_two_many(name, amount)

@app.get("/insult/random/{name}")
async def get_one_insult_named(name: str):
    return get_one(name)

@app.get("/insult/randomdouble/{name}")
async def get_two_insults_named(name: Optional[str]):
    return get_two(name)

@app.get("/insult/list/adjectives")
async def get_adj():
    return adjectives

@app.get("/insult/list/nouns")
async def get_nouns():
    return nouns