from models.room import Room

from marshmallow import Schema, fields


class RoomSchema(Schema):
    id = fields.Integer()
    name = fields.Str()
    major = fields.Integer()
    minor = fields.Integer()
    speaker_name = fields.Str()
    start_date = fields.DateTime()
    end_date = fields.DateTime()
    type = fields.Str()


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
            return None
        room = Room(result.data)
        self.db.session.add(room)
        self.db.session.commit()
        return room
