# ShellArtTrade
The goal is for this to be a multipurpose bot for Paints & Shells (UMD Art Club). Current functionality:
* Nothing

Open for anyone to contribute to.
## Setup Python venv
For mac:
```
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

For windows:
```
$ python -m venv venv
$ venv/Scripts/activate
$ pip install -r requirements.txt
```
## Running locally
1. You'll need to create a discord bot at https://discord.com/developers/applications
2. Create a .env file, with `DISCORD_TOKEN={your token}`

#### Turning on Presence Intents
For your local bot, you'll need to go to https://discord.com/developers/applications
Settings -> Privileged Gateway Intents
Turn on all 3 Presence Intents.

#### Local DB - Firebase
1. Create a [Firebase project](https://console.firebase.google.com/u/0/)
2. Go to "Realtime Database" and create a database, copy the link you see (should end with firebase.io.com). Save this to your .env file as `FIREBASE_DATABASE_URL`
3. Go to Project Settings > Service Accounts > Generate New Private Key
4. Drag the downloaded file into this directory. Change the name to `firebase_key`. 
5. Set FIREBASE_KEY in your .env to the path of this key. 

##### Possible Firebase issues
* is your test database public? Check in Realtime Database > Rules

## Database Schema
Designed around a single server.
"Points" -> "User" : their points
"Attacks-Made" -> user_id -> idk yet
"Attacks-Recieved" -> user_id -> idk yet
