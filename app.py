from flask import Flask, request
from database import insert_data, delete_data

app = Flask(__name__)

@app.route("/", methods=["GET"])
def homepage():
    return {"response":"Hey Coder, You are in homepage :)"}

@app.route("/create", methods=["POST"])
def create_user():
    user = request.json
    return insert_data(user)

@app.route("/delete", methods=["DELETE"])
def delete_user():
    user = request.json
    return delete_data(user)