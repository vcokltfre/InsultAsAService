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

### Server Setup

- Rename `docker-compose.example.yml` to `docker-compose.yml`
- Run `docker-compose up -d`
- By default the server runs on port 8008, but this can be changed in `docker-compose.yml`

---

### Contributing

More adjectives and nouns are always welcome to be added to `data/random.json`, just add some and make a pull request.