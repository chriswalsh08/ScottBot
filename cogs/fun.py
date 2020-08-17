# Import modules
import discord
import random
from discord.ext import commands

# Create Fun cog


class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Almighty Conch command

    @commands.command(aliases=['conch', '8ball', 'eightball'], brief="Ask the Almighty Conch a question")
    async def almightyconch(self, ctx, *, question):
        responses = ['It is certain.',
                     'It is decidedly so.',
                     'Without a doubt!',
                     'Yes, definitely!',
                     'As I see it, yes.',
                     'Jon told me to say yes.',
                     'Of course!',
                     'Signs point to yes.',
                     'Reply hazy... try again.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Cannot predict that now.',
                     'Concentrate and ask again.',
                     'You smell, go away!',
                     "Don't count on it.",
                     'Sorry, Noah told me to say no.',
                     'My reply is no.',
                     'My sources say no.',
                     'The overlords forbid it.',
                     "I'd think long and hard about that one, chief.",
                     'Doubt.']
        await ctx.send(f'Question: {question}\nThe Almighty Conch: {random.choice(responses)}')


def setup(client):
    client.add_cog(Fun(client))
