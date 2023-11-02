import os
from dotenv import load_dotenv
import json
# Discord
import discord
from discord.ext import commands
# Firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Discord setup
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.members = True
intents.typing = False
intents.presences = False

all_extensions = [
    "setup",
    "trade.attacks"
]

class PSBot(commands.Bot):
    def __init__(self, intents):
        config = json.load(open("config.json"))["bot_config"]
        super().__init__(**config, intents = intents)
    
    # runs before bot starts
    async def setup_hook(self):
        await firebase_setup()
        for extension in all_extensions:
            self.load_extension(extension)

    async def on_ready(self):
        await self.change_presence(activity=discord.Game('with your mom'))

async def firebase_setup():
    database_url = os.getenv('FIREBASE_DATABASE_URL')
    cred = credentials.Certificate(os.getenv('FIREBASE_KEY'))
    firebase_admin.initialize_app(cred, {
        "databaseURL": database_url
    })
        
PSBot(intents=intents).run(TOKEN)