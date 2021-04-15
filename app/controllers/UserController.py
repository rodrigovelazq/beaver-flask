from flask import Blueprint, jsonify, request
from app import db
from app.models.User import User

mod = Blueprint('users', __name__, url_prefix='/users')


@mod.route('/', methods=['GET'])
def index():
    users = User.query.all()
    output = []
    for user in users:
        user_data = {}
        user_data['id'] = user.id
        user_data['username'] = user.username
        user_data['firstname'] = user.firstname
        user_data['lastname'] = user.lastname
        user_data['lastname'] = user.lastname
        output.append(user_data)
    return jsonify(output)


@mod.route('/<user_id>', methods=['GET'])
def show(user_id):
    user = User.query.get(user_id)
    return jsonify(user)

@mod.route('/', methods=['POST'])
def store():
    request_data = request.get_json()
    username = request_data['username']
    firstname = request_data['firstname']
    lastname = request_data['lastname']
    password = request_data['password']
    user = User(username=username, firstname=firstname, lastname=lastname, password=password)
    db.session.add(user)
    db.session.commit()

    return 'Ok'

@mod.route('/', methods=['PUT'])
def update():
    # request_data = request.get_json()
    # username = request_data['username']
    # firstname = request_data['firstname']
    # lastname = request_data['lastname']
    # password = request_data['password']
    # user = User(username=username, firstname=firstname, lastname=lastname, password=password)
    # db.session.add(user)
    # db.session.commit()

    return 'Ok'

@mod.route('/<user_id>', methods=['DELETE'])
def destroy(user_id):
    # request_data = request.get_json()
    # username = request_data['username']
    # firstname = request_data['firstname']
    # lastname = request_data['lastname']
    # password = request_data['password']
    # user = User(username=username, firstname=firstname, lastname=lastname, password=password)
    # db.session.add(user)
    # db.session.commit()

    return 'Ok'

@mod.route('/testdb')
def testdb():
    if db.session.query("1").from_statement("SELECT 1").all():
        return 'It workds.'
    else:
        return 'something is broken.'