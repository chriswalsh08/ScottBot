# Import modules
import discord
from discord.ext import commands

# Create Moderation cog


class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Ban command
    @commands.command(brief="Bans target with reason")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} has been deemed unworthy. BANNED!')

    # Kick command
    @commands.command(brief="Kicks target with reason")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention}. Get him outta here!')


def setup(client):
    client.add_cog(Moderation(client))
