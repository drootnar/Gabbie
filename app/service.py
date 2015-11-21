from flask import abort

from models.room import Room
from models.user import User

from marshmallow import Schema, fields


def check_room_type(element):
    if element == u'qa' or element == u'place':
        return True
    return False


class RoomSchema(Schema):
    name = fields.Str(required=True)
    major = fields.Integer(required=True)
    minor = fields.Integer(required=True)
    speaker_name = fields.Str(required=True)
    start_date = fields.DateTime(required=True)
    end_date = fields.DateTime(required=True)
    type = fields.Str(required=True, validate=check_room_type)


class RoomService(object):
    def __init__(self, db):
        self.db = db

    def get(self, data):
        major = data.get('major')
        minor = data.get('minor')
        query = self.db.session.query(Room)
        if major and minor:
            query = query\
                .filter(Room.major == major)\
                .filter(Room.minor == minor)
        return query

    def add(self, data):
        schema = RoomSchema()
        result = schema.load(data)
        if result.errors:
            abort(400, result.errors)
        room = Room(result.data)
        self.db.session.add(room)
        self.db.session.commit()
        return room


class UserSchema(Schema):
    username = fields.Str(required=True)


class UserService(object):
    def __init__(self, db):
        self.db = db

    def get(self, data):
        query = self.db.session.query(User)
        return query

    def add(self, data):
        schema = UserSchema()
        result = schema.load(data)
        if result.errors:
            abort(400, result.errors)
        user = User(result.data)
        self.db.session.add(user)
        self.db.session.commit()
        return user
