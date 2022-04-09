import requests
#from decouple import config

#token = "sgsegswrgssgrewwrg"


def aztro(sign, day):
    url = "https://sameer-kumar-aztro-v1.p.rapidapi.com/"
    query = {"sign": sign, "day": day}
    headers = {"X-RapidAPI-Host": "sameer-kumar-aztro-v1.p.rapidapi.com",
               "X-RapidAPI-Key":  "04cd38010amsh94b753ec6b17c62p10c407jsn3968076a6722"
               }
    resp = requests.post(url, headers=headers, params=query)
    return resp.json()['description']


aztro('aquarius', 'today')