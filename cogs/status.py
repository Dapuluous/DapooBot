import discord
from discord.ext import commands

class Welcome(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		await self.client.change_presence(activity=discord.Game('With Imaginary Girlfriend'))
		print("Welcome To DapooBot!")
		print("--------------------")

	@commands.command()
	@commands.is_owner()
	async def shutdown(self, ctx):
		await ctx.send("Thank you for using me!")
		await ctx.bot.logout()

def setup(client):
	client.add_cog(Welcome(client))