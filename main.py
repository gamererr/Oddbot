#!/usr/bin/env python3

import random
import asyncio
import discord
import requests
from discord import Member, Embed

with open("tokenfile", "r") as tokenfile:
	token=tokenfile.read()

intents = discord.Intents.all()
client = discord.Client(intents=intents)

async def attachments_to_files(attached,spoiler=False):
	filelist = []
	for i in attached:
		file = await i.to_file()
		filelist.insert(len(filelist),file)

@client.event
async def on_ready():
	print("hello world!")

prefix = "!"

# lists
nuts = ["balls", "nuts", "deez nuts", "mama", "this cock", "my face", "penis", "dickenballs", "cockandnutz"]
ontop = ["oddspray", "gsg"]

# embeds
helpmessage = discord.Embed(title="Commands", description=f'**{prefix}gotem** - sends everything after {prefix}gotem then a random item from a list of genitalia related words"\n**{prefix}ontop** sends "oddspray/gs > a random user in the server"', color=0x7e01e4)


@client.event
async def on_message(message):
    
    args = message.content.lower
    args = message.content.replace(prefix," ")
    argslist = args.split(" ")
    
    if message.content.startswith(prefix):
        if (argslist[1] == "help"):
            helpmessage.color = 0x00C400
            await message.channel.send(embed=helpmessage)
        elif (argslist[1] == "gotem"):
            await message.channel.send(f"{message.content[6:]} {nuts[random.randrange(len(nuts))]}")
        elif (argslist[1] == "ontop"):
            await message.channel.send(f"{ontop[random.randrange(len(ontop))]} > {message.guild.members[random.randrange(len(message.guild.members))].name}")
        elif (argslist[1] == "jokestar"):
            return
        else:
            helpmessage.color = 0xFF0000
            await message.channel.send("unknown command, here is a list of commands", embed=helpmessage)
        
client.run(token)