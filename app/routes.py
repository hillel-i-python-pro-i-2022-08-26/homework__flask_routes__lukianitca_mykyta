from typing import Generator

from flask import render_template, abort
from webargs import fields
from webargs.flaskparser import use_args

from app import app
from app.data_work import read_txt, get_average_data, ContactsTable
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


@app.route("/add-new-contact")
@use_args({"contact_name": fields.Str(required=True), "phone_number": fields.Str(required=True)}, location="query")
def add_contact(args: dict):
    operation_info = {"operation_name": "add", "is_successful": True}
    with ContactsTable() as contacts_table:
        contacts_table.add_new_contact(args)
    return render_template("operation_status.html", operation_info=operation_info)


@app.route("/update-contact")
@use_args(
    {"user_id": fields.Int(required=True), "contact_name": fields.Str(), "phone_number": fields.Str()}, location="query"
)
def update_existing_contact(args: dict):
    user_id = args.pop("user_id")
    operation_info = {"operation_name": "update", "is_successful": False}
    with ContactsTable() as contacts_table:
        try:
            contacts_table.update_record(user_id=user_id, updates=args)
            operation_info["is_successful"] = True
            return render_template("operation_status.html", operation_info=operation_info)
        except ValueError:
            return render_template("operation_status.html", operation_info=operation_info)


@app.route("/delete-contact/<int:user_id>")
def delete_contact(user_id: int):
    operation_info = {"operation_name": "delete", "is_successful": True}
    with ContactsTable() as contacts_table:
        contacts_table.delete_record(user_id=user_id)
    return render_template("operation_status.html", operation_info=operation_info)


@app.route("/read/<int:user_id>")
def read_one_contact(user_id: int):
    with ContactsTable() as contacts_table:
        contact = contacts_table.get_one_record(user_id=user_id)
    if contact:
        return render_template("one_contact.html", contact=contact)
    operation_info = {"operation_name": "get one", "is_successful": False}
    return render_template("operation_status.html", operation_info=operation_info)


@app.route("/read-all")
def read_all_contacts():
    with ContactsTable() as contacts_table:
        contacts = contacts_table.get_all_records()
    return render_template("all_contacts.html", contacts=contacts)
