from discord.ext import commands
import discord

class General_Commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.dnd, activity=discord.Streaming(name="Don't click on my stream", url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
        print(f'logged in as {self.client.user.name}')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.client.latency * 1000)}ms')
        

def setup(client):
    client.add_cog(General_Commands(client))