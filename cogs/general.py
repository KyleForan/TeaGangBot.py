from discord.ext import commands
import discord

class General(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.client.latency * 1000)}ms')
        

def setup(client):
    client.add_cog(General(client))