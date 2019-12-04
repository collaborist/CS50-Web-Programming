# Ввести в теминале set FLASK_APP=application.py перед работой

from flask import Flask

app = Flask(__name__)

# дефолтная страница
@app.route("/")
def index():
    return "Hello, world!!!"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello, {name}!</h1>"