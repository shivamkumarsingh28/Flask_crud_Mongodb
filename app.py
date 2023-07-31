from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = "secret key"
app.config["MONGO_URI"] = "mongodb://localhost:27017/saeeamdb"
mongo = PyMongo(app)

