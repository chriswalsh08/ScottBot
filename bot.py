# ScottBot
# Author: Christopher James Walsh
# Created in August 2020 to spice up my friends' Discord server with funny games, a music player,
# and some moderation commands.

# Import modules
import discord
import os
import random
import json
from aiohttp import request
from discord import Embed
from discord.ext import commands, tasks
from itertools import cycle

# Allows user to change prefix for the bot


def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]


# Create instance of the discord bot and assign to client variable
description = "Chatbot with some fun social, pre-programmed response, and moderation commands."
client = commands.Bot(command_prefix=get_prefix, description=description)

# Create list of statuses for bot status changer to use
status = cycle(['Back to work!', 'No goofing off >:(',
                'Noah smells good :)', 'Hi mom!', 'Conference room in 10', 'with the API', '.help'])

# GIFs for 'gamer night' event listener
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

# Bot sends quirky responses to certain keywords/phrases


@client.event
async def on_message(message):
    if client.user.id != message.author.id:
        if 'whomst' in message.content.lower():
            await message.channel.send("It's gamer night boyos, all hands on deck! @here")
            await message.channel.send(files=my_files)
        elif 'bye' in message.content.lower():
            await message.channel.send(file=discord.File('gifs/goodbye.gif'))
        elif 'bot sucks' in message.content.lower():
            await message.channel.send("no u")
            await message.channel.send(file=discord.File('gifs/sad_mike.gif'))
        elif 'no u' in message.content.lower():
            await message.channel.send("no u")

    await client.process_commands(message)

###### TASKS ######


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

###### COMMANDS ######

# Load and Unload commands for loading and unloading cogs


@client.command(hidden=True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command(hidden=True)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

# Custom help command


@client.command(hidden=True, brief="Displays the help dash")
async def help(ctx):
    embed = Embed(
        title="Help Commands",
        description="A categorized list of Scottbot's commands!"
        colour=ctx.author.colour
    )
    embed.set_thumbnail(
        url="https://media2.giphy.com/media/55SfA4BxofRBe/giphy.gif?cid=ecf05e47n74f220gey16m63wccnqu5kcjw7eulr6z4n8c0l3&rid=giphy.gif")
    embed.add_field(name="")

# Change command prefix


@client.command(brief="Change ScottBot's command prefix")
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefix changed to: {prefix}')

# Clear command


@client.command(brief="Clears messages in current channel")
@commands.has_permissions(manage_messages=True)
@commands.cooldown(3, 10, commands.BucketType.user)
async def clear(ctx, amount: int):
    amount += 1
    if amount > 11:
        await ctx.send("Nice try bucko, you can't delete over 10 messages at once!")
    else:
        await ctx.channel.purge(limit=amount)

# Check bot's ping (in milliseconds!)


@client.command(brief="Displays ScottBot's ping in milliseconds")
async def ping(ctx):
    embed = Embed(
        title=f"Pong!",
        description=f"My ping is {round(client.latency * 1000)}ms!",
        colour=ctx.author.colour)

    await ctx.send(embed=embed)


###### ERRORS ######

# Bot command error message


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = Embed(
            title=f"Oops!",
            description=f"Command not found! Type .help if you need the list of my commands!",
            colour=ctx.author.colour)
        await ctx.send(embed=embed)

# Clear command error message


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify an amount of messages to delete.')

# Import cogs

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# Run bot using bot token from Discord
client.run('NzQyNzY3NTY5MDUxNTgyNTU0.XzK6NA.2ul0mi5bkjGe6TdYbuHtJY7ah5I')
