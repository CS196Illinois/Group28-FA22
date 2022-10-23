import discord
import csv
import os
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')

    @commands.command()
    async def testread(self, ctx):
        path = 'Project/Discord.py Bot/bot_test.csv'
        with open(path, 'r+') as beta_test_file:
            reader = csv.reader(beta_test_file)
            for row in reader:
                await ctx.send(f'{row}')

def setup(client):
    client.add_cog(Example(client))