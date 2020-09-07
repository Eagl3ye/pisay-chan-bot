import discord
from discord.ext import commands
import os

class Tools(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(name="university", aliases=['univ', 'uni', 'u'])
	@commands.has_guild_permissions(administrator=True)
	async def university(self, ctx):
		msg = ctx.message
		description = '► Assign yourself a role by reacting to the specified emoji based on your campus.\n\n'
		reacts = [
			':airplane:',':construction_site:',':evergreen_tree:',
			':microscope:',':robot:',':tiger2:',
			':bow_and_arrow:',':eagle:',':sunflower:'  
		]
		roles = [
			'International','MSU','CMU',
			'WVSU','Mapua','UST',
			'DLSU','ADMU','UP'
		]
		embed = discord.Embed(
			title=':information_source: **ROLE MENU: Campus** :information_source:\n',
			description=description,
			colour=discord.Colour.from_rgb(0, 160, 220)
			)
		for react, role in zip(reacts, roles):
			embed.add_field(name=react+' **'+role+'**', value='\u200b', inline=True)
		
		await ctx.send(embed=embed)
		await msg.delete()

	@commands.command(name="embed")
	@commands.has_guild_permissions(administrator=True)
	async def embed(self, ctx, color_r=0, color_g=0, color_b=0, *, content:str):
		msg = ctx.message
		content = content.split("|")
		embed = discord.Embed(
			title=(content[0]).strip(),
			description=(content[1]).strip(),
			colour=discord.Colour.from_rgb(color_r, color_g, color_b)
			)
		await ctx.send(embed=embed)
		await msg.delete()
'''
	@commands.command(name="setagree", aliases=['agreezone', 'uni', 'u'])
	@commands.has_guild_permissions(administrator=True)
	async def setagree(self, ctx, color_r=0, color_g=0, color_b=0, *, content:str):
		msg = ctx.message
		content = content.split("|")
		title = (content[0]).strip()
		embed = discord.Embed(
			title=(content[0]).strip(),
			description=(content[1]).strip(),
			colour=discord.Colour.from_rgb(color_r, color_g, color_b)
			)
		await ctx.send(embed=embed)
		await msg.delete()

	def compareChannelID(self, channelid):
		ret_value = False
		if int(os.environ['AGREEMENT_CHID']) == 0:
			print("Command: Aggreement | AGREEMENT_CHID is empty")
			ret_value = False
		else:
			ret_value = channelid == os.environ['AGREEMENT_CHID']
			print("Command: Aggreement | AGREEMENT_CHID and the target channel is " + str(ret_value))
		return ret_value

	@commands.Cog.listener()
	async def on_message(self, message):
		msg = message
		if (message.content).lower() in ["i accept","accept"] and self.compareChannelID(message.channel.id):
			print("ACCEPTED!")
			print(message.content)
		await msg.delete()

'''
def setup(client):
	client.add_cog(Tools(client))
