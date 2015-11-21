from flask import abort

from models.room import Room

from marshmallow import Schema, fields


class RoomSchema(Schema):
    name = fields.Str(required=True)
    major = fields.Integer(required=True)
    minor = fields.Integer(required=True)
    speaker_name = fields.Str(required=True)
    start_date = fields.DateTime(required=True)
    end_date = fields.DateTime(required=True)
    type = fields.Str(required=True)


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
