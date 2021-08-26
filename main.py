import os
import discord
from discord.ext import commands
from eiko import EikoBot
from decouple import config

if __name__ == "__main__":
    bot = EikoBot()

    for name in os.listdir("./cogs"):
        if name.endswith(".py"):
            bot.load_extension("cogs.{}".format(name[:-3]))

        bot.run(config('TOKEN'))
