import discord
from discord.ext import commands
import os
import random
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
load_dotenv()

client = discord.Client(intents=intents)
token = os.getenv('TOKEN')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# client = commands.Client(command_prefix="!")

@client.event
async def on_ready():
    print(f'{client.user} is online!')
    
    
    
client.run(TOKEN)