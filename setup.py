# import discord
from discord.ext import commands
from firebase_admin import db
from datetime import datetime

"""
Commands for bot set up within a server. i.e. configuring the channel to spam messages in.
TODO: SetUp commands should only be callable by server admin.
"""

class SetUpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    """
    TODO: Delete this later
    Here, when you type !boop, it'll insert the current time into the database.(lmao)
    """
    @commands.command(name='boop')
    async def send_message(self, ctx):
        print("booped")
        database_ref = db.reference("/")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        data = {
            "boop": current_time
        }
        database_ref.child("hi").set(data)


async def setup(bot):
    await bot.add_cog(SetUpCog(bot))