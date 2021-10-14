import flask

app = flask.Flask(__name__)
app.secret_key = b"I am a secret key"

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    if flask.request.form.get("campus_id") == "jmartin191":
        return flask.redirect(flask.url_for("welcome"))
    else:
        flask.flash("Wrong campus ID")
        return flask.redirect("/")

@app.route("/welcome")
def welcome():
    return "<h1>Welcome John!</h1>"

app.run(port=8080)