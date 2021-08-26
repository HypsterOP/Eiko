import os
import discord
from discord.ext import commands
from eiko import EikoBot
from dotenv import load_dotenv
import asyncpg
from asyncpg.pool import create_pool
load_dotenv()

if __name__ == "__main__":
    bot = EikoBot()

    async def create_db_pool():
        bot.pg_con = await asyncpg.create_pool(database="Eiko", user="postgres",password=os.environ.get('DB_PASS'))

    for name in os.listdir("./cogs"):
        if name.endswith(".py"):
            bot.load_extension("cogs.{}".format(name[:-3]))

        bot.loop.run_until_complete(create_db_pool())
        bot.run(os.environ.get('TOKEN'))
