import datetime
from .controller import *
from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from flask import Blueprint
from doki import mongo, api
from doki.master.controller import find_user, reg_user, delUser
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager



Calculatorr = Blueprint('calc', __name__)

class Calculate:
    def mul(self, a, b):
        c = int(a * b)
        return c

    def add(self, a, b):
        c = int(a + b)
        return c

    def div(self, a, b):
        c = (a / b)

        return c

    def sub(self, a, b):
        c = int(a - b)
        return c


class Calculate1(Resource):
    def post(self):
        Dataa = request.get_json()
        num1 = Dataa.get('first')
        num2 = Dataa.get('second')
        obj = Calculate()
        mulval = obj.mul(num1, num2)
        subval = obj.sub(num1, num2)
        addval = obj.add(num1, num2)
        divval = obj.div(num1, num2)
        res = regcal(num1, num2, mulval,subval,addval,divval)
        if res:
            return make_response(jsonify({
                "a": num1,
                "b": num2,
                "resultM": mulval,
                "resultA": addval,
                "subvalS": subval,
                "divvalD": divval
            }))
        else:
            return make_response(jsonify({"message": "Error "}))


api.add_resource(Calculate1, '/calc')

