import requests
import json
import discord
from discord.ext import commands

client = discord.Client()
token = # Bot Token
url = "https://ai-chatbot.p.rapidapi.com/chat/free"

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(ctx):
    if (ctx.author.bot):
        print(f"Message is by {ctx.author}")
    else:
        querystring = {"message":ctx.content,"uid":"user1"}
        headers = {
        	"X-RapidAPI-Host": "ai-chatbot.p.rapidapi.com",
	        "X-RapidAPI-Key": # Api Key
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        jayson = json.loads(response.text)
        await ctx.reply(jayson["chatbot"]["response"])

client.run(token) 