import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/spicy'):
        await message.channel.send('https://imgur.com/Ob2CHLe')
        await message.channel.send('Thats a spicy Tom!')
        

client.run('NzIyODcxNjYyMDY4MTA1MzE2.XupZxg.dzJbRkc7TuKsDmM64r6j2kOzRJw')