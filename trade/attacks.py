from discord.ext import commands

"""
Todo
"""

class AttacksCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(AttacksCog(bot))