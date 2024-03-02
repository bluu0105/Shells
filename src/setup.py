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
    Admin only help
    """
    @commands.command()
    @commands.is_owner()
    async def modhelp(self, ctx):
        embed = discord.Embed(color=0x6d8abf)
        embed.add_field(name="`/sync`", value="Sync commands with bot tree. Required when command names are updated.", inline=False)
        await ctx.send(embed=embed)

    """
    Sync command for syncing slash commands.
    """
    @commands.command()
    @commands.is_owner()
    async def sync(self, ctx):
        try: 
            self.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await self.bot.tree.sync()
            print(f"Synced {len(synced)} commands/n")
            await ctx.send("Synced")
        except discord.HTTPException as e:
            await ctx.send("Failed" + str(e))

async def setup(bot):
    await bot.add_cog(SetUpCog(bot))