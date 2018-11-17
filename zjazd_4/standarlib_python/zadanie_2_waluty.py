import json
import urllib.request

with urllib.request.urlopen("http://api.nbp.pl/api/exchangerates/tables/A?format=json") as f:
    print(f)
    kursy = json.loads(f.read())

rates = kursy[0]["rates"]
for r in rates:
    print("- ", r["code"], " : ", r["mid"])

waluta = input("Podaj kod waluty: ")
ile = input("Ile chcesz kupić?: ")

for r in rates:
    if r["code"] == waluta.upper():
        # print("Kurs średni ", r["code"], ": ", r["mid"])
        result = ile * r["mid"]

print("Płacisz: ", result)