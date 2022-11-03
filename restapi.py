from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList

app = Flask (__name__)
app.secret_key = 'kris' # This is used to encrypt the session cookie
api = Api (app)

jwt = JWT (app, authenticate, identity) # /auth


api.add_resource (Item, '/item/<string:name>')
api.add_resource (ItemList, '/items')
api.add_resource (UserRegister, '/register')

if __name__ == '__main__':
    app.run (port=1982, debug=True)
