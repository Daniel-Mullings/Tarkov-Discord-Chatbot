import os
import discord
import api_market_handler
from datetime import datetime

client = discord.Client()
def word_checker(message):
    keywords = ["price", "cost", "worth", "value", "info", "information", "details", "stats", "statistics"]
    for word in keywords:
        if word in message.content:
            return word
    return "no procedure"
  

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
        if api_market_handler.isWeaponNamePresent(message.content):
            response = "The " + api_market_handler.getWeaponName(str(message.content)) + " is worth " + str(api_market_handler.getWeaponPrice(api_market_handler.getWeaponName(str(message.content)))) + " Rubles"
            await message.channel.send(response)
        elif api_market_handler.isAmmoNamePresent(message.content):
            response = "The " + api_market_handler.getAmmoName(str(message.content)) + " ammo type is worth " + str(api_market_handler.getAmmoPrice(api_market_handler.getAmmoName(str(message.content)))) + " Rubles"
            await message.channel.send(response)
        else:
            await message.channel.send("ERROR")

async def info(message):
    if message.author == client.user:
        return
    else:
        await message.channel.send("info")

async def stats(message):
    if message.author == client.user:
        return
    else:
        await message.channel.send("stats")

async def cost(message):
    if message.author == client.user:
        return
    else:
        await price(message)

async def worth(message):
    if message.author == client.user:
        return
    else:
        await price(message)

async def value(message):
    if message.author == client.user:
        return
    else:
        await price(message)

async def information(message):
    if message.author == client.user:
        return
    else:
        await info(message)
 
async def details(message):
    if message.author == client.user:
        return
    else:
        await info(message)

async def statistics(message):
    if message.author == client.user:
        return
    else:
        await stats(message)


client.run('ODk5NDQ2MTUxNzM5MjE1OTMy.YWy4gQ.PI_BS8TljX4jD8Hb-DToge-1nA8')