from app import app


@app.route("/")
def index():
    return "<h1>Hello user!</h1>"


@app.route("/requirements")
def show_txt():
    pass


@app.route("/generate-users")
def generate_users():
    pass


@app.route("/space")
def show_cosmonauts():
    pass


@app.route("/mean")
def calculate_people_info():
    pass
