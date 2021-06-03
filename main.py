from discord.ext import commands, tasks
from dotenv import dotenv_values
import discord
import os

client = commands.Bot(command_prefix = '-')
config = dotenv_values(".env")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Streaming(name="Don't click on my stream", url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
    print(f'logged in as {client.user.name}')


# ============
# LOADING COGS
# ============


for file in os.listdir('./cogs'):
    if file.endswith('.py'):
        client.load_extension(f'cogs.{file[:-3]}')


client.run(config['token'])