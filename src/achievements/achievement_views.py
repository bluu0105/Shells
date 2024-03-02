import discord

"""
whereever you call this, you must create:
    file = discord.File("assets/achievement-badge.png", filename="image.png")
and pass in file=file
"""
class AchievementUnlockedEmbed(discord.Embed):
    def __init__(self, title="", description=""):
        super().__init__(title=title,
                         description=description,
                         color=0xf7c95c)
        self.set_author(name="Achievement Unlocked!", icon_url="attachment://image.png")
        self.set_thumbnail(url="attachment://image.png")