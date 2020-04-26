from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("info.html", remote_ip=get_remote_ip())


@app.route("/<name>")
def user(name):
    return f"Hello {name}!"


def get_remote_ip():
    return request.environ['REMOTE_ADDR']


if __name__ == "__main__":
    app.run(host="0.0.0.0")
