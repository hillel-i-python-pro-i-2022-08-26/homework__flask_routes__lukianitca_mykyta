from typing import Generator

from flask import render_template, abort
from webargs import fields
from webargs.flaskparser import use_args

from app import app
from app.data_work import read_txt, get_average_data, ContactsTable
from .users_info import generate_users, get_cosmonauts


# from app.data_work.work_with_db import ContactsTable


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


@app.route("/add-new-contact")
@use_args({"contact_name": fields.Str(required=True), "phone_number": fields.Str(required=True)}, location="query")
def add_contact(args: dict):
    with ContactsTable() as contacts_table:
        contacts_table.add_new_contact(args)
    return "Contact Added successfully"


@app.route("/update-contact/<int:user_id>")
@use_args({"contact_name": fields.Str(), "phone_number": fields.Str()}, location="query")
def update_existing_contact(user_id: int, args: dict):
    with ContactsTable() as contacts_table:
        contacts_table.update_record(user_id, updates=args)
