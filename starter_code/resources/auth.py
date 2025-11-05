# FILE: starter_code/resources/auth.py
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from starter_code.models.user import UserModel


class Auth(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help='Username cannot be blank'
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help='Password cannot be blank'
    )

    def post(self):
        data = Auth.parser.parse_args()
        user = UserModel.find_by_username(data['username'])

        # --- DEBUG LOG ---
        print("AUTH DEBUG:", data,
              "| FOUND:", user.username if user else None,
              "| PASS:", user.password if user else None)

        if user and user.password == data['password']:
            # ✅ Convert user.id to string for JWT compatibility
            access_token = create_access_token(identity=str(user.id))
            print("AUTH SUCCESS: Token created for user", user.username)
            return {'access_token': access_token}, 200

        print("AUTH FAIL: Invalid credentials for", data['username'])
        return {'message': 'Invalid credentials'}, 401
