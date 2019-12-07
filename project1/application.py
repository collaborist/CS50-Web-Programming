import os, requests

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():

    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "UhfsSEQUF0WNoD7yNaKcA", "isbns": "9781632168146"})
    print(res.json())
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    """Book a flight."""

    # Get form information.
    name = request.form.get("name")
    password = request.form.get("password")
    if (name == "") or (password == ""):
        return render_template("error.html", message="Name or Password is empty!")
    #print(name,password)
    db.execute("INSERT INTO users (name, password) VALUES (:name, :password)", {"name": name, "password": password})
    db.commit()
    return render_template("success.html")
