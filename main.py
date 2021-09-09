import discord
import random
TOKEN = ''
phrases = {
    1 : 'phrase 1',
    2 : 'phrase 2',
    3 : 'phrase 3'
}
def phrases_count():
    cnt = 0
    for name in phrases.keys():
        cnt+=1
    return cnt
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await message.channel.send(phrases.get(random.randint(1,phrases_count())))
        
client.run(TOKEN)