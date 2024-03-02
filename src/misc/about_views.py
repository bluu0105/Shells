import discord

about_color = 0xbbbfba
artfight_color = 0xe35e4f
telephone_color = 0x7ee07f

class AboutSelect(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="General Commands", emoji="⚙️", description="See commands not specifc to any game"),
            discord.SelectOption(label="Art Fight", emoji="⚔️", description="\"Attack\" a fellow member with your art!"),
            # discord.SelectOption(label="Telephone",emoji="☎️",description="This is option 2!"),
        ]
        super().__init__(placeholder="Select a game mode to see commands",
                         max_values=1,
                         min_values=1,
                         options=options)
    
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "General Commands":
            await interaction.response.edit_message(embed=AboutEmbed())
        elif self.values[0] == "Art Fight":
            await interaction.response.edit_message(embed=ArtFightEmbed())
        elif self.values[0] == "Telephone":
            await interaction.response.edit_message(embed=TelephoneEmbed())

class AboutView(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
        self.add_item(AboutSelect())

class AboutEmbed(discord.Embed):
    def __init__(self):
        super().__init__(title="⚙️ General Commands",
                         description="To see game-specific commands, use the dropdown below.",
                         color=about_color)
        self.add_field(name="👤 `/profile`", value="Add a short bio and/or link to an OC folder.", inline=False)
        self.add_field(name="👤 `/editprofile`", value="Use this to modify your profile!", inline=False)
        self.add_field(name="🏆 `/leaderboard`", value="View the activity leaderboard for all games.", inline=False)
        # self.add_field(name="🎖️ `/achievements`", value="View your achievements, or someone else's 😳.", inline=False)
        # self.add_field(name="💬 `/feedback`", value="Send anonymous feedback or suggestions.", inline=False)

class ArtFightEmbed(discord.Embed):
    def __init__(self):
        super().__init__(title="⚔ ️Art Fight",
                         description="Art fight is a game where artists \"attack\" fellow artists by making art of the \"victim's\" OCs or favorite things. To share your OC's and favorites, be sure to update your profile with `/editprofile`! [This game is based on the original ArtFight.](https://artfight.net/info/about#:~:text=Art%20Fight%20is%20an%20annual,which%20they%20are%20assigned%20randomly.).",
                         color=artfight_color)
        self.add_field(name="🖌️ `/af attack`", value="Attack a fellow member by creating art for them! You can ask them what they like, or check their `/profile`.", inline=False)
        self.add_field(name="❌ `/af delete`", value="Made an oopsie? Delete an attack. You'll need to find your attack's id for this.", inline=False)
        self.add_field(name="🔎 `/af view`", value="View the details for a specific attack. You'll need the attack's id for this.", inline=False)
    
class TelephoneEmbed(discord.Embed):
    def __init__(self):
        super().__init__(title="☎️ Telephone",
                         description="Art fight is a game where artists \"attack\" fellow artists by making art of the \"victim's\" OCs or favorite things. To share your OC's and favorites, be sure to update your profile with /editprofile!",
                         color=telephone_color)
        self.add_field(name="🖌️ `/af attack`", value="Attack a fellow member by creating art for them! You can ask them what they like, or check their `/profile`.", inline=False)