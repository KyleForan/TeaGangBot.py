from discord.ext import commands
import discord

class Error_Handeling(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, err):
        
        if isinstance(err, commands.MissingRequiredArgument):
            await ctx.send('Please use specified args')

        elif isinstance(err, commands.CommandNotFound):
            pass

        elif isinstance(err, commands.MissingPermissions):
            await ctx.send('You don\'t have permission for that command ')

        elif isinstance(err, commands.MemberNotFound):
            await ctx.send('Invalid member')

        elif isinstance(err, commands.MissingPermissions):
            ctx.send('You do not have permission to run that command')

        elif isinstance(err, commands.BotMissingPermissions):
            ctx.send('I do not have permission to run that command')

        elif isinstance(err, commands.ExtensionNotLoaded):
            ctx.send('Extension failed to load')

        elif isinstance(err, commands.ExtensionNotFound):
            ctx.send('Extension not found')

        elif isinstance(err, commands.ExtensionAlreadyLoaded):
            ctx.send('Extension already loaded')

        else: 
            await ctx.send(f'Unknown Error: {err}')
        

def setup(client):
    client.add_cog(Error_Handeling(client))