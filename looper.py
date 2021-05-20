from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "<p>I dont know how you got here, but nice to meet ya.<br>Oh? you want to know where this place is?<br> This place is nowhere and everywhere.</p>"

def run():
  app.run(host='0.0.0.0',port=8080)

def loop():
    t = Thread(target=run)
    t.start()