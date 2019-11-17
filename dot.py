import discord
from googlesearch import search
# bot.py
token ="NjQ0NzgxMDk2OTMxNjg4NDY4.XdDTMg.mVMwsLzamQzq3J0hRVn6hBHB3AQ"
guild="Cloudbot"

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'hi':
        await message.channel.send("hey")

    if "!google" in message.content:
        parts=message.content.split(" ")
        query=' '.join(parts[1:])
        print(query)
        with open("storage.txt","a") as f:
            msg=query+"\n"
            print(msg)
            f.write(msg)
        for j in search(query, tld="co.in", num=10, start=0,stop=5, pause=2):
            # print(j)
            await message.channel.send(j)

    if "!recent" in message.content:
        recentsplit=message.content.split(" ")
        recentparts=' '.join(recentsplit[1:])
        with open ("storage.txt","r") as f:
            for line in f:
                if recentparts in line:
                    await message.channel.send(line)

client.run(token)