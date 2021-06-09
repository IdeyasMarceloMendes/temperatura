from decouple import config
import requests

DEBUG=True
if DEBUG:
    key=f"key={config('KEY')}"
    format="format=json"
    locale="locale=pt"
    cidade="woeid=455922"#id cidade de  vitória
    url = f"https://api.hgbrasil.com/weather?{key}&{cidade}&{format}&{locale}/"
    r = requests.get(url)
    print(r.text)
