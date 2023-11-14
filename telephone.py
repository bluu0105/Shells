import discord
from discord.ext import commands
from firebase_admin import db

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
    
    """
    Starts game if there
    """
    @commands.command()
    async def testcommand(self, ctx):
        await ctx.send("This is a button!", view=self.TelephoneView(self.db_ref))

    @discord.app_commands.command(name='telephonegame')
    async def send_message(self, ctx):
        await ctx.reply('Hello!')

async def setup(bot):
    await bot.add_cog(TelephoneCog(bot))