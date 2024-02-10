import discord
from discord.ui import Select, View, Button
from discord.ext import commands
from firebase_admin import db
import trade.utils

"""
This cog contains miscellaneous commands not specific to any game.
"""

class MiscCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    """
        Displays current game modes
    """
    @discord.app_commands.command(name="about")
    async def about(self):
        return ""

async def setup(bot):
    await bot.add_cog(MiscCog(bot))