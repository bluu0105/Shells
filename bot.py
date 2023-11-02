import os
# Discord
import discord
from dotenv import load_dotenv
from discord.utils import get
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

client = discord.Client(intents=intents)

# Firebase setup
database_url = os.getenv('FIREBASE_DATABASE_URL')
cred = credentials.Certificate(os.getenv('FIREBASE_KEY'))
firebase_admin.initialize_app(cred, {
    "databaseURL": database_url
})

@client.event
async def on_ready():
    for guild in client.guilds:
        print(guild.name)

    # This is the ROOT node
    database_ref = db.reference("/")

    data = {
        "hee": "hoo",
        "haa": "haa",
    }
    database_ref.child("hi").set(data)
        
client.run(TOKEN)