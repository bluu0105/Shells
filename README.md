# Shells

The goal is for this to be a multipurpose bot for Paints & Shells! Current functionality:

- Art Fight: "attack" another member by drawing their OC or something for them to get activity points.

Open for anyone to contribute to.

## Python Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/).

2. Clone this repository.

3. Navigate into the `Shells` project directory:

   ```bash
   cd Shells
   ```

4. Create a new virtual environment:

    #### For mac:

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

    #### For windows:

    ```bash
    python -m venv venv
    venv/Scripts/activate
    ```

5. Install the requirements:

   ```bash
   pip install -r requirements.txt
   ```

6. Make an environment variables file (`.env`) You should still be in the `Shells` directory:

   ```bash
   touch .env
   ```
7. Fill in the `.env` file with the following:

    ```bash
    DISCORD_TOKEN=your_discord_bot_token
    FIREBASE_DATABASE_URL=your_firebase_database_url
    FIREBASE_KEY=firebase_key.json
    ```

    * Replace `your_discord_bot_token` with your bot's token.
    * Replace `your_firebase_database_url` with your Firebase database URL.
    * Replace `firebase_key.json` with the path to your Firebase key file.

### Discord Bot

1. You'll need to [create a discord bot](https://discord.com/developers/applications) and invite it to your server.

2. To turn on Presence Intents, go to your bot's [settings](https://discord.com/developers/applications), `Bot -> Privileged Gateway Intents`, and turn on all 3 Presence Intents.

3. Fill in the .env file with your bot token.

    ##### * Bot Role Permissions
    * Once your bot has joined your server, be sure to give it a role with permissions to "Manage Messages"


### Local DB - Firebase

1. Create a [Firebase project](https://console.firebase.google.com/u/0/)
2. Go to `Build -> Realtime Database` and create a database, copy the link you see (ie. `https://example.firebaseio.com`). Save this to your .env file as `FIREBASE_DATABASE_URL`
3. Go to `Project Settings -> ⚙️ -> Service Accounts -> Generate New Private Key` and download the JSON file as `firebase_key.json`.
4. Drag the downloaded file into this directory.
5. Set FIREBASE_KEY in your .env to the path of this key.

    ##### * Possible Firebase issues
    * Is your test database public? Check in Realtime Database > Rules


### Running the bot

Run the app using python or python3 depending on your system (make sure you are in the `Shells/src` directory):

```bash
cd src
python main.py
```

## Database Schema

Designed around a single server.
```
.  
├── "attacks"  
│   └── Attack's Discord Message ID  
│       ├── "attacker"  
│       ├── "victim"  
│       ├── "points"
│       ├── "message"     
│       ├── "size"  
│       ├── "finish"  
│       ├── "color"  
│       ├── "shading"  
│       └── "background"  
└── "users"  
    └── User's Discord ID  
        ├── "name"  
        ├── "points"
        ├── "oclink"
        ├── "notes"      
        ├── "attacks_sent"  
        │   └── [List of attack IDs]  
        └── "attacks_received"  
            └── [List of attack IDs]  
```