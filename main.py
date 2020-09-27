import discord
from discord.ext import commands
import heartBot
import os

client = commands.Bot(command_prefix = ".")

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

client.run(heartBot.token)

