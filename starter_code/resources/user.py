from flask_restful import Resource, reqparse
from starter_code.models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help="This field cannot be blank.",
        location='json'
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="This field cannot be blank.",
        location='json'
    )

    def post(self):
        try:
            data = UserRegister.parser.parse_args()
            print("DEBUG DATA:", data)

            if UserModel.find_by_username(data['username']):
                return {'message': "A user with that username already exists."}, 400

            user = UserModel(**data)
            user.save_to_db()
            return {"message": "User created successfully."}, 201

        except Exception as e:
            import traceback
            traceback.print_exc()
            return {"error": str(e)}, 500
