from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return open("index.html").read()
    
    return app

def launch_app():
    app = create_app()
    app.run(port=8000, host="0.0.0.0")

if __name__ == "__main__":
    launch_app()