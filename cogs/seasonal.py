import discord
from discord.ext import commands
import os
import random

class Seasonal(commands.Cog):
	def __init__(self, client):
		self.client = client
		self.allowed_guilds = [402259476515913728]
		self.ignored_channels = []
		self.datamap = {}
		#691929067251040326 2021 Batch Server
		#402259476515913728 Casino
		#758561233715593256 La Casa de Jowny 
	
	def checkCache(self):
		try:
			with open("../cache/cache_spooktober.data",'r') as f:
				try:	
					print(f.readlines()[0])
				except IndexError:
					pass
		except FileNotFoundError:
			with open("../cache/cache_spooktober.data",'w') as f:
				f.write("")

	def saveCache(self):
		self.checkCache()
		with open("../cache/cache_spooktober.data",'w') as f:
			f.write(str(self.datamap))

	def getCache(self):
		self.checkCache()
		try:
			with open("../cache/cache_spooktober.data",'r') as f:
				try:
					self.datamap = ast.literal_eval(f.readlines()[0])
					print(self.datamap)
				except IndexError:
					pass
		except FileNotFoundError:
			pass
			
	@commands.command(name="ignore")
	@commands.has_guild_permissions(administrator=True)	
	async def ignore(self, ctx):
		print(self.ignored_channels) ###################################
		if ctx.channel.id not in self.ignored_channels:
			self.ignored_channels.append(ctx.channel.id) 
			embed = discord.Embed(
				title=":jack_o_lantern: Seasonal Sppoktober Event :jack_o_lantern:",
				description=":no_entry: | Trick or treating is not allowed on this channel",
				colour=discord.Colour.from_rgb(230, 135, 0)
			)
		else:
			embed = discord.Embed(
				title=":jack_o_lantern: Seasonal Sppoktober Event :jack_o_lantern:",
				description=":no_entry: | Trick or treating is already not allowed on this channel",
				colour=discord.Colour.from_rgb(230, 135, 0)
			)
		embed.set_footer(text=ctx.channel.name)	
		print(self.ignored_channels) ###################################
		await ctx.send(embed=embed)

	@commands.command(name="unignore")
	@commands.has_guild_permissions(administrator=True)	
	async def unignore(self, ctx):
		print(self.ignored_channels) ###################################
		if ctx.channel.id in self.ignored_channels:
			self.ignored_channels.pop(ctx.channel.id) 
			embed = discord.Embed(
				title=":jack_o_lantern: Seasonal Sppoktober Event :jack_o_lantern:",
				description=":white_check_mark: | Trick or treating is now allowed on this channel",
				colour=discord.Colour.from_rgb(230, 135, 0)
			)
		else:
			embed = discord.Embed(
				title=":jack_o_lantern: Seasonal Sppoktober Event :jack_o_lantern:",
				description=":white_check_mark: | Trick or treating is already allowed on this channel",
				colour=discord.Colour.from_rgb(230, 135, 0)
			)
		embed.set_footer(text=ctx.channel.name)
		await ctx.send(embed=embed)
		print(self.ignored_channels) ###################################

	@commands.command(name="activate")
	@commands.has_guild_permissions(administrator=True)	
	async def activate(self, ctx):
		print(self.allowed_guilds) ###################################
		if ctx.guild.id not in self.allowed_guilds:
			self.allowed_guilds.append(ctx.guild.id) 
			embed = discord.Embed(
				title=":jack_o_lantern: Seasonal Sppoktober Event :jack_o_lantern:",
				description="This event is now activated on this guild",
				colour=discord.Colour.from_rgb(230, 135, 0)
			)
		else:
			embed = discord.Embed(
				title=":jack_o_lantern: Seasonal Sppoktober Event :jack_o_lantern:",
				description="This event is already activated on this guild",
				colour=discord.Colour.from_rgb(230, 135, 0)
			)
		embed.set_footer(text=ctx.channel.name)	
		print(self.allowed_guilds) ###################################
		await ctx.send(embed=embed)

	@commands.command(name="mycandy")	
	async def mycandy(self, ctx):
		self.getCache()
		if str(message.author.id) in self.datamap.keys():
			embed = discord.Embed(
				title=":jack_o_lantern: Seasonal Sppoktober Event :jack_o_lantern:",
				description="{}:\n :candy: **Candy**: {} ".format(ctx.author.name, self.datamap[str(message.author.id)]),
				colour=discord.Colour.from_rgb(230, 135, 0)
			)
		else:
			embed = discord.Embed(
				title=":jack_o_lantern: Seasonal Sppoktober Event :jack_o_lantern:",
				description="{}:\n :candy: **Candy**: {} ".format(ctx.author.name, 0),
				colour=discord.Colour.from_rgb(230, 135, 0)
			)
		self.saveCache()
		embed.set_footer(text="Valid until November 1, 2020")
		await ctx.send(embed=embed)

	@commands.Cog.listener()
	async def on_message(self, message):
		msg = message
		if message.guild.id in self.allowed_guilds and message.channel.id not in self.ignored_channels:
			print(message.guild.name,":")
			if random.randrange(0, 3) == 3:
				embed = discord.Embed(
					title=":jack_o_lantern: Seasonal Sppoktober Event :jack_o_lantern:",
					description="Here's a special treat for you:",
					colour=discord.Colour.from_rgb(230, 135, 0)
				)
				candy = random.randrange(1, 3)
				embed.add_field(name=':candy: ~-~> {}x Candy <~-~ :candy:'.format(candy), value="\u200b", inline=False)
				embed.add_field(name='- Collect as many as you can', value="\u200b", inline=False)
				embed.add_field(name='- Exchange it later for some goods', value="\u200b", inline=False)
				embed.add_field(name='- Do `mycandy` to see your candies', value="\u200b", inline=False)
				embed.set_footer(text="Valid until November 1, 2020")
				self.getCache()
				if str(message.author.id) in self.datamap.keys():
					self.datamap[str(message.author.id)] += candy
				else:
					self.datamap[str(message.author.id)] = candy
				self.saveCache()
				await ctx.send(embed=embed)

def setup(client):
	client.add_cog(Seasonal(client))