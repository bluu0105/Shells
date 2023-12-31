import discord
from discord.ui import Select, View, Button
from discord.ext import commands
from firebase_admin import db
import trade.utils

"""
Todo
"""

class AttacksCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.db_ref_users = db.reference("/").child("users")
        self.db_ref_attacks = db.reference("/").child("attacks")
     
    @discord.app_commands.command(name="attack", description="attack a victim!")
    async def attack(self, interaction: discord.Interaction, victim: discord.Member, message: str, image: discord.Attachment):

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
        #select_options -> size, finish, color, shading, background
        
        success_button = Button(label="I'm Done!", style=discord.ButtonStyle.success)
        async def success_callback(interaction: discord.Interaction):
            #self.db_ref_users.update({0: "siblings are user ids"})
            #self.db_ref_attacks.update({0: "siblings are message ids"})
            attack_info = {interaction.message.id: {
                           "attacker":interaction.user.id,
                           "victim":victim.id,
                           "size": select_1.values[0],
                           "finish": select_2.values[0],
                           "color": select_3.values[0],
                           "shading": select_4.values[0],
                           "background": select_5.values[0],
                           "points": trade.utils.size_calc(select_1.values[0]) + trade.utils.finish_calc(select_2.values[0]) + trade.utils.color_calc(select_3.values[0]) + trade.utils.shading_calc(select_4.values[0]) + trade.utils.background_calc(select_5.values[0]),
                           }}
            
            original_points_1 = 0
            original_sent_1 = {}
            original_received_1 = {}
 
            if self.db_ref_users.get() != None and str(interaction.user.id) in self.db_ref_users.get():
                db_ref_attacker = self.db_ref_users.child(str(interaction.user.id))
                original_points_1 = db_ref_attacker.child("points").get()
                original_sent_1 = trade.utils.get_none_handler(db_ref_attacker.child("attacks_sent").get())
                original_received_1 = trade.utils.get_none_handler(db_ref_attacker.child("attacks_received").get())
            original_sent_1[interaction.message.id] = ""
            original_points_1 += attack_info[interaction.message.id]["points"]
            
            original_points_2 = 0
            original_sent_2 = {}
            original_received_2 = {}

            if self.db_ref_users.get() != None and str(victim.id) in self.db_ref_users.get():
                db_ref_attacker = self.db_ref_users.child(str(victim.id))
                original_points_2 = db_ref_attacker.child("points").get()
                original_sent_2 = trade.utils.get_none_handler(db_ref_attacker.child("attacks_sent").get())
                original_received_2 = trade.utils.get_none_handler(db_ref_attacker.child("attacks_received").get())
            original_received_2[interaction.message.id] = ""
                
            attacker_info = {interaction.user.id: {
                           "name": interaction.user.name,
                           "points": original_points_1,
                           "attacks_sent": original_sent_1,
                           "attacks_received": original_received_1,
                           }}
            victim_info = {victim.id: {
                           "name": victim.name,
                           "points": original_points_2,
                           "attacks_sent": original_sent_2,
                           "attacks_received": original_received_2,
                           }}

            content = f'{interaction.user.mention} has attacked {victim.mention} for {attack_info.get(interaction.message.id).get("points")} points! *(attack id: {interaction.message.id})*'
            final_embed = discord.Embed(title="", description=message, color=discord.Colour.light_embed())
            final_embed.set_image(url=image.url)
            
            self.db_ref_attacks.update(attack_info)
            self.db_ref_users.update(attacker_info)
            self.db_ref_users.update(victim_info)
            
            confirmation_embed = discord.Embed(title="**Attack Successfully Sent!**", description="Your attack was successfully stored in the database\n(feel free to dismiss this message)", color=discord.Colour.light_embed())
            
            await interaction.response.edit_message(content="", embed=confirmation_embed, view=None)
            await interaction.channel.send(content=content, embed=final_embed, view=None)
        success_button.callback = success_callback
        
        ##########
        
        cancel_button = Button(label="Cancel Attack" ,style=discord.ButtonStyle.danger)
        async def cancel_callback(interaction: discord.Interaction):
            cancel_embed = discord.Embed(title="**Attack Cancelled**", description="(feel free to dismiss this message)", color=discord.Colour.light_embed())
            await interaction.response.edit_message(content="", embed=cancel_embed, view=None)
        cancel_button.callback = cancel_callback
        
        view_6 = View()
        view_6.add_item(success_button)
        view_6.add_item(cancel_button)
        
        ##########
        
        if interaction.user.id == victim.id:
            await interaction.response.send_message("Don't attack yourself D: *(try again)*", ephemeral=True)
        else:
            await interaction.response.send_message("Please select an option:", view=view_1, ephemeral=True)
        
        ##########
        ##########
        ##########
        ##########
    
    @discord.app_commands.command(name="leaderboard", description="displays a leaderboard of who has the most points")
    async def leaderboard(self, interaction: discord.Interaction):
        calculated_standings = ""
        top_3_counter = 1
        user_dictionary = self.db_ref_users.get()
        if user_dictionary == None:
            calculated_standings = "No one has attacked yet"
        else:
            users_sorted = sorted(user_dictionary.items(), key=lambda x: x[1]["points"], reverse=True)
            for key, value in users_sorted:
                if top_3_counter == 1:
                    v_name = value["name"]
                    v_points = value["points"]
                    calculated_standings += f"{top_3_counter} - 🥇 {v_name} - {v_points} points\n"
                    top_3_counter += 1
                elif top_3_counter == 2:
                    v_name = value["name"]
                    v_points = value["points"]
                    calculated_standings += f"{top_3_counter} - 🥈 {v_name} - {v_points} points\n"
                    top_3_counter += 1
                elif top_3_counter == 3:
                    v_name = value["name"]
                    v_points = value["points"]
                    calculated_standings += f"{top_3_counter} - 🥉 {v_name} - {v_points} points\n"
                    top_3_counter += 1
                else:
                    v_name = value["name"]
                    v_points = value["points"]
                    calculated_standings += f"{top_3_counter} - 🏅 {v_name} - {v_points} points\n"
                    top_3_counter += 1
        
        embed_leaderboard = discord.Embed(title="**Paints & Shells Art Fight Leaderboard**", description=calculated_standings, color=discord.Colour.light_embed())
        
        await interaction.response.send_message("", embed=embed_leaderboard, ephemeral=True)
    
    @discord.app_commands.command(name="profile", description="shows a user\'s profile including points and attack info")
    async def profile(self, interaction: discord.Interaction, user: discord.Member):
        profile_info = ""
        user_dictionary = self.db_ref_users.get()
        if user_dictionary == None:
            profile_info = "No users have been logged"
        else:
            specified_user = user_dictionary.get(str(user.id))
            if specified_user == None:
                profile_info = "This particular user has not been logged yet"
            else:
                v_username = specified_user.get("name")
                v_points = specified_user.get("points")
                
                sent_dictionary = specified_user.get("attacks_sent")
                v_sent = ""
                if sent_dictionary == None:
                    v_sent = "**N/A**\n"
                else:
                    for message_id in sent_dictionary:
                        message_url = f"https://discord.com/channels/{interaction.guild.id}/{interaction.channel.id}/{message_id}"
                        v_sent += f"[{message_id}]({message_url})\n"
                
                received_dictionary = specified_user.get("attacks_received")
                v_received = ""
                if received_dictionary == None:
                    v_received = "**N/A**\n"
                else:
                    for message_id in received_dictionary:
                        message_url = f"https://discord.com/channels/{interaction.guild.id}/{interaction.channel.id}/{message_id}"
                        v_received += f"[{message_id}]({message_url})\n"
                
                profile_info += f"Username: **{v_username}**\nPoints: **{v_points}**\n\nAttacks Sent:\n{v_sent}\nAttacks Received:\n{v_received}\n"
                
        
        embed_profile = discord.Embed(title=f"**{user}'s Profile**", description=profile_info, color=discord.Colour.light_embed())
        
        await interaction.response.send_message("", embed=embed_profile, ephemeral=True)
        
async def setup(bot):
    await bot.add_cog(AttacksCog(bot))