import datetime
from doki import api
from flask import Flask, request, jsonify, make_response, Blueprint
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_restful import Resource, Api
from .controller import find_user, reg_user, delUser

bluemaster = Blueprint('form', __name__)


class Register(Resource):
    def post(self):

        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            return make_response(jsonify({"error": "username already exists"}), 409)
        existing_user = find_user(username)
        if existing_user:
            return make_response(jsonify({'error': "Username already exists"}), 409)

        new_user = {
            'username': username,
            'password': password
        }
        result = reg_user(new_user)
        if result:
            return make_response(
                jsonify({"message": "User registered successfully", 'user_id': str(result.inserted_id)}), 201)


class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        data.get('password')
        userinfo = find_user(username)
        usernamedb = userinfo.get("username")
        pwddb = userinfo.get("password")
        access_token = create_access_token(identity=username, expires_delta=datetime.timedelta(minutes=15))

        if pwddb == password and usernamedb == username:
            return make_response(
                jsonify({"message": "User logged in successfully",
                         "access_Token": access_token})

            )
        else:
            return make_response(jsonify({"message": "Invalid credentials"}))


class RemoveUser(Resource):
    @jwt_required
    def delete(self):
        data = request.get_json()
        username = data.get('username')
        print(username)
        password = data.get('password')
        data.get('password')
        userinfo = find_user(username)
        usernamedb = userinfo.get("username")
        pwddb = userinfo.get("password")

        if usernamedb is None:
            return jsonify({'message': 'user not found'})
        else:
            deletedUser = delUser(usernamedb)

        return make_response(jsonify({"Message": "user deleted successfully"}))


# class Update(Resource):
#     def post(self):
#         data = request.get_json()
#         username = data.get('username')


api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(RemoveUser, '/delete')
