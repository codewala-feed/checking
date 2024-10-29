from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def homepage():
    return {"response":"Hey Coder, You are in homepage :)"}