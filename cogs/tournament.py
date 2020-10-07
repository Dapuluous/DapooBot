import discord
from discord.ext import commands
import random
from itertools import accumulate

class Tournament(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def group(self, ctx, *, initialInput = None):
		if initialInput:
			groupArray = initialInput.split(", ")

			def check(m):
				return m.author == ctx.author

			for i in range(1, 2):
				await ctx.send(f"Please input team size!")
				msg = await self.client.wait_for('message', check=check)
				lengthSplit = msg.content.split(", ")

				try:
					# Turn lengthsplit array from str to int
					for i in range(0, len(lengthSplit)): 
						lengthSplit[i] = int(lengthSplit[i])

					totalSize = sum(lengthSplit)
					
					# print(totalSize)
					# print(len(groupArray))

					if(totalSize == len(groupArray)):
						# Randomizing groupArray's array
						inputRandomized = random.sample(groupArray, len(groupArray))

						# Splitting randomized groupArray's array based on lengthSplit
						finalizedRandom = [inputRandomized[x - y: x] for x, y in zip(accumulate(lengthSplit), lengthSplit)]

						# Print Team
						for x in range(0, len(lengthSplit)):
							teamArray = []
							await ctx.send(f'Group {x+1}')

							for y in range(0, lengthSplit[x]):
								teamArray.append(finalizedRandom[x][y])

							await ctx.send(f"```{', '.join(map(str, teamArray))}```")
					elif(totalSize > len(groupArray)):
						await ctx.send(f"Your group size is exceeding the number of available members! Total group size: **{totalSize}** | Actual group size: **{len(groupArray)}**")
					else:
						await ctx.send(f"Your group size is not equal to the number of available members! Total group size: **{totalSize}** | Actual group size: **{len(groupArray)}**")
				except:
					await ctx.send(f"Unknown input. Example correct input: `3, 3, 2, 2` (separated by `, `)")
		else:
			await ctx.send(f"No input detected.")

def setup(client):
	client.add_cog(Tournament(client))