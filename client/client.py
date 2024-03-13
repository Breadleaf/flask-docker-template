import requests
import flask
import json
import sys

app = flask.Flask(
    __name__,
    static_folder = ".",
    static_url_path = ""
)


API_URL = "http://api:5000/api"

@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    data = flask.request.get_json()
    name = data["name"]
    response = requests.post(
        API_URL,
        json = {
            "name": name
        }
    )
    return response.text


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python client.py <host> <port>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])

    app.run(
        host = host,
        port = port,
        debug = True
    )
