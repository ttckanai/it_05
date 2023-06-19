from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    html = """
    <h1>これはタイトル</h1>
    <p>ここに本文</p>
    """
    return html