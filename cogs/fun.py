# Import modules
import discord
import random

from aiohttp import request
from discord import Embed
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

    # Compliment command :)
    @commands.command(brief="Give your friends a nice compliment")
    async def compliment(self, ctx, member: discord.Member):
        compliments = ['you smell nice today!',
                       'how do you get your hair so silky?',
                       'you have the prettiest eyes!',
                       'you really brighten up the room :)',
                       'the person who sent this loves you!',
                       'you are a really great friend.',
                       'you are loved by your friends and family.',
                       'your smile is contagious!',
                       "you're like sunshine on a rainy day.",
                       'being around oyu is like a happy little vacation.',
                       'you inspire me to be a better bot.',
                       'you are a gift to those around you!'
                       "you're all that and a family-sized bag of chips!",
                       "on a scale from 1-10, you're an 11!"]
        await ctx.send(f'{member.mention}, {random.choice(compliments)}')

    # Insult command
    @commands.command(brief="Insult the mentioned user!")
    async def insult(self, ctx, member: discord.Member):
        insults = ['being around you honestly makes me want to throw up.',
                   "I'm gonna beat the goofy out of you.",
                   'your gene pool could use a little chlorine.',
                   'if you were any more inbred, you would be a sandwich.',
                   'I would slap you, but it would be considered animal abuse.',
                   "I'm trying to see things from your point of view but I can't stick my head that far up my own ass.",
                   "don't be ashamed of who you are, that's your parents job.",
                   'your ass should be jealous of all of the shit coming out of your mouth.',
                   "your only chance of getting laid is to climb up a chicken's ass and wait.",
                   "you're dumber than snake mittens!",
                   "I'll never forget the first time we met, but I'll keep trying.",
                   "your teeth are so jacked up you could eat an apple through a fence."]
        await ctx.send(f'{member.mention}, {random.choice(insults)}')

    # Animal fact command
    @commands.command(brief="Display an animal fact")
    async def animalfact(self, ctx, animal: str):
        if (animal := animal.lower()) in ("dog", "cat", "panda", "fox", "bird", "koala"):
            fact_url = f"https://some-random-api.ml/facts/{animal}"
            image_url = f"https://some-random-api.ml/img/{'birb' if animal == 'bird' else animal}"

            async with request("GET", image_url, headers={}) as response:
                if response.status == 200:
                    data = await response.json()
                    image_link = data["link"]

                else:
                    image_link = None

            async with request("GET", fact_url, headers={}) as response:
                if response.status == 200:
                    data = await response.json()

                    embed = Embed(
                        title=f"{animal.title()} Fact:",
                        description=data["fact"],
                        colour=ctx.author.colour)
                    if image_link is not None:
                        embed.set_image(url=image_link)

                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"API returned a {response.status} status.")
        else:
            await ctx.send("No facts are available for that animal.")

    # Animal fact error
    @animalfact.error
    async def animalfact_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Choose an animal from the following list that you would like a fact about: dog, cat, panda, fox, bird, or koala")


def setup(client):
    client.add_cog(Fun(client))
