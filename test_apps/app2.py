from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    raise ValueError("やばい")
    return "Hello World!"