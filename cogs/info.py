import discord 
from discord.ext import commands 

class Info(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready():
        print("Ready Eiko")

    @commands.command(aliases= 'p')
    async def ping(self, ctx):
        await ctx.reply(f"Pong! {round(self.bot.latency * 1000)}ms")