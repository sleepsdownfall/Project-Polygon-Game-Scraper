# Project Polygon Game Scraper
Scrapes and downloads games off of Pizzaboxer's Project Polygon (a roblox revival)

https://polygon.pizzaboxer.xyz/

Due to polygon shutting down, I had the idea to make a script to download all of the games from polygon.

This will only download from the 56 pages of games that polygon currently has at the time of writing this (30/07/2022). I was too lazy to automate it to get the maximum amount of pages, and made this in a rush to give to my friend.

# How To Use

## Step 1
Download Main.py

## Step 2
Get your CSRF token by going to https://polygon.pizzaboxer.xyz/, opening inspect element (ctrl + shift + i), going to console, and pasting this script here:
```
console.log(document.getElementsByName('polygon-csrf')[0].content)
```
## Step 3
Get your "polygon_session" cookie, by using the edit this cookie browser extension

## Step 4
Open Main.py, enter your cookie, then after that, enter your csrf token

Once all those steps have been completed, you should be automatically downloading all of polygon's games.
