import os
from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from starter_code.db import db


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'ryan123'

    api = Api(app)

    # JWT setup
    app.config['JWT_SECRET_KEY'] = 'ryan123'
    app.config['JWT_TOKEN_LOCATION'] = ['headers']
    app.config['JWT_HEADER_TYPE'] = 'Bearer'
    jwt = JWTManager(app)

    db.init_app(app)

    # Ensure DB resets every run, even with Flask reloader
    with app.app_context():
        db.drop_all()
        db.create_all()
        print("✅ Database reset complete")

    # Imports (AFTER db.init_app)
    from starter_code.resources.item import Item, ItemList
    from starter_code.resources.store import Store, StoreList
    from starter_code.resources.user import UserRegister
    from starter_code.resources.auth import Auth

    api.add_resource(Store, '/store/<string:name>')
    api.add_resource(Item, '/item/<string:name>')
    api.add_resource(ItemList, '/items')
    api.add_resource(StoreList, '/stores')
    api.add_resource(UserRegister, '/register')
    api.add_resource(Auth, '/auth')

    @app.errorhandler(401)
    @app.errorhandler(422)
    def handle_auth_error(err):
        return jsonify({'message': 'Could not authorize. Did you include a valid Authorization header?'}), 401

    return app


app = create_app()

if __name__ == '__main__':
    # Disable the reloader so the DB reset runs once per real start
    app.run(port=5000, use_reloader=False)
