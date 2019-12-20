# Common
from flask import Blueprint, request

# Private
from control.user import User

default = Blueprint('freeboard', __name__)

@default.route('/')
def root():
    return 'root'

@default.route('/user', methods=['GET', 'POST'])
def user():
    print(request)
    if request.method == 'GET':
        return User.get()
    elif request.method == 'POST':
        return User.post()

