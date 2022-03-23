import discord
import random
import aiocron

# Init Stuff
TOKEN = open('token.txt').readline()
client = discord.Client()
CHANNEL = 954114697060298782


# Send Message
@aiocron.crontab('52 0 * * *')
async def quote():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL)
    print("Sending message....")
    await channel.send(random.choice(open('quotes.txt').readlines()))
    return

# Events
@client.event
async def on_ready():
    print('bot online')


@client.event
async def on_message(message):
    usermsg = str(message.content)
    if message.author == client.user:
        return

    if message.channel.name == 'general':
        if usermsg.lower() == 'ayo':
            await message.channel.send('whats up cocksukka')
            return


# Run Bot
client.run(TOKEN)


