import os
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from flask import abort

from models.room import Room
from models.user import User
from models.question import Question

from marshmallow import Schema, fields


def check_room_type(element):
    if element == u'qa' or element == u'place':
        return True
    return False


class RoomSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)
    major = fields.Integer(required=True)
    minor = fields.Integer(required=True)
    speaker_name = fields.Str(required=True)
    start_date = fields.DateTime(required=True)
    end_date = fields.DateTime(required=True)
    type = fields.Str(required=True, validate=check_room_type)


def user_exist(user_id):
    engine = create_engine(os.environ['DATABASE_URL'], echo=False)
    db = scoped_session(sessionmaker(
        autocommit=False, autoflush=False, bind=engine))
    result = db.query(User).filter(User.id == user_id).first()
    if result:
        return True
    return False


def room_exist(room_id):
    engine = create_engine(os.environ['DATABASE_URL'], echo=False)
    db = scoped_session(sessionmaker(
        autocommit=False, autoflush=False, bind=engine))
    result = db.query(Room).filter(Room.id == room_id).first()
    if result:
        return True
    return False


class MessageSchema(Schema):
    user_id = fields.Integer(required=True, validate=user_exist)
    room_id = fields.Integer(required=True, validate=room_exist)
    text = fields.Str(required=True)


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

    def get_detail(self, room_id):
        return self.db.session.query(Room)\
            .filter(Room.id == room_id).first()

    def add_message(self, room_id, data):
        schema = MessageSchema()
        result = schema.load(data)
        if result.errors:
            abort(400, result.errors)
        question = Question(result.data)
        self.db.session.add(question)
        self.db.session.commit()
        return question

    def list_messages(self, room_id, filters):
        messages = self.db.session.query(Question)\
            .filter(Question.room_id == room_id)
        if 'status' in filters:
            if filters['status'] in ['created', 'answered', 'rejected']:
                messages = messages.filter(Question.status == filters['status'])
        if 'user_id' in filters:
            messages = messages.filter(Question.user_id == filters['user_id'])
        messages = messages.order_by(Question.created_at.desc())
        return messages


class UserSchema(Schema):
    username = fields.Str(required=True)


class UserService(object):
    def __init__(self, db):
        self.db = db

    def get_all(self):
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

    def get(self, user_id):
        return self.db.session.query(User)\
            .filter(User.id == user_id).first()
