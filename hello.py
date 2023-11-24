from flask import Flask
from flask import render_template

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return render_template("index.html")
    
    return app

def launch_app():
    app = create_app()
    app.run(port=8000, host="0.0.0.0", debug=True)

if __name__ == "__main__":
    launch_app()