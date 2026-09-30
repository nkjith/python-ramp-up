import httpx
from pydantic import BaseModel

class Species(BaseModel):
    name :str
    url: str

class Pokemon(BaseModel):
    id: int
    name: str
    height : int
    weight: int
    species : Species

url = "https://pokeapi.co/api/v2/pokemon/pikachu"

with httpx.Client() as client:
    response = client.get(url=url)
    pokemon = Pokemon.model_validate(response.json())
    print(pokemon.species.name)