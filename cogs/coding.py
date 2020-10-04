import discord
from discord.ext import commands
import os

class Coding(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_message(self, message):
		msg = message
		print(message)
		#if (message.content).lower() in ["i accept","accept"] and self.compareChannelID(message.channel.id):
		#	print("ACCEPTED!")
		#	print(message.content)
		#await msg.delete()

def setup(client):
	client.add_cog(Coding(client))
