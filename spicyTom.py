import discord
import os
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!spicy'):
        await message.channel.send('https://imgur.com/Ob2CHLe')
        await message.channel.send('Thats a spicy Tom!')

@client.event
async def on_reaction_add(reaction, user):
	channel = reaction.message.channel
	if raction.emoji == ':hot_pepper:'
		await client.send_message(channel, 'https://imgur.com/Ob2CHLe')
		await client.send_message(channel, 'Thats a spicy Tom!')

client.run(os.environ['DISCORD_TOKEN'])