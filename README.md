# Insult as a Service (IaaS)

## This is a simple API that lets you insult people

Usage: send a GET request to `/insult/random/{name}` and the API will return a JSON object looking like this:

```json
{
    "status":"ok",
    "insult":"{name} is a stupid asshat"
}
```

Here's a simple python program to get an insult for a name:

```py
from requests import get

def insult(name: str):
    result = get(f"http://localhost:8008/insult/random/{name}").json()
    return result['insult']

print(insult("Bob"))
```

---

## API Routes

### `GET /`
Retuns a list of endpoints.

### `GET /insult/random`
Return an insult for a random name.

### `GET /insult/random/{name}`
Return an insult for a name.

### `GET /insult/random/{name}/{amount}`
Return a list of insults for a name, to a maximum of 32.

### `GET /insult/randomdouble`
Return an insult with 2 adjectives for a random name.

### `GET /insult/randomdouble/{name}`
Return an insult with 2 adjectives for a name.

### `GET /insult/randomdouble/{name}/{amount}`
Return a list of insults with 2 adjectives for a name, to a maximum of 32.

---

### Server Setup

- Make a copy of `docker-compose.example.yml` called `docker-compose.yml`
- Run `docker-compose up -d`
- By default the server runs on port 8008, but this can be changed in `docker-compose.yml`

---

### Contributing

More adjectives and nouns are always welcome to be added to `data/random.json`, just add some and make a pull request.