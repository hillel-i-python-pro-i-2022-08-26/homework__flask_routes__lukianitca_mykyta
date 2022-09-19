from flask import render_template, abort
from app import app
from app.data_work import read_txt
from .users_info import generate_users
from webargs import fields
from webargs.flaskparser import use_args


@app.route("/")
def index():
    return "<h1>Hello user!</h1>"


@app.route("/requirements")
def show_txt():
    text: str = read_txt()
    return render_template("requirements.html", title="Requirements", text=text)


@app.route("/generate-users")
@use_args({"user_num": fields.Int(required=True)}, location="query")
def show_users_info(args):
    user_num = args["user_num"]
    if user_num in range(1, 250):
        users = generate_users()
        return render_template(
            "gen_users.html", title="Users Information", users_list=users
        )
    else:
        return abort(404)


@app.route("/space")
def show_cosmonauts():
    pass


@app.route("/mean")
def calculate_people_info():
    pass
