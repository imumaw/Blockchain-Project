from flask import Flask, request, send_file
import block_lib as blib

blockchain = blib.Blockchain(3)

ROOT = "/definitely-cs-project"

app = Flask(__name__)

@app.route(ROOT + "/")
def index():
    return send_file("webpage.html")

@app.route(ROOT + "/send", methods=["POST"])
def send():
    raw_messages = request.get_json()

    messages = []
    for raw_message in raw_messages:
        message = blib.Message(
            sender=raw_message['from'], 
            receiver=raw_message['to'], 
            message=raw_message['message']
            )

        messages.append(message)

    new_block = blib.Block(messages)
    # How to add to blockchain???
    return "Block added.", 200

@app.route(ROOT + "/chain")
def chain():
    return blockchain.html()

if __name__ == "__main__":
    app.run(debug=True)
