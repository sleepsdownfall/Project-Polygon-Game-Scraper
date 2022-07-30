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

print("##########################################################################################")
print("                             Made by sleep#0802 | dsc.bio/sleeps")
print("                               Enter your polygon Csrf Token.")
print("                             Made by sleep#0802 | dsc.bio/sleeps")
print("##########################################################################################")

polygon_csrf = input()

os.system("CLS")

print("##########################################################################################")
print("                             Made by sleep#0802 | dsc.bio/sleeps")
print("                             The games should be downloading now.")
print("                             Made by sleep#0802 | dsc.bio/sleeps")
print("##########################################################################################")

def get_page(page):
    cookies = {
        'polygon_session': polygon_session,
        'farewell': '1',
    }
    headers = {
        'user-agent': 'Hey Pizzaboxer! from sleep <3',
        'x-polygon-csrf': polygon_csrf,
    }

    data = {
        'FilterBy': 'Default',
        'FilterVersion': 'All',
        'Query': '',
        'Page': page,
    }
    return requests.post('https://polygon.pizzaboxer.xyz/api/games/fetch', cookies=cookies, headers=headers, data=data) 

invalid_characters = {"/", "\\", ":", "*", "?", "\"", "<", ">", "|"}

for x in range(56):
    response = get_page(x + 1)
    parse = response.json()
    for y in range(len(parse["items"])):
        url = "https://polygondev.pizzaboxer.xyz/asset?id=" + str(parse["items"][y]["PlaceID"])
        download = requests.get(url)
        print("downloading " + str(parse["items"][y]["Name"]+".rbxl") + " Place ID: " + str(parse["items"][y]["PlaceID"]))
        place_name = str(parse["items"][y]["Name"])
        for character in invalid_characters:
            place_name = place_name.replace(character, "")
        open(place_name+".rbxl", "wb").write(download.content)
