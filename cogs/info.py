from io import BytesIO
import json
import os
import platform
import random
import sys
from PIL import Image, ImageChops, ImageDraw, ImageFont
import aiohttp
import discord
from discord.ext import commands

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)


class info(commands.Cog, name="info"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, context):
        """
        Check the bot's latency.
        """
        await context.reply(f"Pong! {round(self.bot.latency * 1000)}ms")
def setup(bot):
    bot.add_cog(info(bot))