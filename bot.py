# Import commands and libraries
import discord
import random
import json
from discord.ext import commands, tasks
from itertools import cycle

# Allows user to change prefix for the bot


def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]


# Create instance of the discord bot and assign to client variable
client = commands.Bot(command_prefix=get_prefix)

# Create list of statuses for bot status changer to use
status = cycle(['Back to work!', 'No goofing off >:(',
                'Noah smells good :)', 'Hi mom!', 'Conference room in 10', 'with the API', '.help'])

# GIFs for 'gamer night' commands
my_files = [
    discord.File('gifs/wheelchair1.gif'),
    discord.File('gifs/wheelchair2.gif'),
    discord.File('gifs/wheelchair3.gif')
]

###### EVENTS ######

# Make sure the bot is online and set custom status


@client.event
async def on_ready():
    print('**********')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('**********')
    change_status.start()

# Makes . default value for bot command prefix by manipulating json file


@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '.'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

# Member join message


@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send(f"""The temp is here! Toby, get {member.mention} started on the new hire paperwork!""")

# Member leave message


@client.event
async def on_member_remove(member):
    for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send(f"""Rest assured, {member.mention} won't be getting any severance pay. See ya!""")

# Bot responds to certain keywords


@client.event
async def on_message(message):
    if client.user.id != message.author.id:
        if 'whomst' in message.content:
            await message.channel.send("It's gamer night boyos, all hands on deck! @here")
            await message.channel.send(files=my_files)

    await client.process_commands(message)


###### TASKS ######


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

###### COMMANDS ######

# Change command prefix


@client.command()
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefix changed to: {prefix}')

# Kick command


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}. Get him outta here!')

# Ban command


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}.')

# Clear command


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
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

###### ERRORS ######

# Bot error message


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Beep boop. Command not found!")

# Clear command error prompt


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify an amount of messages to delete.')

# Running bot using bot token from Discord
client.run('NzQyNzY3NTY5MDUxNTgyNTU0.XzK6NA.sMey640nLORFfQzo_MScrC6s4oU')
