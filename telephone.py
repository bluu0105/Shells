import discord
from discord import app_commands
from discord.ext import commands
from discord.utils import get
from firebase_admin import db
from typing import Optional

"""
Art Telephone
"""
class TelephoneCog(commands.Cog):

    class TelephoneView(discord.ui.View): 
        
        def __init__(self, db_ref):
            super().__init__()
            self.db_ref = db_ref

        @discord.ui.button(label="Start Game", style=discord.ButtonStyle.primary, emoji="😎") 
        async def button_callback(self, interaction, button):
            await interaction.response.send_message(content="You clicked the button!") 
            self.db_ref.set({"hello": "bye"})

    def __init__(self, bot):
        self.bot = bot
        self.db_ref = db.reference("/").child("telephone")
        super().__init__()
    
    """
    Starts game if there
    """
    @commands.command()
    async def testcommand(self, ctx):
        await ctx.send("This is a button!", view=self.TelephoneView(self.db_ref))

    # @commands.hybrid_command(name="ping") hybrid command example
    #@app_commands.command(name='game')
    #@commands.command(name='telephone')
    @commands.hybrid_command()
    async def game(self, ctx: commands.Context, command: Optional[str]):
        # Makes sure the message has add_reaction method
        if ctx.message.type == discord.MessageType.default:
            await ctx.message.add_reaction("👍")
        await ctx.reply('Hello!')

async def setup(bot):
    await bot.add_cog(TelephoneCog(bot))