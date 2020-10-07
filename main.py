import discord
from discord.ext import commands
import heartBot
import os

client = commands.Bot(command_prefix = ".")
client.remove_command("help")

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game('With Imaginary Girlfriend'))
	print("Welcome To DapooBot!")
	print("--------------------")

@client.command()
@commands.is_owner()
async def sh(ctx):
	await ctx.send("Shutting down...")
	await ctx.bot.logout()

@client.command(pass_context = True)
async def help(ctx, *, helpCategory = None):
	if helpCategory:
		if(helpCategory.lower() == "misc"):
			embed = discord.Embed(
				title = "Miscellaneous",
				colour = discord.Colour.blue()
			)

			embed.add_field(name = ".ping", value = "Returns pong!", inline = False)
			await ctx.send(embed = embed)
		elif(helpCategory.lower() == "tournament"):
			embed = discord.Embed(
				title = "Tournament",
				colour = discord.Colour.blue()
			)

			embed.add_field(name = ".group", value = "randomizes the list of members and places them into the groups according to the input", inline = False)
			await ctx.send(embed = embed)
		else:
			await ctx.send(f"{helpCategory} is not found in Help.")
	else:
		embed = discord.Embed(
				colour = discord.Colour.blue()
			)

		embed.add_field(name = "Available help", value = "misc\ntournament", inline = False)
		await ctx.send(embed = embed)

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

client.run(heartBot.token)

