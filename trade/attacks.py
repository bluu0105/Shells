import discord
from discord.ui import Select, View, Button
from discord.ext import commands
from firebase_admin import db

"""
Todo
"""

class AttacksCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.db_ref = db.reference("/").child("attacks")
     
    @discord.app_commands.command(name="attack")
    async def attack(self, interaction: discord.Interaction, victim: discord.Member, message: str, image: discord.Attachment, number_of_characters: int):

        #select_options -> size, finish, color, shading, background
        
        select_1 = Select(
            placeholder="Choose an attack size",
            options=[
                discord.SelectOption(label="Simple"),
                discord.SelectOption(label="Portrait"),
                discord.SelectOption(label="Half Body"),
                discord.SelectOption(label="Full Body")
            ]
        )
        async def callback_1(interaction: discord.Interaction):
            await interaction.response.edit_message(content=f"Your choice is **{select_1.values[0]}**!, please choose a finish", view=view_2)
        select_1.callback = callback_1
        view_1 = View()
        view_1.add_item(select_1)
        
        ##########
        
        select_2 = Select(
            placeholder="Choose an attack finish",
            options=[
                discord.SelectOption(label="Rough"),
                discord.SelectOption(label="Clean/Lined/Lineless")
            ]
        )
        async def callback_2(interaction: discord.Interaction):
            await interaction.response.edit_message(content=f"Your choice is **{select_2.values[0]}**!, please choose a color", view=view_3)
        select_2.callback = callback_2
        view_2 = View()
        view_2.add_item(select_2)
        
        ##########
        
        select_3 = Select(
            placeholder="Choose an attack color",
            options=[
                discord.SelectOption(label="Uncolored"),
                discord.SelectOption(label="Rough"),
                discord.SelectOption(label="Clean Color/Painted")
            ]
        )
        async def callback_3(interaction: discord.Interaction):
            await interaction.response.edit_message(content=f"Your choice is **{select_3.values[0]}**!, please choose a shading", view=view_4)
        select_3.callback = callback_3
        view_3 = View()
        view_3.add_item(select_3)
        
        ##########
        
        select_4 = Select(
            placeholder="Choose an attack shading",
            options=[
                discord.SelectOption(label="Unshaded"),
                discord.SelectOption(label="Minimal"),
                discord.SelectOption(label="Fully Shaded")
            ]
        )
        async def callback_4(interaction: discord.Interaction):
            await interaction.response.edit_message(content=f"Your choice is **{select_4.values[0]}**!, please choose a background", view=view_5)
        select_4.callback = callback_4
        view_4 = View()
        view_4.add_item(select_4)
        
        ##########
        
        select_5 = Select(
            placeholder="Choose an attack background",
            options=[
                discord.SelectOption(label="None"),
                discord.SelectOption(label="Pattern/Abstract"),
                discord.SelectOption(label="Props"),
                discord.SelectOption(label="Full Scene"),
            ]
        )
        async def callback_5(interaction: discord.Interaction):
            confirm_embed = discord.Embed(title="Confirm Attack", color=discord.Colour.light_embed(), description=f"Size: **{select_1.values[0]}**\nFinish: **{select_2.values[0]}**\nColor: **{select_3.values[0]}**\nShading: **{select_4.values[0]}**\nBackground: **{select_5.values[0]}**\n")
            await interaction.response.edit_message(content=None, embed=confirm_embed, view=view_6)
        select_5.callback = callback_5
        view_5 = View()
        view_5.add_item(select_5)
        
        ##########
        
        await interaction.response.send_message("Please select an option:", view=view_1, ephemeral=True)
        
        success_button = Button(label="I'm Done!", style=discord.ButtonStyle.success)
        async def success_callback(interaction: discord.Interaction):
            content = f'{interaction.user.mention} has attacked {victim.mention} for (INSERT POINT CALCULATION HERE)!'
            final_embed = discord.Embed(title="", description=message, color=discord.Colour.light_embed())
            final_embed.set_image(url=image.url)
            
            confirmation_embed = discord.Embed(title="**Attack Successfully Sent!**", description="Your attack was (NOT) successfully stored in the database\n(feel free to dismiss this message)", color=discord.Colour.light_embed())
            
            await interaction.response.edit_message(content="", embed=confirmation_embed, view=None)
            await interaction.channel.send(content=content, embed=final_embed, view=None)
        success_button.callback = success_callback
        
        cancel_button = Button(label="Cancel Attack" ,style=discord.ButtonStyle.danger)
        async def cancel_callback(interaction: discord.Interaction):
            cancel_embed = discord.Embed(title="**Attack Cancelled**", description="(feel free to dismiss this message)", color=discord.Colour.light_embed())
            await interaction.response.edit_message(content="", embed=cancel_embed, view=None)
        cancel_button.callback = cancel_callback
        
        view_6 = View()
        view_6.add_item(success_button)
        view_6.add_item(cancel_button)
        
        ##########
        
async def setup(bot):
    await bot.add_cog(AttacksCog(bot))