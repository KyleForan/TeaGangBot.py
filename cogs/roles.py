from discord.ext import commands
import discord

roles = {
    'Engineering': 'Engineering',
    'Maths': 'Maths',
    'Physics': 'Physics',
    'Philosophy': 'Philosophy',
    'Biology': 'Biology',
    'Psychology': 'Psychology',
    'LawPolitics': 'Law & Politics',
}

class Role_React(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, pl):
        msg_id = pl.message_id

        if msg_id == 838895050288267317:
            guild_id = pl.guild_id
            guild = discord.utils.get(self.client.guilds, id=guild_id)

            if pl.emoji.name in roles:
                role = discord.utils.get(guild.roles, name=roles[pl.emoji.name])
            else: 
                raise 'Role not found'

            member = guild.get_member(pl.user_id)

            if not member:
                member = await guild.fetch_member(pl.user_id)

            if member is not None:
                await member.add_roles(role, reason='Chosen with reaction role')
            else:
                print('member not found')


    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, pl):
        msg_id = pl.message_id

        if msg_id == 838895050288267317:
            guild_id = pl.guild_id
            guild = discord.utils.get(self.client.guilds, id=guild_id)

            if pl.emoji.name in roles:
                role = discord.utils.get(guild.roles, name=roles[pl.emoji.name])
            else: 
                raise 'Role not found'

            member = guild.get_member(pl.user_id)

            if not member:
                member = await guild.fetch_member(pl.user_id)

            if member is not None:
                await member.remove_roles(role, reason='Chosen with reaction role')
            else:
                print('member not found')
        

def setup(client):
    client.add_cog(Role_React(client))