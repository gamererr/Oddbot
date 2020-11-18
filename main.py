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

@client.event
async def on_message(message):
    
    args = message.content.lower
    args = message.content.replace(prefix," ")
    argslist = args.split(" ")
    
    if message.content.startswith(prefix):
        if (argslist[1] == "help"):
            await message.channel.send("there are no commands")
        else:
            await message.channel.send(f"thats not a command, use {prefix}help for a list of commands")
        
client.run(token)