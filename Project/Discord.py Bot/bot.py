import discord
import os
from discord.ext import commands

class CustomHelpCommand(commands.HelpCommand):
    
    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):
        for cog in mapping:
            await self.get_destination().send(f'{cog.qualified_name}: {[command.name for command in mapping[cog]]}')

    async def send_cog_help(self, cog):
        await self.get_destination().send(f'{cog.qualified_name}: {[command.name for command in cog.get_commands()]}')

    async def send_group_help(self, group):
        await self.get_destination().send(f'{group.name}: {[command.name for index, command in enumerate(group.commands)]}')

    async def send_command_help(self, command):
        await self.get_destination().send(command.name)

client = commands.Bot(command_prefix = '$', help_command=commands.MinimalHelpCommand())

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


path = 'Project\Discord.py Bot\cogs'
for filename in os.listdir(path):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')   


client.run("MTAyOTQ5NTk5MzI4MjA4NDg3NA.G6AIif.8dTat6ZQEQDao3c6aQneqlGBf6-SCZjFuZ1rBY")