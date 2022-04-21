from flask import Flask
import block_lib as blib

chain = blib.Blockchain(3)

message1 = blib.Message( "Dr. Morrison", "Definitely CS Majors Group", "Wow this is decently formatted" )
messages1 = [message1]

chain.add_block( messages1 )

message2 = blib.Message( "Definitely CS Majors Group", "Dr. Morrison", "Thank you professor!" )
message3 = blib.Message( "Definitely CS Majors Group", "Dr. Morrison", "Here's hoping for that gift card prize!" )
messages2 = [message2, message3]

chain.add_block( messages2 )

ROOT = "/definitely-cs-project"

app = Flask(__name__)

@app.route(ROOT + "/")
def index():
    return chain.html()

@app.route(ROOT + "/send")
def send():
    return "We should be able to POST messages here."

if __name__ == "__main__":
    app.run(debug=True)
