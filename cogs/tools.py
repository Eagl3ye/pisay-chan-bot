import discord
from discord.ext import commands

class Tools(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_message(self, message):
		print(message.content)

	@commands.command(name="university",aliases=['univ', 'uni', 'u'])
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
	async def embed(ctx, color_r=0, color_g=0, color_b=0, *, content:str):
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

def setup(client):
	client.add_cog(Tools(client))