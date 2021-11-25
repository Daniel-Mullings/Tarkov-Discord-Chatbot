import sqlite3
import discord
from discord import message
from Ammo import SelectCell
import api_market_handler
from datetime import datetime

client = discord.Client()
def word_checker(message):
    keywords = {
        "price" :["price", "cost", "worth", "value",],
        "info": ["info", "information", "details", "Damage", "Penetration", "ArmourDamageChance", "AccuracyChange", "RecoilChange", "FragmentChance", "RicochetChance", "LightBleedChance", "HeavyBleedChance", "Velocity", "SpecialEffects"],
        "stats": ["stats", "statistics"]
    }
    keys = keywords.keys()

    for word in message.content.split():
        for key in keys:
            if str(word).lower() in str(keywords.get(key)).lower() or str(word).lower() == str(key).lower():
                return key
    return "no procedure"
  
def ammonamechecker(message):
    ammonames = getammolist()
    for word in message.split():
        for ammo in ammonames:
            if str(word).upper() in str(ammo).upper():
                return ammo

    return "no ammo"

def getammolist():
    connection = sqlite3.connect("ammoTable.db")
    cursor = connection.cursor()
    filedata = cursor.execute("SELECT Name FROM Ammo ORDER BY Name")
    content = filedata.fetchall()
    connection.commit()
    connection.close()
    return content

def ammodata(message):
    valuesnames = ["Damage", "Penetration", "ArmourDamageChance", "AccuracyChange", "RecoilChange", "FragmentChance", "RicochetChance", "LightBleedChance", "HeavyBleedChance", "Velocity", "SpecialEffects"]
    for word in message.split():
        for value in valuesnames:
            if str(word).lower() in str(value).lower():
                return value
    return "Name"


@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client) + " @ " + datetime.now().strftime("%H:%M:%S"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        procedure = word_checker(message)
    if procedure == "no procedure":
        await message.channel.send("do nothing")
    else:
        await eval(procedure + "(message)")
        
async def price(message):
    if message.author == client.user:
        return
    else:
        if api_market_handler.isItemNamePresent(message.content):
            response = "The " + api_market_handler.getItemName(str(message.content)) + " costs " + str(api_market_handler.getItemPrice(api_market_handler.getItemName(str(message.content)), "tMarket"))
            await message.channel.send(response)
        else:
            await message.channel.send(api_market_handler.isItemNamePresent)

async def info(message):
    if message.author == client.user:
        return
    else:
        ammoname = str(ammonamechecker(message.content)[0])
        ammovalue = str(ammodata(message.content))
        print(ammoname, ammovalue)
        if ammoname != "no ammo":
            data = SelectCell("ammoTable.db", ammovalue, ammoname)
            await message.channel.send(data)
    return

async def stats(message):
    if message.author == client.user:
        return
    else:
        await message.channel.send("stats")


client.run('ODk5NDQ2MTUxNzM5MjE1OTMy.YWy4gQ.PI_BS8TljX4jD8Hb-DToge-1nA8')