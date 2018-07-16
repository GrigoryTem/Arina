import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = "?") #Initialise client bot

chat_filter = ["PINEAPPLE", "APPLE", "CHROME"]

@client.event 
async def on_ready():
    print("Bot is online and connected to Discord") #This will be called when the bot connects to the server

@client.event
async def on_message(message):
   contents = message.content.split(" ") #contents is a list type
    for word in contents:
        if word.upper() in chat_filter:
            await client.send_message(message.channel, "**Hey!** You're not allowed to use that word here!")

client.run("NDY3NzM0MTc0NjI4MDUzMDI2.Di3fdg.O_hg2m8pEdY5w87L-B6QdN__gDQ") #Replace token with your bots token
