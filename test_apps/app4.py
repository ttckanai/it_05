from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    html = """
    <h1>これはタイトル</h1>
    <p>ここに本文</p>
    <a href="/about">Aboutページへ</a>
    """
    return html

@app.route("/about")
def about_page():
    html = """
    <h1>About</h1>
    <p>ほげほげほげほげ</p>
    <a href="/">トップページへ</a>
    """
    return html