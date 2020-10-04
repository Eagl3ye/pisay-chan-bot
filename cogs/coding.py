import discord
from discord.ext import commands
import os

class Coding(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_message(self, message):
		msg = message
		if message.channel.id == 762322266116980786 and (message.content[0:4] == "```py" or message.content[0:8] == "```python"):
			print("<#762322266116980786>:")
			print(message.content)
		#await msg.delete()

def setup(client):
	client.add_cog(Coding(client))
