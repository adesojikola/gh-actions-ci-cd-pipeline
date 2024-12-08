from flask import Flask, request

from src import ops

app = Flask(__name__) 


@app.route("/", methods=["GET"])
def index():
    return "App is running successfully."


@app.route("/sum", methods=["GET"])
def sum():
    try:
        n1 = request.args.get("n1", type=int)
        n2 = request.args.get("n2", type=int)
        return f"The sum of {n1} and {n2} is {ops.sum(n1, n2)}."
    except TypeError:
        return "Invalid inputs. Please enter valid integers."
    except Exception:
        return "Something went wrong."


if __name__ == "__main__": 
    app.run()
