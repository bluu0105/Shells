import discord
from discord.ui import Select, View, Button
from discord.ext import commands
from firebase_admin import db
import trade.utils

"""
Todo
"""

"""
Commands: /attack, /leaderboard, /profile, /editprofile,/viewattack, /deleteattack,
"""

class AttacksCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.db_ref_users = db.reference("/").child("users")
        self.db_ref_attacks = db.reference("/").child("attacks")
        
    af = discord.app_commands.Group(name="af", description="art fight commands!")
     
    @af.command(name="attack", description="attack a victim!")
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
            await interaction.response.edit_message(content=f"Your choice is **{select_1.values[0]}**! please choose a finish", view=view_2)
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
            await interaction.response.edit_message(content=f"Your choice is **{select_2.values[0]}**! please choose a color", view=view_3)
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
            await interaction.response.edit_message(content=f"Your choice is **{select_3.values[0]}**! please choose a shading", view=view_4)
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
            await interaction.response.edit_message(content=f"Your choice is **{select_4.values[0]}**! please choose a background", view=view_5)
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
            confirm_embed.set_author(name="Art Fight", icon_url=interaction.guild.icon.url)
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
            
            score_calculation = trade.utils.size_calc(select_1.values[0]) + trade.utils.finish_calc(select_2.values[0]) + trade.utils.color_calc(select_3.values[0]) + trade.utils.shading_calc(select_4.values[0]) + trade.utils.background_calc(select_5.values[0])
            content = f"{interaction.user.mention} has attacked {victim.mention} for {score_calculation} points!"
            final_embed = discord.Embed(title="", description="", color=discord.Colour.light_embed())
            final_embed.set_author(name=f"{interaction.user.name}: {message}", icon_url=interaction.user.avatar.url)
            final_embed.set_footer(text="Art Fight", icon_url=interaction.guild.icon.url)
            final_embed.set_image(url="attachment://image.png")
            image_file = await image.to_file(filename="image.png")
            sent_message = await interaction.channel.send(content=content, embed=final_embed, file=image_file, view=None)
            content +=  f" **attack id: {sent_message.id}**"
            await sent_message.edit(content=content)
            attack_info = {sent_message.id: {
                           "attacker":interaction.user.id,
                           "victim":victim.id,
                           "size": select_1.values[0],
                           "finish": select_2.values[0],
                           "color": select_3.values[0],
                           "shading": select_4.values[0],
                           "background": select_5.values[0],
                           "points": score_calculation,
                           "message": message,
                           }}
            
            original_points_1 = 0
            original_sent_1 = {}
            original_received_1 = {}
            original_oclink_1 = "N/A"
            original_notes_1 = "N/A"
 
            if self.db_ref_users.get() != None and str(interaction.user.id) in self.db_ref_users.get():
                db_ref_attacker = self.db_ref_users.child(str(interaction.user.id))
                original_points_1 = db_ref_attacker.child("points").get()
                original_sent_1 = trade.utils.get_none_handler(db_ref_attacker.child("attacks_sent").get())
                original_received_1 = trade.utils.get_none_handler(db_ref_attacker.child("attacks_received").get())
                original_oclink_1 = trade.utils.get_none_handler(db_ref_attacker.child("oclink").get())
                original_notes_1 = trade.utils.get_none_handler(db_ref_attacker.child("notes").get())
            original_sent_1[sent_message.id] = ""
            original_points_1 += attack_info[sent_message.id]["points"]
            
            original_points_2 = 0
            original_sent_2 = {}
            original_received_2 = {}
            original_oclink_2 = "N/A"
            original_notes_2 = "N/A"

            if self.db_ref_users.get() != None and str(victim.id) in self.db_ref_users.get():
                db_ref_attacker = self.db_ref_users.child(str(victim.id))
                original_points_2 = db_ref_attacker.child("points").get()
                original_sent_2 = trade.utils.get_none_handler(db_ref_attacker.child("attacks_sent").get())
                original_received_2 = trade.utils.get_none_handler(db_ref_attacker.child("attacks_received").get())
                original_oclink_2 = trade.utils.get_none_handler(db_ref_attacker.child("oclink").get())
                original_notes_2 = trade.utils.get_none_handler(db_ref_attacker.child("notes").get())
            original_received_2[sent_message.id] = ""
                
            attacker_info = {interaction.user.id: {
                           "name": interaction.user.name,
                           "points": original_points_1,
                           "attacks_sent": original_sent_1,
                           "attacks_received": original_received_1,
                           "oclink": original_oclink_1,
                           "notes": original_notes_1,
                           }}
            victim_info = {victim.id: {
                           "name": victim.name,
                           "points": original_points_2,
                           "attacks_sent": original_sent_2,
                           "attacks_received": original_received_2,
                           "oclink": original_oclink_2,
                           "notes": original_notes_2,
                           }}
            
            self.db_ref_attacks.update(attack_info)
            self.db_ref_users.update(attacker_info)
            self.db_ref_users.update(victim_info)
            
            confirmation_embed = discord.Embed(title="**Attack Successfully Sent!**", color=discord.Colour.light_embed())
            confirmation_embed.set_author(name="Art Fight", icon_url=interaction.guild.icon.url)
            
            await interaction.response.edit_message(content="", embed=confirmation_embed, view=None)
        success_button.callback = success_callback
        
        ##########
        
        cancel_button = Button(label="Cancel Attack" ,style=discord.ButtonStyle.danger)
        async def cancel_callback(interaction: discord.Interaction):
            cancel_embed = discord.Embed(title="**Attack Cancelled**", description="(feel free to dismiss this message)", color=discord.Colour.light_embed())
            cancel_embed.set_author(name="Art Fight", icon_url=interaction.guild.icon.url)
            await interaction.response.edit_message(content="", embed=cancel_embed, view=None)
        cancel_button.callback = cancel_callback
        
        view_6 = View()
        view_6.add_item(success_button)
        view_6.add_item(cancel_button)
        
        ##########
        
        if interaction.user.id == victim.id:
            await interaction.response.send_message("Don't attack yourself D: *(try again)*", ephemeral=True)
        elif interaction.client.user.id == victim.id:
            await interaction.response.send_message("Don't attack the bot D: *(try again)*", ephemeral=True)
        else:
            await interaction.response.send_message("Please select an option:", view=view_1, ephemeral=True)
        
        ##########
        ##########
        ##########
        ##########
    
    @af.command(name="leaderboard", description="displays a leaderboard of who has the most points (top 10)")
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
    
    @af.command(name="profile", description="shows a user\'s profile including points and attack info")
    async def profile(self, interaction: discord.Interaction, user: discord.Member):
        profile_info = ""
        user_dictionary = self.db_ref_users.get()
        
        if user_dictionary == None:
            profile_info = "No users have been logged"
        else:
            users_sorted = sorted(user_dictionary.items(), key=lambda x: x[1]["points"], reverse=True)
            rank = 1
            for key, value in users_sorted:
                if value["name"] == user.name:
                    break
                rank += 1
                
            specified_user = user_dictionary.get(str(user.id))
            if specified_user == None:
                profile_info = "This particular user has not been logged yet, if this user is you then you need to attack or be attacked to have your profile logged"
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
                        
                v_oclink = specified_user.get("oclink")
                #v_oclink = f"[{v_oclink}]({v_oclink})"
                v_notes = specified_user.get("notes")
                
                profile_info += f"User: **<@{user.id}>**\nPoints: **{v_points}**\nRank: **{rank}**\n\nAttacks Sent:\n{v_sent}\nAttacks Received:\n{v_received}\nOC Link:\n**{v_oclink}**\n\nNotes:\n**{v_notes}**\n"
                
        
        embed_profile = discord.Embed(title='', description=profile_info, color=discord.Colour.light_embed())
        # embed_profile.set_thumbnail(url=user.avatar)
        embed_profile.set_author(name=f'{user.name}\'s Profile', icon_url=user.avatar)
        
        await interaction.response.send_message("", embed=embed_profile, ephemeral=True)
    
    @af.command(name="editprofile", description="Allows exisitng users to add links to OCs and preference notes (blanks fields stay the same)")
    async def editprofile(self, interaction: discord.Interaction, new_oc_link: str = "", new_notes: str = ""):
        
        user_dictionary = self.db_ref_users.get()
        
        if new_oc_link == "" and new_notes == "":
            await interaction.response.send_message("You didn't pass in any profile updates to make", ephemeral=True)
        elif user_dictionary == None:
            await interaction.response.send_message("No profiles are currently logged", ephemeral=True)
        elif not (str(interaction.user.id) in user_dictionary):
            await interaction.response.send_message("You aren't logged yet, you need to attack or be attacked in order to create a profile", ephemeral=True)
        else:

            if new_oc_link != "":
                self.db_ref_users.child(str(interaction.user.id)).child("oclink").delete()
                self.db_ref_users.child(str(interaction.user.id)).update({"oclink": new_oc_link})
            if new_notes != "":
                self.db_ref_users.child(str(interaction.user.id)).child("notes").delete()
                self.db_ref_users.child(str(interaction.user.id)).update({"notes": new_notes})
        
            await interaction.response.send_message("Links and Notes have been updated! (feel free to dismiss this message)", ephemeral=True)
        
    @af.command(name="viewattack", description="provides info on the attack as well as a link to the original attack id")
    async def viewattack(self, interaction: discord.Interaction, attack_id: str):
        attack_node = self.db_ref_attacks.child(attack_id).get()
        
        if attack_node == None:
            await interaction.response.send_message("This id does not match with any attacks (feel free to dismiss this message)", ephemeral=True)
        else:
            attacker_info = interaction.guild.get_member(attack_node.get("attacker")).name
            victim_info = interaction.guild.get_member(attack_node.get("victim")).name
            size_info = attack_node.get("size")
            finish_info = attack_node.get("finish")
            color_info = attack_node.get("color")
            shading_info = attack_node.get("shading")
            background_info = attack_node.get("background")
            points_info = attack_node.get("points")
            message_info = attack_node.get("message")
            
            lines_of_info = f"Attacker: **{attacker_info}**\nVictim: **{victim_info}**\nSize: **{size_info}**\nFinish: **{finish_info}**\nColor: **{color_info}**\nShading: **{shading_info}**\nBackground: **{background_info}**\nPoints: **{points_info}**\nMessage: **{message_info}**\n"
            
            original_attack_url = f"https://discord.com/channels/{interaction.guild.id}/{interaction.channel.id}/{int(attack_id)}"
            message_to_send = f"Attack #: **[{attack_id}]({original_attack_url})**\n\n {lines_of_info}"
            embed_viewattack = discord.Embed(title="", description=message_to_send, color=discord.Colour.light_embed())

            await interaction.response.send_message("", embed=embed_viewattack, ephemeral=True)
        
    @af.command(name="deleteattack", description="deletes the given attack and readjusts values, must be a permitted user to use")
    @commands.has_permissions(administrator=True)
    async def deleteattack(self, interaction: discord.Interaction, attack_id: str):
        
        permitted_users = ["skarpetky", "spectregray", "___bryant", "silentvoice._."]
        curr_attacks = self.db_ref_attacks.get()
        if not (interaction.user.name in permitted_users):
            await interaction.response.send_message("You don't have permission to delete attacks", ephemeral=True)
        elif (curr_attacks == None) or (not (attack_id in curr_attacks)):
            await interaction.response.send_message("This attack ID doesn't exist", ephemeral=True)
        else:
            selected_attack = curr_attacks[attack_id]
            point_deduction = selected_attack["points"]
            selected_attacker = self.db_ref_users.child(str(selected_attack["attacker"]))
            selected_victim = self.db_ref_users.child(str(selected_attack["victim"]))
            
            self.db_ref_attacks.child(attack_id).set({})
            selected_attacker.child("attacks_sent").child(attack_id).set({})
            original_points = selected_attacker.child("points").get()
            selected_attacker.child("points").set(original_points - point_deduction)
            selected_victim.child("attacks_received").child(attack_id).set({})
            
            if selected_attacker.child("attacks_sent").get() == None and selected_attacker.child("attacks_received").get() == None:
                selected_attacker.set({})
            if selected_victim.child("attacks_sent").get() == None and selected_victim.child("attacks_received").get() == None:
                selected_victim.set({})    
            
            try:
                msg_to_delete = await interaction.channel.fetch_message(int(attack_id))
                await msg_to_delete.delete()
                await interaction.response.send_message(f"The attack **{attack_id}** has been deleted completely. If this is the attacker's only attack and/or victim's only reception, their respective profiles will have also been deleted.", ephemeral=True)
            except Exception as e:
                await interaction.response.send_message(f"warning, The attack **{attack_id}** has been deleted partially, check to see if all data has been deleted manually", ephemeral=True)
        
async def setup(bot):
    await bot.add_cog(AttacksCog(bot))