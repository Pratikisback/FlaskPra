import pymongo
from flask import Flask
from flask_restful import Api
from pymongo import MongoClient
from flask_pymongo import PyMongo
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['MONGO_URI'] ="mongodb://localhost:27017/"
app.config["JWT_SECRET_KEY"] = "GBVFUYFYGY6556568FGYUF"
mongo = PyMongo(app)
api = Api(app)


app_jwt = JWTManager(app)
app_jwt.init_app(app)
