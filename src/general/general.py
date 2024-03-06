import discord
from discord import app_commands
from discord.ext import commands
from general.help_views import HelpView, HelpEmbed 
# from misc.achievement_views import AchievementUnlockedEmbed
from firebase_admin import db

"""
This cog contains miscellaneous commands not specific to any game.
"""

class GeneralCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db_ref_users = db.reference("/").child("users")
        self.db_ref_attacks = db.reference("/").child("attacks")

    # Collab
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content != "fart club" and message.channel.id == 1214590079146922054:
            await message.delete()

    @app_commands.command(name="help", description="Info about commands, etc.")
    async def help(self, interaction: discord.Interaction):
        await interaction.response.send_message(embed=HelpEmbed(), view=HelpView(), ephemeral=True)

    @app_commands.command(name="profile", description="View your profile")
    async def profile(self, interaction: discord.Interaction, user: discord.Member=None):
        if user is None:
            user = interaction.user

        profile_info = ""
        user_dictionary = self.db_ref_users.get()
        user_attacks = self.db_ref_attacks.get(str(user.id))
        user_profile = db.reference("/profiles").get(str(user.id))
        
        if user_attacks is None and user_profile is None:
            profile_info = "Nothing to see here :) If this is you, please use `/editprofile` to add a profile."
        else:
            if user_dictionary is not None:
                users_sorted = sorted(user_dictionary.items(), key=lambda x: x[1]["points"], reverse=True)
                rank = 1
                for key, value in users_sorted:
                    if value["name"] == user.name:
                        break
                    rank += 1
                    
                specified_user = user_dictionary.get(str(user.id))

                if specified_user is not None:
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
                            
            if user_profile is not None:
                v_oclink = user_profile[0][str(user.id)]["oclink"] if "oclink" in user_profile[0][str(user.id)] else "None"
                #v_oclink = f"[{v_oclink}]({v_oclink})"
                v_notes = user_profile[0][str(user.id)]["notes"] if "notes" in user_profile[0][str(user.id)] else "None"
                
            profile_info += f"User: **<@{user.id}>**\nPoints: **{v_points}**\nRank: **{rank}**\n\nAttacks Sent:\n{v_sent}\nAttacks Received:\n{v_received}\nOC Link:\n**{v_oclink}**\n\nNotes:\n**{v_notes}**\n"
                
        
        embed_profile = discord.Embed(title='', description=profile_info, color=discord.Colour.light_embed())
        # embed_profile.set_thumbnail(url=user.avatar)
        embed_profile.set_author(name=f'{user.name}\'s Profile', icon_url=user.avatar)
        
        await interaction.response.send_message("", embed=embed_profile, ephemeral=True)

    @app_commands.command(name="editprofile", description="Add a link to your oc's and/or a description of your favorite things")
    async def editprofile(self, interaction: discord.Interaction, new_oc_link:str="no_changes_made", new_notes:str="no_changes_made"):
        db_ref_profiles = db.reference("/").child("profiles")
        
        if new_oc_link == "no_changes_made" and new_notes == "no_changes_made":
            await interaction.response.send_message("You didn't pass in any profile updates.", ephemeral=True)
        else:
            db_ref_profiles.child(str(interaction.user.id)).update({"oclink": new_oc_link})
            db_ref_profiles.child(str(interaction.user.id)).update({"notes": new_notes})
        
            await interaction.response.send_message("Links and Notes have been updated!", ephemeral=True)
        
    @app_commands.command(name="leaderboard", description="Shows an activity-based leaderboard for all the games")
    async def leaderboard(self, interaction: discord.Interaction):
        calculated_standings = ""
        top_3_counter = 1
        user_dictionary = self.db_ref_users.get()
        if user_dictionary == None:
            calculated_standings = "No one has attacked yet"
        else:
            users_sorted = sorted(user_dictionary.items(), key=lambda x: x[1]["points"], reverse=True)
            for key, value in users_sorted:
                if value["points"] == 0:
                    break
                
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
                elif top_3_counter >= 4 and top_3_counter <= 10:
                    v_name = value["name"]
                    v_points = value["points"]
                    calculated_standings += f"{top_3_counter} - 🏅 {v_name} - {v_points} points\n"
                    top_3_counter += 1
            
            while top_3_counter <= 10:
                calculated_standings += f"{top_3_counter} -\n"
                top_3_counter += 1
        
        embed_leaderboard = discord.Embed(title="**Art Fight Leaderboard**", description=calculated_standings, color=discord.Colour.light_embed())
        
        await interaction.response.send_message("", embed=embed_leaderboard, ephemeral=True)
    

async def setup(bot):
    await bot.add_cog(GeneralCog(bot))

