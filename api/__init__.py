from flask import Flask, config
from flask_restplus import Api
from flask_cors import CORS
import mongoengine

from config import Config as config


api = Api(
    title="Address Book CRUD APIs",
)

def register_extensions(app):
    # regsitering extensions
    api.init_app(app)
    CORS(app)

def db_init():
    try:
        mongoengine.connect(
            db=config.DB_NAME, 
            host=config.DB_HOST, 
            username=config.DB_USERNAME, 
            password=config.DB_PASSWORD, 
            authentication_source=config.DB_AUTHENTICATION_SOURCE
        )
    except Exception as e:
        print(e)

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(config)

    # register extensions
    register_extensions(app)

    # connecting to database
    db_init()

    from .address.routes import np as address_namespace

    api.add_namespace(address_namespace, path="/api/v1/address")

    return app






