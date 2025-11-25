from flask import Flask, jsonify


def create_app() -> Flask:
    """Application factory for easier testing and configuration."""
    app = Flask(__name__)

    @app.get("/")
    def index():
        return jsonify(message="Hello, Sápmi!"), 200

    return app


if __name__ == "__main__":
    create_app().run(debug=True)

