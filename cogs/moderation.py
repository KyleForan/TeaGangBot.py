from discord.ext import commands
import discord

class Moderation_Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clear(self, ctx, num=10):
        await ctx.channel.purge(limit=num+1)


    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason = 'No reason given'):
        await member.kick(reason=reason)
        await ctx.send(f'kicked {member.mention}')


    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason = 'No reason given'):
        await member.ban(reason=reason)
        await ctx.send(f'banned {member.mention}')


    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        if member[0] == '@': member = member[1:]
        print(member)
        member_name, member_disc = member.split('#')

        for bUser in banned_users:
            user = bUser.user

            if((user.name, user.discriminator) == (member_name, member_disc)):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return
    

def setup(client):
    client.add_cog(Moderation_Commands(client))