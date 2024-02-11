import discord
from discord.ext import commands
from misc.misc_views import AboutView
from firebase_admin import db

"""
This cog contains miscellaneous commands not specific to any game.
"""

class MiscCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="about")
    async def about(self, interaction: discord.Interaction):
        await interaction.send_message("hi", view=AboutView(), ephemeral=True)
        # .response("menu", view=AboutView())
        # await interaction.send_message("menu", view=AboutView())
    
async def setup(bot):
    await bot.add_cog(MiscCog(bot))