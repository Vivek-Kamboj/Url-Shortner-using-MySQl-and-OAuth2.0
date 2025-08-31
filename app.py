
from flask import Flask, redirect, render_template, request, url_for, jsonify, session
import json
from authlib.integrations.flask_client import OAuth

from utils import generate_code
from dao import MySQLDAO
import requests

configs = json.load(open("config.json"))

app = Flask(__name__)
dao = MySQLDAO(password=configs["mysql_pass"], database=configs["mysql_table"])
dao.create_table()

app.secret_key = configs["secret_key"]

oauth = OAuth(app)
oauth.register(
    name="google",
    client_id=configs["google_client_id"],
    client_secret=configs["google_client_secret"],
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile https://www.googleapis.com/auth/user.birthday.read https://www.googleapis.com/auth/user.gender.read"},
)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        original_url = request.form["url"]
        code = generate_code(original_url)
        dao.insert_url(code, original_url)
        short_url = request.host_url + code
        print(request.host_url)
        return render_template("result.html", short_url = short_url)
    return render_template("index.html", session = session.get("google_token"), pretty = json.dumps(session.get("google_token"), indent=4))

@app.route("/<code>")
def redirect_to_url(code):
    original_url = dao.get_url(code)

    if original_url:
        return redirect(original_url)

    return "Url not Found", 404

@app.route("/google-login")
def google_login():
    redirect_uri = url_for("google_callback", _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

@app.route("/google-callback")
def google_callback():
    token = oauth.google.authorize_access_token()
    personal_url = "https://people.googleapis.com/v1/people/me?personFields=genders,birthdays"
    personal_info = requests.get(personal_url, headers={"Authorization": f"Bearer {token['access_token']}"})
    token["personal_info"] = personal_info.json()
    session["google_token"] = token
    return redirect(url_for("index"))

@app.route("/logout")
def logout():
    session.pop("google_token", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)