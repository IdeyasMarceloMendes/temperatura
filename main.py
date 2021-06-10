from decouple import config
import requests
import json
DEBUG=True
if DEBUG:
    key = f"key={config('KEY')}"
    format = "format=json"
    locale = "locale=pt"
    json_file = open("cidades.json","r").read()
    json_file = json.loads(json_file)
    for value in json_file:
        id = value["id"]
        cidade=f"woeid={id}"
        print(cidade)
        url = f"https://api.hgbrasil.com/weather?{key}&{cidade}&{format}&{locale}/"
        r = requests.get(url)
        response = json.loads(r.text)
        response = response['results']
        print(response)
        input("\n aperte enter para ver a proxima cidade.")
