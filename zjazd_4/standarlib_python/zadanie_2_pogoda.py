#https://docs.python.org/3/howto/urllib2.html
#https://www.metaweather.com/api/
import json
import urllib.request
import sys
from collections import namedtuple

Weather = namedtuple("Weather", ["location", "temperature", "humidity", "air_pressure"]) # ta tupla nadaje nazwy swoim indeksom, żeby było łatwiej się do nich odwołać

if __name__= "__main__":
    #pobierz id dla lokalizacji
    #pobierz pogodę
    #pokaż id

    location_id = get_location_id(sys.argv[1])
    print(location_id)

#location = input("Podaj lokalizację: ")

basic_url = 'https://www.metaweather.com/api/location/search/?query='
#url_for_location = basic_url + location
url_for_location = basic_url + location_id
#location_data = urllib.request.urlopen(full_url)

with urllib.request.urlopen(url_for_location) as url:
    location_ids = json.loads(url.read())
    print(location_ids)

for id in location_ids:
    url_for_data_set = basic_url + str(id["woeid"])
    print(url_for_data_set)