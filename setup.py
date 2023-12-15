import discord
from discord.ext import commands
from firebase_admin import db
from datetime import datetime

from pprint import pprint

"""
Commands for bot set up within a server. i.e. configuring the channel to spam messages in.
"""

class SetUpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    """
    Sync command for syncing slash commands.
    """
    @commands.command()
    @commands.is_owner()
    async def sync(self, ctx):
        try: 
            self.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await self.bot.tree.sync()
            print(synced)
            await ctx.send("Synced")
        except discord.HTTPException as e:
            await ctx.send("Failed" + str(e))

async def setup(bot):
    await bot.add_cog(SetUpCog(bot))