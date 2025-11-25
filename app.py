from flask import Flask, render_template


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/")
    def index():
        return render_template("index.html")

    return app

# test commit
if __name__ == "__main__":
    create_app().run(debug=True)