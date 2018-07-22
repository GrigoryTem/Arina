import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import time


Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = "?") #Initialise client bot

greetings = ["hey", "hi", "hello"]

@client.event 
async def on_ready():
    print("Bot is online and connected to Discord") #This will be called when the bot connects to the server

@client.event
async def on_message(message):
    for word in greetings:
    if message.content == word:
        await client.send_message(message.channel, "mafia - I can choose victim\nmaniac - hm what is victim?")
    if message.content == "mafia":
        await client.send_message(message.channel, "I dont care")
    if "Voting" in message.content:
        await client.send_message(message.channel, random.choice(["Akbar", "Fox", "Marcus", "Grigory"]))

client.run("NDY2NjM0MDMyNzIyMjE0OTEy.DjY7qg.I8aZaPUR1CXBePQWiuEjJtgPb5U") #Replace token with your bots token
