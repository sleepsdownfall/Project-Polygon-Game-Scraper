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
        'authority': 'polygon.pizzaboxer.xyz',
        'accept': '*/*',
        'accept-language': 'en,en-US;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'polygon_session=4f250cf24441ee2a8c215e4810952090be3ac99bdfe87317e6e48f5ec62a0b050c985514115508a43488514aa093cb22f6d5f2b09c74fdd2dd9583770a77464a23550b57e55d75ac586b6fa384df168259a930d35a8fb3eb5cad91aa5e89711fd56e228bbcc10a9af1670ddebbae0a5309045cf0d78b15650972c30fd6fc52e7; farewell=1',
        'origin': 'https://polygon.pizzaboxer.xyz',
        'pragma': 'no-cache',
        'referer': 'https://polygon.pizzaboxer.xyz/games',
        'sec-ch-ua': '"Opera GX";v="89", "Chromium";v="103", "_Not:A-Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Hey Pizzaboxer! from sleep <3',
        'x-polygon-csrf': '0111969040dad49c9f55764856c520c20d1ae3b76ac723608921d6a0e835003a',
        'x-requested-with': 'XMLHttpRequest',
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
