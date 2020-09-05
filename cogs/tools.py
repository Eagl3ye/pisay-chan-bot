import discord
from discord.ext import commands

class Tools:
	def __init__(self, client):
		self.client = client

	@commands.command(name="university",alias="uni")
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

def setup(client):
	client.add_cog(Tools(client))