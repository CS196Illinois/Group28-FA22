# bot.py
import csv
from fileinput import filename
import os
import json
import discord
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import pandas as pd

client = pymongo.MongoClient("mongodb+srv://discord:abcd@cluster0.uqbxcn6.mongodb.net/?retryWrites=true&w=majority")
db = client.userFile

load_dotenv()
json_file_path = "C:/Users/nagav/Documents/GitHub/Group28-FA22/Project/env.json"

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
        db.server_user_log.insert_one(
            {
                "message": message.content,
                "author": message.author.id
            }
        )
    elif message.content.startswith('Instructions'):
        await message.channel.send(f'Upload a CSV file ')
    
    elif message.attachments[0].url.endswith('csv'):
        await message.channel.send(f'{message.author} thank u sir')
        header = ["date", "type", "symbol", "shares", "share", "price", "costs", "fees", "total amount", "div amount", 
                "shares affected	currency"	"rate"	"cash affected", "name", "comment", "brokerage", "id", "taxes",	
                "credits", "rate currency",	"acb per share", "uuid", "linked uuid", "use rate ccy", "provider"]

        df = pd.read_csv(message.attachments[0])
        # db.server_file_log.insert_many(df)
        csvfile = open(df, 'r')
        reader = csv.DictReader( csvfile )

        for each in reader:
            row={}
            for field in header:
                row[field]=each[field]
            db.server_file_log.insert(row)
        
    else:
        await message.channel.send(f'{message.author} Goofy asl I asked for a csv lmao')

client.run(TOKEN)