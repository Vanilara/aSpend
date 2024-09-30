from flask import Flask, request, render_template
from flask_session import Session
from blueprints import Blueprints
from config import Config


def create_app():
    def register_blueprints():
        for blueprint in Blueprints:
            app.register_blueprint(blueprint)
    app = Flask(__name__)
    app.config["SECRET_KEY"] = Config.Flask.SESSION_KEY
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)
    register_blueprints()
    return app

app = create_app()


@app.route('/')
@app.route('/summary')
def index():
    return render_template('pages/summary.html')

@app.route('/spends')
def spends():
    return render_template('pages/spends.html')