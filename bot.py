import discord
from discord.ext import commands


client = commands.Bot(command_prefix = 's.')

@client.event
async def on_ready():
    print("Bot is ready to be used")


