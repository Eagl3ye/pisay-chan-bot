import discord
from discord.ext import commands
import os
import random
import asyncio

client = commands.Bot(command_prefix = 'p+')
@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.idle, activity=discord.Game("with all the Iskolar ng Bayan"))
	print('Logged on as')
	print(client.user.name)
	print(client.user.id)

client.load_extension("cogs.tools")
client.run(os.environ['TOKEN'])