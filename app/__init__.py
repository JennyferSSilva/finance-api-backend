from flask import Flask
from app.config import Config
from app.extensions import db, jwt


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    from app.routes.auth_routes import auth_bp
    from app.routes.expense_routes import expense_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(expense_bp)

    return app
