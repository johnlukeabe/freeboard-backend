# Common
from flask import request, jsonify, json

# Private
from db import models

class User():
    @staticmethod
    def get():
        result = models.User.query.all()
        return jsonify([e.serialize for e in result]), 200

    @staticmethod
    def post():
        data = {'name':'Abraham Sohn', 'email': 'jsson98@gmail.com'}
        return jsonify(data), 200


