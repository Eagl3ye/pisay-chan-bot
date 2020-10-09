import discord
from discord.ext import commands
import os

class Coding(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_message(self, message):
		msg = message
		if message.channel.id == 762322266116980786:
			print("<#762322266116980786>:")
			codedisc = message.content.split("```")[1].split("\n")
			if codedisc[0] in ['py','python']:
				for codeline in range(1,len(codedisc)-1):
					print(codedisc[codeline]) 
			else:
				for codeline in range(0,len(codedisc)-1):
					print(codedisc[codeline])
		#await msg.delete()

def setup(client):
	client.add_cog(Coding(client))
