from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_ngrok import run_with_ngrok

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    run_with_ngrok(app)
    app.config['SECRET_KEY'] = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'health_auth.login'
    login_manager.init_app(app)

    from .models import Patient
    @login_manager.user_loader
    def load_user(user_id):
        return Patient.query.get(int(user_id))

    from .health_main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .health_auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app

db.create_all(app=create_app())
