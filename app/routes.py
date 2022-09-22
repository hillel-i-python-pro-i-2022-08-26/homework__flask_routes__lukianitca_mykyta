from typing import Generator

from flask import render_template, abort
from webargs import fields
from webargs.flaskparser import use_args

from app import app
from app.data_work import read_txt, get_average_data
from .users_info import generate_users, get_cosmonauts


@app.route("/")
def index():
    return render_template("index.html", title="Main Page")


@app.route("/requirements")
def show_txt():
    text_from_file: str = read_txt()
    return render_template("requirements.html", title="Requirements", text=text_from_file)


@app.route("/generate-users")
@use_args({"users_number": fields.Int(missing=100)}, location="query")
def show_users_info(args: dict):
    users_amount_show: int = args["users_number"]
    if users_amount_show in range(1, 251):
        users_list: Generator = generate_users(users_amount_show)
        return render_template("gen_users.html", title="Users Information", users_list=users_list)
    return abort(404, "Incorrect number of users")


@app.route("/space")
def show_cosmonauts():
    astro_dict: dict = get_cosmonauts()
    return render_template("cosmonauts.html", title="Cosmonauts", astro=astro_dict)


@app.route("/mean")
def calculate_people_info():
    avg_data: dict = get_average_data()
    return render_template("avg_data.html", title="Live research", avg_data=avg_data)
