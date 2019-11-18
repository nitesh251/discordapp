import discord
from googlesearch import search
import pymongo

token ="NjQ0NzgxMDk2OTMxNjg4NDY4.XdGX7w.9o6MiGYI6Lf_JFZPSg7G7HFmIww"
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

#===============================Google Search=============================================================
    if "!google" in message.content:
        parts=message.content.split(" ")
        query=' '.join(parts[1:])
        print(query)
#------------------------------------------------------------------------------------------------------------
        #with open("storage.txt","a") as f:
            #msg=query+"\n"
            #print(msg)
            #f.write(msg)
#------------------------------------------------------------------------------------------------------------
        myclient = pymongo.MongoClient('mongodb://localhost:27017/')
        mydb = myclient['mydatabase']
        mycol = mydb["discordstorage"]

        mydict = {"search_string": query}

        x = mycol.insert_one(mydict)

        for j in search(query, tld="co.in", num=10, start=0,stop=5, pause=2):
            await message.channel.send(j)


#=================================Recent History========================================================
    if "!recent" in message.content:
        recentsplit=message.content.split(" ")
        recentparts=' '.join(recentsplit[1:])
        
#-----------------------------------------------------------------------------------------------------
	#with open ("storage.txt","r") as f:
            #for line in f:
                #if recentparts in line:
                    #await message.channel.send(line)
#-----------------------------------------------------------------------------------------------------
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb["discordstorage"]

        myquery = {"search_string": recentparts}
        mydoc = mycol.find(myquery)
        for x in mydoc:
            print(x["search_string"])
            await message.channel.send(x["search_string"])



client.run(token)