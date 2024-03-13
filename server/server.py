import flask_cors
import flask
import sys

app = flask.Flask(__name__)
flask_cors.CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/")
def index():
    return """
    <p>Server Frontend; Please use the API</p>
    """.strip()


@app.route("/api", methods=["POST"])
def api():
    name = flask.request.json.get("name", None)
    if name is None:
        return "Name is required", 400
    return f"Hello, {name}!", 200


if __name__ == "__main__":
    host = None
    port = None

    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <host> <port>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])

    app.run(
        host=host,
        port=port,
        debug=True,
    )
