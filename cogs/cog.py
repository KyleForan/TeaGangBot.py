from logging import debug
from discord.ext import commands
import discord

class Debug(commands.Cog):

    def __init__(self, client) -> None:
        self.client = client

    @commands.command()
    async def load(self, ctx, ext):
        self.client.load_extension(f'cogs.{ext}')
        await ctx.send(f'Loaded {ext}')


    @commands.command()
    async def disable(self, ctx, ext):
        self.client.unload_extension(f'cogs.{ext}')
        await ctx.send(f'Disabled {ext}')

def setup(client):
    client.add_cog(Debug(client))