import discord

"""
whereever you call this, you must create:
    file = discord.File("assets/achievement-badge.png", filename="image.png")
and pass in file=file
"""
class AchievementUnlockedEmbed(discord.Embed):
    def __init__(self):
        super().__init__(title="I'm rarted",
                         description="I did something really rarted",
                         color=0xf7c95c)
        self.set_author(name="Achievement Unlocked!", url="https://twitter.com/RealDrewData", icon_url="attachment://image.png")
        self.set_thumbnail(url="attachment://image.png")
        self.set_image(url="attachment://image.png")
        self.set_footer(text="Use /achievements to see all of your achievements")