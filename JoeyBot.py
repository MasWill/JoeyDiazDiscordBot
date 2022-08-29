import discord
import random
import aiocron

# Init Stuff
TOKEN = open('token.txt').readline()
client = discord.Client()
CHANNEL = 123456789 # Enter channel ID of channel you want coco quotes to appear (123456789) is not 
                    # a legit channel id


# Send Message
# cron format:  (min hr day month year day-of-week)
@aiocron.crontab('52 0 * * *') # edit these crom tab parameters to set time quotes get sent
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
            await message.channel.send('whats up')
            return


# Run Bot
client.run(TOKEN)


