from flask import Flask

from app.data_work.work_with_db import tables_init

app = Flask(__name__)
tables_init()

from app import routes
