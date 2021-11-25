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
        "info": ["info", "information", "details",],
        "stats": ["stats", "statistics"]
    }
    keys = keywords.keys()

    for word in message.content.split():
        for key in keys:
            if word in keywords.get(key) or word == key:
                return key
    return "no procedure"
  
def ammonamechecker(message):
    ammonames = getammolist()
    for word in message.content.split():
        for ammo in ammonames:
            if word in ammo:
                return ammo

    return "Name"

def getammolist():
    connection = sqlite3.connect("ammoTable.db")
    cursor = connection.cursor()
    filedata = cursor.execute("SELECT Name FROM Ammo ORDER BY Name")
    content = filedata.fetchall()
    connection.commit()
    connection.close()
    return content

def ammodata(message):
    values = ["Damage", "Penetration", "ArmourDamageChance", "AccuracyChange", "RecoilChange", "FragmentChance", "RicochetChance", "LightBleedChance", "HeavyBleedChance", "Velocity", "SpecialEffects"]
    for word in message.content.split():
        for value in values:
            if word in value:
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
        if api_market_handler.isItemNamePresent(message):
            response = "The " + api_market_handler.getItemName(str(message.content)) + " costs " + str(api_market_handler.getWeaponTraderPrice(api_market_handler.getItemName(str(message.content))))
            await message.channel.send(response)
        else:
            await message.channel.send(api_market_handler.isItemNamePresent)

async def info(message):
    if message.author == client.user:
        return
    else:
        connection = sqlite3.connect("ammoTable.db")
        data = SelectCell("ammoTable.db", ammonamechecker(message), ammodata(message))
        await message.channel.send(data)
        connection.commit()
        connection.close()
    return

async def stats(message):
    if message.author == client.user:
        return
    else:
        await message.channel.send("stats")


client.run('ODk5NDQ2MTUxNzM5MjE1OTMy.YWy4gQ.PI_BS8TljX4jD8Hb-DToge-1nA8')