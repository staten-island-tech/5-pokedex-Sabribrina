""" import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex) """

""" ask = int(input("what pokemon want?"))
value = data[ask]["name"]
print("name is", value)
lang = input("what language?")
print(data[ask]["name"][lang]) """

""" yoo = input("heyyeuyruy what type of pokemon?")
for mon in data:
    if yoo in mon["type"]:
        print(mon["name"])
else:
    print("There is none u bad bad boy") """

""" ehe = input("search for pokemon :D")
for mon in data:
    if ehe in mon["name"]["english"]:
        print(mon["name"])["english"]
else:
    print("no pokepokemons") """

import json
pokedex = open("./moves.json", encoding="utf8")
data = json.load(pokedex)

urgh = input("hiyaa what type of pokemon do u wanna see its moves?")
for mon in data:
    if urgh in mon["type"]:
        print(mon["ename"])
else:
    print("nuh uh u BIG BAD boy")