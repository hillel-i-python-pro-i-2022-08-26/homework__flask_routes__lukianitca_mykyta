from app import app


@app.route("/")
def index():
    return "<h1>Hello user!</h1>"
