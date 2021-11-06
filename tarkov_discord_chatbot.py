import os
import discord
import api_market_handler

client = discord.Client()
def word_checker(message):
    keywords = ["price", "info", "stats"]
    for word in keywords:
      if word in message.content:
        return word
    return "no procedure"
  

@client.event
async def on_ready():
  print("we have logged in as {0.user}".format(client))


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
    if api_market_handler.WeaponNamePresent(message.content):
      response = "The " + api_market_handler.GetWeaponName(str(message.content)) + " is worth " + str(api_market_handler.GetWeaponPrice(api_market_handler.GetWeaponName(str(message.content)))) + " Rubles"
      await message.channel.send(response)
    elif api_market_handler.AmmoNamePresent(message.content):
      response = "The " + api_market_handler.GetAmmoName(str(message.content)) + " ammo type is worth " + str(api_market_handler.GetAmmoPrice(api_market_handler.GetAmmoName(str(message.content)))) + " Rubles"
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
  
client.run('ODk5NDQ2MTUxNzM5MjE1OTMy.YWy4gQ.PI_BS8TljX4jD8Hb-DToge-1nA8')
