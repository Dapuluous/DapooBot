import discord
from discord.ext import commands
import random
from itertools import accumulate

class Misc(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def ping(self, ctx):
		await ctx.send(f'Pong!')

def setup(client):
	client.add_cog(Misc(client))