import os
import discord
from dotenv import load_dotenv
from discord.utils import get

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        print(guild.name)

    guild.fetch_members()
    user = guild.get_member_named("spectregray")
    if user:
        try:
            await user.send("hi")
        except:
            print("dm failed")
            
client.run(TOKEN)