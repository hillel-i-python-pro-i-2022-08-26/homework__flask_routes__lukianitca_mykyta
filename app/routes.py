from flask import render_template, abort
from app import app
from app.data_work import read_txt, get_average_data
from .users_info import generate_users, get_astronauts
from webargs import fields
from webargs.flaskparser import use_args
from typing import Generator


@app.route("/")
def index():
    return "<h1>Hello user!</h1>"


@app.route("/requirements")
def show_txt():
    text: str = read_txt()
    return render_template("requirements.html", title="Requirements", text=text)


@app.route("/generate-users")
@use_args({"user_num": fields.Int()}, location="query")
def show_users_info(args: dict):
    user_num: int = args.get("user_num", 100)
    if user_num in range(1, 251):
        users: Generator = generate_users(user_num)
        return render_template(
            "gen_users.html", title="Users Information", users_list=users
        )
    return abort(404, "Incorrect number of users")


@app.route("/space")
def show_cosmonauts():
    astro_dict: dict = get_astronauts()
    return render_template("astronauts.html", title="Astronauts", astro=astro_dict)


@app.route("/mean")
def calculate_people_info():
    avg_data: dict = get_average_data()
    return render_template("avg_data.html", title="Live research", avg_data=avg_data)
