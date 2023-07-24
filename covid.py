import requests
from win11toast import toast
import json
import time
def update():
    r=requests.get("https://coronavirus-19-api.herokuapp.com/all")
    data=r.json()
    text="Confirmed Cases:{}\n Deaths :{}\nRecovered:{}".format(data['cases'],data['deaths'],data['recovered'])
    while True:
        toast('Covid-19 Updates',text,duration=20)
        time.sleep(60)
update()