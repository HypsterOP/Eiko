import os
import discord
from discord.ext import commands
from eiko import EikoBot
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    bot = EikoBot()

    for name in os.listdir("./cogs"):
        if name.endswith(".py"):
            bot.load_extension("cogs.{}".format(name[:-3]))

        bot.run(os.environ.get('TOKEN'))
