import discord
from discord.ext import commands
import random
from itertools import accumulate
import random

class Misc(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def ping(self, ctx):
		await ctx.send(f'Pong! ({round(self.client.latency * 1000)} ms)')

	@commands.command()
	async def randomizeGroup(self, ctx, *, initialInput):
		groupArray = initialInput.split(",")

		lengthSplit = [3, 3, 2, 2]

		InputRandomized = random.sample(groupArray, len(groupArray))

		FinalizedRandom = [InputRandomized[x - y: x] for x, y in zip( 
          accumulate(lengthSplit), lengthSplit)]

		for x in range(0, 4):
			teamArray = []
			await ctx.send(f'Group {x+1}')

			if(lengthSplit[x] == 2):
				for y in range(0, 2):
					teamArray.append(FinalizedRandom[x][y])
			else:
				for y in range(0, 3):
					teamArray.append(FinalizedRandom[x][y])

			await ctx.send(f"```{', '.join(map(str, teamArray))}```")

		# await ctx.send(f'Input Example: {Output}')
	# 	if (len(inputku) == 0):
	# 	await ctx.send("Tidak ada input terdaftar")
	# else:
	# 	iniArray = inputku.split(",")
	# 	InputRandomized = random.sample(iniArray, len(iniArray))

	# 	await ctx.send(f'Inputku: {InputRandomized}')

def setup(client):
	client.add_cog(Misc(client))