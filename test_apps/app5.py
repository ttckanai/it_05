from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/hello", methods=["GET"])
def hello_person():
    params = request.args
    if "name" in params:
        name = params["name"]
    else:
        name = "friend"
    print(params)
    html = f"""
    <h1>ごあいさつ</h1>
    <p>Hello {name}!</p>
    """
    return html