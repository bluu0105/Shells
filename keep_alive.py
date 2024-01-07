from flask import Flask
from threading import Thread
import schedule

app = Flask('')

@app.route('/')
def home():
    return "hello from the other side"

def print_message():
  print("I'm still alive")

schedule.every(30).minutes.do(print_message)

def run():
  app.run(host='0.0.0.0',port=8080)

  while True:
    schedule.run_pending()

def keep_alive():
    t = Thread(target=run)
    t.start()
