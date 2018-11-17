import json

#tworze pytonowy obiekt

meble = ["krzesło","szafa","komoda","stół"]
print(type(meble))
meble_as_json = json.dumps(meble)
print((type(meble_as_json)))
print(meble_as_json)

meble_odczytane_z_json = json.loads(meble_as_json)

print((type(meble_odczytane_z_json)))
print(meble_odczytane_z_json)

with open("meble.json", "w") as f:
    json.dump(meble,f)   #tworzy plik z treścią meble

with open("meble.json") as f:
    meble = json.load(f)
    meble.append("taboret")

print(meble)

with open("meble.json", "w") as f:
    json.dump(meble,f)
