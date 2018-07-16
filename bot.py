import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = "?") #Initialise client bot

@client.event 
async def on_ready():
    print("Bot is online and connected to Discord") #This will be called when the bot connects to the server

@client.event
async def on_message(message):
    if message.content.upper().startswith('arina'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> , I am not mafia maybe YOU!" % (userID))

client.run("NDY3NzM0MTc0NjI4MDUzMDI2.Di3fdg.O_hg2m8pEdY5w87L-B6QdN__gDQ") #Replace token with your bots token
