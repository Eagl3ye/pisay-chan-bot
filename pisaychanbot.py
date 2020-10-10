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

cogs = ["cogs.tools","cogs.coding","cogs.seasonal"]
for cog in cogs:
	client.load_extension(cog)
client.run(os.environ['TOKEN'])