from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/fibonacci", methods=["GET"])
def fibonacci():
    params = request.args
    if "n" in params:
        n = int(params["n"])
        if n < 2:
            n = 2
    else:
        n = 10
    array = [1,1]
    for i in range(n-2):
        array.append(array[-2] + array[-1])

    response = {
        "params":params,
        "output":{
            "array":array
        }
    }
    return response

if __name__ == "__main__":
    app.run(debug=True)