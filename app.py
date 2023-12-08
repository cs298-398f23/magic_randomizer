from flask import Flask
from flask import render_template
from pymongo.mongo_client import MongoClient
from flask import request
from bson import json_util
import json
from deck import Deck
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required

def create_app():
    app = Flask(__name__)

    app.config.from_object('config')
    app.secret_key = app.config["SECRET_KEY"]

    mongoClient = MongoClient("mongodb://mongo:27017")

    users = {'admin': {'password': 'admin'}}

    class User(UserMixin):
        pass

    login_manager = LoginManager()
    login_manager.init_app(app)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/save", methods=["POST"])
    def save():
        data = request.get_data().decode("utf-8")
        data = json.loads(data)
        deck = Deck(data["name"], text=data["deck_list"])
        try:
            possible_duplicates = json.loads(json_util.dumps(mongoClient.magic_randomizer.decks.find({"name": deck.name})))
            if len(possible_duplicates) > 0:
                return "Deck already exists!", 400
            
            mongoClient.magic_randomizer.decks.insert_one(deck.get_json()) # collection.deeper_collection.insert_one(document)
            return "Deck Added successfully!", 200
        except Exception as e:
            result = e
            return str(result), 500

    @app.route("/load", methods=["GET"])
    def load():
        deck = mongoClient.magic_randomizer.decks.find({"name": request.args.get("name")})

        data = json.loads(json_util.dumps(deck))
        return data, 200

    @app.route("/random",methods=["GET"])
    def random():
        deck = Deck(generate=True, colors=request.args.get("colors").split(","))
        return str(deck), 200
    
    @login_manager.user_loader
    def user_loader(username):
        if username not in users:
            return

        user = User()
        user.id = username
        return user

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            if request.form['password'] == users[username]['password']:
                user = User()
                user.id = username
                login_user(user)
                data = {"username": username}
                data = json.loads(json_util.dumps(data))
                return data["username"], 200  # Return only the username to the client
        
        return 'Bad login', 401
    
    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return 'Logged out'

    return app

def launch():
    return create_app()
