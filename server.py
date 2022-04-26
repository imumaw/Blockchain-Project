from flask import Flask, request, send_file
import block_lib as blib

blockchain = blib.Blockchain(6)

ROOT = "/definitely-cs-project"

app = Flask(__name__)

@app.route(ROOT + "/")
def index():
    return send_file("webpage.html")

@app.route(ROOT + "/send", methods=["POST"])
def send():
    raw_message = request.get_json()

    message = blib.Message(
        sender=raw_message['from'], 
        receiver=raw_message['to'], 
        message=raw_message['message']
        )

    blockchain.add_message(message)

    return "Block added.", 200

@app.route(ROOT + "/chain")
def chain():
    return blockchain.html()

@app.route(ROOT + "/logo")
def logo():
    return send_file("logo.png")

if __name__ == "__main__":
    app.run(debug=True)
