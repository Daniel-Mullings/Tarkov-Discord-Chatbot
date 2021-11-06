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
    await message.channel.send("cost")

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
  
client.run(os.environ['btocode'])
