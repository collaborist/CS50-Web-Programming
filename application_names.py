from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    names = ["Othello", "Iago", "Cassio"]
    return render_template("index_names.html", names = names)