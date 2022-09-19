import os

from flask import Flask

app = Flask(__name__)
app.config["FLASK_APP"] = os.environ.get("FLASK_APP")

from app import routes
