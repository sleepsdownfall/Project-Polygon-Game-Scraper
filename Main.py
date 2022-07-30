# Made by sleep
# dsc.bio/sleeps

import requests
import os

print("##########################################################################################")
print("                             Made by sleep#0802 | dsc.bio/sleeps")
print("Enter your polygon session. This can be found with the Edit This Cookie browser extension.")
print("                             Made by sleep#0802 | dsc.bio/sleeps")
print("##########################################################################################")
polygon_session = input()

os.system("CLS")

def getPage(page):
    cookies = {
        'polygon_session': polygon_session,
        'farewell': '1',
    }
    headers = {
        'origin': 'https://polygon.pizzaboxer.xyz',
        'referer': 'https://polygon.pizzaboxer.xyz/games',
        'user-agent': 'Hey Pizzaboxer! from sleep <3',
        'x-polygon-csrf': '0111969040dad49c9f55764856c520c20d1ae3b76ac723608921d6a0e835003a',
    }

    data = {
        'FilterBy': 'Default',
        'FilterVersion': 'All',
        'Query': '',
        'Page': page,
    }
    return requests.post('https://polygon.pizzaboxer.xyz/api/games/fetch', cookies=cookies, headers=headers, data=data) 

for x in range(56):
    response = getPage(x + 1)
    parse = response.json()
    for y in range(len(parse["items"])):
        url = "https://pizzaboxer.xyz/asset?id=" + str(parse["items"][y]["PlaceID"])
        download = requests.get(url)
        print("downloading " + str(parse["items"][y]["Name"]+".rbxl") + " Place ID: " + str(parse["items"][y]["PlaceID"]))
        open(str(parse["items"][y]["Name"]+".rbxl"), "wb").write(download.content)
