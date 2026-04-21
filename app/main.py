from flask import Flask, jsonify, request, abort

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/echo", methods=["POST"])
def echo():
    payload = request.get_json(silent=True)
    if not payload or "message" not in payload:
        abort(400, description="payload must include message")

    message = payload["message"]
    if not isinstance(message, str) or len(message) > 200:
        abort(400, description="message must be a string up to 200 characters")

    return jsonify({"echo": message.strip()}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
