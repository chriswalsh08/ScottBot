# Import commands and libraries
import discord
import random
from discord.ext import commands

# Create instance of the discord bot and assign to client variable
client = commands.Bot(command_prefix='.')

###### EVENTS ######

# Make sure the bot is online


@client.event
async def on_ready():
    print('**********')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('**********')

# Member join message


@client.event
async def on_member_join(member):
    await print(f'{member} has joined the team!')

# Member leave message


@client.event
async def on_member_remove(member):
    await print(f'{member} walked out on us! We need another accountant!')

###### COMMANDS ######

# Kick command


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}. Get him outta here!')

# Ban command


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}.')

# Clear command


@client.command()
async def clear(ctx, amount=5):
    amount += 1
    await ctx.channel.purge(limit=amount)

# Check bot's ping


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! My ping is {round(client.latency * 1000)}ms!')

# Magic 8-ball


@client.command(aliases=['conch', '8ball', 'eightball'])
async def almightyconch(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt!',
                 'Yes, definitely!',
                 'As I see it, yes.',
                 'Of course!',
                 'Signs point to yes.',
                 'Reply hazy... try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict that now.',
                 'Concentrate and ask again.',
                 'You smell, go away!',
                 "Don't count on it.",
                 'My reply is no.',
                 'My sources say no.',
                 'The overlords forbid it.',
                 "I'd think long and hard about that one, chief.",
                 'Doubt.']
    await ctx.send(f'Question: {question}\nThe Almighty Conch: {random.choice(responses)}')

# Running bot using bot token from Discord
client.run('NzQyNzY3NTY5MDUxNTgyNTU0.XzK6NA.Hb2z-Cahu6auHcX6s5jI9saoAjY')
