from discord.ext import commands
from dotenv import dotenv_values
import discord
import os
import random

client = commands.Bot(command_prefix = '-')
config = dotenv_values(".env")

# ================
# Cog Commands
# ================


@client.command()
async def load(ctx, ext):
    client.load_extension(f'cogs.{ext}')


@client.command()
async def unload(ctx, ext):
    client.unload_extension(f'cogs.{ext}')


# ============
# Loading Cogs
# ============


for file in os.listdir('./cogs'):
    if file.endswith('.py'):
        client.load_extension(f'cogs.{file[:-3]}')


client.run(config['token'])