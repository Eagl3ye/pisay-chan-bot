import discord
from discord.ext import commands
import os
import random
import asyncio

def mudae_randomize():
	container = [("a"*1),("b"*9),("c"*12),("d"*11),("e"*10),("f"*9),("g"*9),("h"*6),("i"*18),("j"*7),("k"*8)]
	string = ""
	while(len(container)>0):
		string += container.pop(random.randint(0,len(container)-1))
	string = list(string)
	return string.pop(random.randint(0,99))

#def mudae_release():
#	letters = ['a','b','c','d','e','f','g','h','i','j','k']
#	return letters[random.randint(0,len(container)-1)]

mudae_events_list = {
		"a":["UNLUCKY EVENT","Server-wide Thanos Snap"],											# 1%
		"b":["UNLUCKY EVENT","Force-divorce all firstmarries"],										# 9%
		"c":["UNLUCKY EVENT","Limit your harem to 50 for a week"],									# 12%
		#"Force-divorce the highest-kakera character"],										# 6%
		"d":["UNLUCKY EVENT","Force-divorce 2 random characters (500-ka below)"],					# 11%
		"e":["NEUTRAL EVENT","Send any character to someone (Must be 250-ka above)"], 				# 10%
		"f":["UNLUCKY EVENT","Pay 2000 kakera"],													# 9%
		"g":["UNLUCKY EVENT","Thanos Snap (2 random players)"],										# 9%
		"h":["LUCKY EVENT","Earn 1x Trading Power (Random player)"],								# 6%
		"i":["LUCKY EVENT","Earn 200 kakera"],														# 18% 
		"j":["LUCKY EVENT","Earn 1x Two lock-in rights during Thanos/Reset (3 random players)"],	# 7%	
		#"Earn 100 daily kakera for 7 days (Random player)"],								# 18%
		"k":["LUCKY EVENT","Next event immunity (random player)"]									# 8%
	}
		#BURN THE FIRST THING YOU ROLL
		#

client = commands.Bot(command_prefix = 'r!')

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.dnd, activity=discord.Game("with the Events | r!help"))
	print('Logged on as')
	print(client.user.name)
	print(client.user.id)

@client.command()
async def mudae_event(ctx, mode=None, number=1):
	msg = ctx.message
	if mode is None or mode == "spawn":
		embed = discord.Embed(
			title=':heart_exclamation: **Mudae Event** :heart_exclamation:',
			colour=discord.Colour.red()
			)
		if number > 4:
			number = 4
		if number < 1:
			number = 1
		for _ in range(number):
			choice = mudae_randomize()
			embed.add_field(name='📍| '+mudae_events_list[choice][0], value=mudae_events_list[choice][1], inline=False)

		await ctx.send(embed=embed)
	elif mode == "release":
		embed = discord.Embed(
			title=':heart_exclamation: **Mudae Event** :heart_exclamation:',
			description='► The following randomly-picked events will be __**removed**__ for this week\'s mudae event:',
			colour=discord.Colour.from_rgb(255, 230, 230)
			)
		if number > 4:
			number = 4
		if number < 1:
			number = 1
		for _ in range(number):
			choice = mudae_randomize()
			embed.add_field(name=':outbox_tray:| '+mudae_events_list[choice][0], value=mudae_events_list[choice][1], inline=False)
		#letters = ['a','b','c','d','e','f','g','h','i','j','k']
		embed.set_footer(text='New events will be added later... stay tuned!')
		#await ctx.send(content=":heart_exclamation: Attention to all <@&742333248125927425> :heart_exclamation:")
		await ctx.send(embed=embed)
	await msg.delete()

@client.command()
async def arena_event(ctx):
	embed = discord.Embed(
		title=':trophy: **Arena Event** :trophy:',
		description='Hosted by: <@336068309789310979>',
		colour=discord.Colour.gold()
		)
	first = '<@!273035462996918273>\n10,000 Tatsumaki Credits | 10,000 IdleRPG Credits | 1000 kakera'
	second = '<@!487935377219256343>\n5,000 Tatsumaki Credits | 5,000 IdleRPG Credits | 500 kakera'
	third = '<@!523701663937200134>\n1,000 Tatsumaki Credits | 1,000 IdleRPG Credits | 100 Kakera'
	embed.add_field(name='Eligible to:', value='Mudae and IdleRPG players', inline=False)
	embed.add_field(name='Rewards and Winners:', value='-', inline=False)
	embed.add_field(name=':first_place: ', value=first, inline=True)
	embed.add_field(name=':second_place: ', value=second, inline=True)
	embed.add_field(name=':third_place: ', value=third, inline=True)
	embed.add_field(name='Score Tally:', value='https://controlc.com/6b6f4fab', inline=False)
	join = 'Use `$skills` and set the skills for each of your 6 waifus/husbandos to the following divisions:' 
	embed.add_field(name='How to join:', value=join, inline=False)
	embed.add_field(name=':small_orange_diamond:| +10 :crossed_swords: stats', value='Yandere Division', inline=True)
	embed.add_field(name=':small_orange_diamond:| +5 :crossed_swords: +5 :shield: stats', value='Tsundere Division', inline=True)
	embed.add_field(name=':small_orange_diamond:| +10 :shield: stats', value='Kuudere Division', inline=True)
	embed.add_field(name=':small_orange_diamond:| +8 :notebook_with_decorative_cover: stats', value='Dandere Division', inline=True)
	embed.add_field(name=':small_orange_diamond:| +40% :heartpulse: stats', value='Deredere Division', inline=True)
	embed.add_field(name=':small_orange_diamond:| Any stats', value='Combo Division', inline=True)
	
	embed.add_field(name='Where:', value='<#745137728793870366>', inline=True)
	embed.set_footer(text='When: COMPLETED ~~Friday, Aug-28-2020, 9:00 PM Local Time~~')
	await ctx.send(embed=embed)
    #await ctx.send(":heart_exclamation: **Mudae Event** :heart_exclamation: \n```📍 | " + events[randomize()] + "\n```")

@client.command()
async def baog(ctx):
	msg = ctx.message
	await ctx.send(content='<a:baoggif:746755743809667193>')
	await msg.delete()

@client.command()
async def rules(ctx):
	msg = ctx.message
	rules = [
		'**1** ►   Same rules as any righteous groups or servers.',
		'**2** ►   Please be respectful towards everyone. This means __**NO HATE**__ and whatever variant of this rule applies.',
		'**3** ►   No self-promotion without admin permission.',
		'**4** ►   Yeah have fun.'
	]
	flatrules = ''
	for rule in rules:
		flatrules += rule + '\n\n'
	embed = discord.Embed(
		title=':round_pushpin: **SERVER RULES** :round_pushpin:\n',
		description=flatrules,
		colour=discord.Colour.from_rgb(102, 255, 153)
		)
	await ctx.send(embed=embed)
	await msg.delete()

@client.command()
async def campus(ctx):
	msg = ctx.message
	description = '► Assign yourself a role by reacting to the specified emoji based on your campus.\n\n'
	reacts = [
		':white_circle:',':black_circle:',':red_circle:',
		':blue_circle:',':brown_circle:',':purple_circle:',
		':green_circle:',':yellow_circle:',':orange_circle:',
		':white_large_square:',':black_large_square:',':orange_square:',
		':blue_square:',':red_square:',':brown_square:',
		'\u200b',':purple_square:','\u200b'
	]
	roles = [
		'IRC','CLC','EVC',
		'CVisC','CVC','WVC',
		'MRC','MC','CBZRC',
		'ZPRC','CARC','CMC',
		'CRC','SMC','BRC',
		'\u200b','SRC','\u200b'
	]
	embed = discord.Embed(
		title=':round_pushpin: **ROLE MENU: Campus** :round_pushpin:\n',
		description=description,
		colour=discord.Colour.from_rgb(102, 255, 153)
		)
	for react, role in zip(reacts, roles):
		embed.add_field(name=react+' **'+role+'**', value='\u200b', inline=True)
	await ctx.send(embed=embed)
	await msg.delete()

@client.command()
async def treasure(ctx):
	msg = ctx.message
	await ctx.send(content='https://cdn.discordapp.com/emojis/677420843076288522.gif?v=1')
	await msg.delete()

@client.command()
async def announce(ctx, color_r=0, color_g=0, color_b=0, *, content:str):
	msg = ctx.message
	embed = discord.Embed(
		title=':round_pushpin: **ANNOUNCEMENT** :round_pushpin:\n',
		description=content,
		colour=discord.Colour.from_rgb(color_r, color_g, color_b)
		)
	await ctx.send(embed=embed)
	await msg.delete()

@client.command()
async def mudae_announce(ctx, *, content:str):
	msg = ctx.message
	embed = discord.Embed(
		title=':heart_exclamation: **Mudae Event** :heart_exclamation:',
		description=content,
		colour=discord.Colour.red()
		)
	await ctx.send(embed=embed)
	await msg.delete()
client.run(os.environ['TOKEN'])



#await bot.process_commands(message)
'''
 1% - Server-wide Thanos Snap
 6% - Earn 1x Trading Power (Random player)
 7% - Earn 1x Two lock-in rights during Thanos/Reset (3 random players)
 8% - Next event immunity (random player)
 9% - Force-divorce all firstmarries
 9% - Pay 2000 kakera
 9% - Thanos Snap (2 random players)
10% - Send any character to someone (Must be 250-ka above)
11% - Force-divorce 2 random characters (500-ka below)
12% - Limit your harem to 50 for a week
18% - Earn 200 kakera
'''