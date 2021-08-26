import discord
from discord.ext import commands


class EikoBot(commands.Bot):
    def __init__(self, **options):
        super().__init__(
                command_prefix="!!", 
                help_command=None,
                description="Eiko Discord bot",
                 **options)
