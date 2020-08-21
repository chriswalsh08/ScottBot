# Import modules
import discord
import random
from discord import Embed
from discord.ext import commands

# Create Gambling cog


class Gambling(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Coin flip command
    @commands.command(brief="Flip a coin")
    async def coinflip(self, ctx):
        choices = ["heads", "tails"]
        coin = random.choice(choices)
        embed = Embed(
            title="Flipping coin...",
            description="The result is " + coin + "!",
            colour=ctx.author.colour
        )
        await ctx.send(embed=embed)

    # Roll dice command
    @commands.command(brief="Roll from the following dice: d4, d6, d8, d10, d20, d100")
    async def roll(self, ctx, dice):
        if dice == 'd4' or dice == '1d4':
            roll = random.randrange(1, 5)
            await ctx.send("*rolling...*")
            await ctx.send(roll)
            if roll == 4:
                await ctx.send("IT'S A CRIT, BABY! DOUBLE THOSE DICE!")
            if roll == 1:
                await ctx.send("Critfail... rocks fall and everyone dies! Maybe try rerolling a druid?")
        if dice == 'd6' or dice == '1d6':
            roll = random.randrange(1, 7)
            await ctx.send("*rolling...*")
            await ctx.send(roll)
            if roll == 6:
                await ctx.send("IT'S A CRIT, BABY! DOUBLE THOSE DICE!")
            if roll == 1:
                await ctx.send("Critfail... rocks fall and everyone dies! Maybe try rerolling a fighter?")
        if dice == 'd8' or dice == '1d8':
            roll = random.randrange(1, 9)
            await ctx.send("*rolling...*")
            await ctx.send(roll)
            if roll == 8:
                await ctx.send("IT'S A CRIT, BABY! DOUBLE THOSE DICE!")
            if roll == 1:
                await ctx.send("Critfail... rocks fall and everyone dies! Maybe try rerolling a wizard?")
        if dice == 'd10' or dice == '1d10':
            roll = random.randrange(1, 11)
            await ctx.send("*rolling...*")
            await ctx.send(roll)
            if roll == 10:
                await ctx.send("IT'S A CRIT, BABY! DOUBLE THOSE DICE!")
            if roll == 1:
                await ctx.send("Critfail... rocks fall and everyone dies! Maybe try rerolling a monk?")
        if dice == 'd20' or dice == '1d20':
            roll = random.randrange(1, 21)
            await ctx.send("*rolling...*")
            await ctx.send(roll)
            if roll == 20:
                await ctx.send("NAT 20, BABY! DOUBLE THOSE DICE!")
            if roll == 1:
                await ctx.send("Critfail... rocks fall and everyone dies! Maybe try getting better armor?")
        if dice == 'd100' or dice == '1d100':
            roll = random.randrange(1, 101)
            await ctx.send("*rolling...*")
            await ctx.send(roll)
            if roll == 100:
                await ctx.send("IT'S A CRIT, BABY! DOUBLE THOSE DICE!")
            if roll == 1:
                await ctx.send("Critfail... rocks fall and everyone dies! Maybe try looking for traps next time?")

    ###### ERRORS ######

    # Dice roll error
    @roll.error
    async def roll_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please choose a dice! i.e., '.roll 1d20'")


def setup(client):
    client.add_cog(Gambling(client))
