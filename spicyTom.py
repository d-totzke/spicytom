import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	
    if message.author == client.user:
        return
    spicy = '🌶️'
    if message.content.startswith('!spicy'):
        await message.channel.send('https://imgur.com/Ob2CHLe')
        await message.channel.send('Thats a spicy Tom!')

    if message.content == spicy:
        await message.channel.send('https://imgur.com/Ob2CHLe')
        await message.channel.send('Thats a spicy Tom!')

@client.event
async def on_reaction_add(reaction, user):
	channel = reaction.message.channel
	spicy = '🌶️'
	if reaction.emoji == spicy:
		await channel.send('https://imgur.com/Ob2CHLe')
		await channel.send('{} says: Thats a spicy Tom! \nTo: {}'.format(user.mention, reaction.message.content))

client.run(os.environ['DISCORD_TOKEN'])