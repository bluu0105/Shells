import discord
from discord import app_commands
from discord.ext import commands
from misc.about_views import AboutView, AboutEmbed
# from misc.achievement_views import AchievementUnlockedEmbed
from firebase_admin import db

"""
This cog contains miscellaneous commands not specific to any game.
"""

class MiscCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="Info about commands, etc.")
    async def help(self, interaction: discord.Interaction):
        await interaction.response.send_message(embed=AboutEmbed(), view=AboutView(), ephemeral=True)
    
async def setup(bot):
    await bot.add_cog(MiscCog(bot))