# bot.py
import csv
from fileinput import filename
import os
import json
import discord
from dotenv import load_dotenv

load_dotenv()
json_file_path = "/Users/agilangunashankar/Group28-FA22-1/Project/env.json"

with open(json_file_path, 'r') as j:
     contents = json.loads(j.read())
TOKEN = contents["DISCORD_TOKEN"]
GUILD = contents["DISCORD_GUILD"]

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
    print(
        f'{member.name} is connected to the following guild:\n'
        
    )
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Hello'):
        await message.channel.send(f'Hello {message.author}, my name is the finance bot! Please send me a csv file to work with!')
    if message.attachments[0].url.endswith('csv'):
        await message.channel.send(f'{message.author} thank u sir')
    else:
        await message.channel.send(f'{message.author} Goofy asl I asked for a csv lmao')

client.run(TOKEN)