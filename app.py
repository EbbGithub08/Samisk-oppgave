from flask import Flask, render_template


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/")
    def index():
        return render_template("index.html")

    return app

    @app.get("/historie")
    def historie():
        return render_template("historie.html")

    @app.get("/kultur")
    def kultur():
        return render_template("kultur.html")

    @app.get("/kontakt")
    def kontakt():
        return render_template("kontakt.html")

if __name__ == "__main__":
    create_app().run(debug=True)