# import discord
from discord.ext import commands
from firebase_admin import db
from datetime import datetime

"""
Commands for bot set up. i.e. configuring the channel to spam messages in.
"""

class SetUpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    """
    Here, when you type !boop, it'll insert the current time into the database.(lmao)
    """
    @commands.command(name='boop')
    async def send_message(self, ctx):
        database_ref = db.reference("/")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        data = {
            "boop": current_time
        }
        database_ref.child("hi").set(data)


async def setup(bot):
    await bot.add_cog(SetUpCog(bot))