from flask import Flask

ROOT = "/definitely-cs-project"

app = Flask(__name__)

@app.route(ROOT + "/")
def index():
    return "This should show the blockchain."

@app.route(ROOT + "/send")
def send():
    return "We should be able to POST messages here."

