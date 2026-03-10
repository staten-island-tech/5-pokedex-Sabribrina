import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)

for index, data in enumerate(pokedex):
    print(index, ":", data["name"])

