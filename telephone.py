import discord
from discord import app_commands
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
        super().__init__()
    
    """
    Test command for views
    """
    @commands.command()
    async def testcommand(self, ctx):
        await ctx.send("This is a button!", view=self.TelephoneView(self.db_ref))

    """
    Test command
    """
    @commands.hybrid_command()
    async def test(self, ctx):
        # Makes sure the message is a default message before adding a reaction
        if ctx.message.type == discord.MessageType.default:
            await ctx.message.add_reaction("👍")
        await ctx.reply('Hello!')
    
    """
    Invites a player to join art telephone via dm.
    TODO
    - Shows current queue
    - Has button with "join"
    - Shows the inviter
    """
    @commands.hybrid_command(
            brief="Invite someone to join telephone with their username.",
            description="Invite a user with their discord username to join a telephone game."
    )
    async def invite(self, ctx, username, game_id):
        await ctx.reply("This command is under works")

async def setup(bot):
    await bot.add_cog(TelephoneCog(bot))