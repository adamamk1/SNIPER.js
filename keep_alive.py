from flask import Flask
from threading import Thread

app=Flask("")

@app.route("/")
def index():
    return "<p>Thank you ily for using my app, help me reach 300 subs! pls ;w; - <strong>Zardex 1337</strong></p>"

Thread(target=app.run,args=("0.0.0.0",8080)).start()
