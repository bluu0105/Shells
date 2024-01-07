from flask import Flask
from threading import Thread
import asyncio

app = Flask('')

@app.route('/')
def home():
    asyncio.ensure_future(print_statement())
    return "hello from the other side"

async def print_statement():
    while True:
        print("boop")
        await asyncio.sleep(1800) 

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()