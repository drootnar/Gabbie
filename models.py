from app import db
from sqlalchemy import FetchedValue, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSON


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    result_all = db.Column(JSON)
    result_no_stop_words = db.Column(JSON)

    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return u'<id {}>'.format(self.id)


class Room(db.Model):
    __tablename__ = 'rooms'

    id = db.Column(db.Integer(), primary_key=True)
    major = db.Column(db.Integer(), nullable=False)
    minor = db.Column(db.Integer(), nullable=False)
    name = db.Column(db.String())
    speaker_name = db.Column(db.String(), nullable=True)
    start_date = db.Column(db.DateTime(), nullable=False)
    end_date = db.Column(db.DateTime(), nullable=False)
    type = db.Column(db.String(), nullable=False, default=u'qa')
    photo = db.Column(db.String(), nullable=True)
    created_at = db.Column(
        db.DateTime(), nullable=False, server_default=text('now()'))
    updated_at = db.Column(
        db.DateTime(), nullable=True, server_onupdate=FetchedValue())

    def __repr__(self):
        return u'<{}-{} {}>'.format(self.major, self.minor, self.name)

    def __init__(self, data):
        self.major = data.get('major', 0)
        self.minor = data.get('minor', 0)
        self.name = data.get('name', 'unknow room')
        self.start_date = data.get('start_date')
        self.end_date = data.get('end_date')
        self.type = data.get('type', 'qa')
        self.photo = data.get('photo')
        self.speaker_name = data.get('speaker_name')

    def json(self, verbose=False):
        result = {
            'major': self.major,
            'minor': self.minor,
            'name': self.name,
            'speaker_name': self.speaker_name,
            'photo': self.photo,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'type': self.type,
        }
        if verbose:
            result['created_at'] = self.created_at
            result['updated_at'] = self.updated_at
        return result


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), nullable=False)
    password = db.Column(db.Unicode(256), nullable=True, default=u'')
    photo = db.Column(db.String(), nullable=True)
    created_at = db.Column(
        db.DateTime(), nullable=False, server_default=text('now()'))
    updated_at = db.Column(
        db.DateTime(), nullable=True, server_onupdate=FetchedValue())

    def __repr__(self):
        return u'<{} {}>'.format(self.id, self.username)

    def __init__(self, data):
        self.username = data.get('username')
        self.photo = data.get('photo')

    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'photo': self.photo,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }


class Question(db.Model):
    __tablename__ = 'questions'
    '''Status: created, answered, rejected'''

    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.String(), nullable=False)
    room_id = db.Column(db.Integer(), db.ForeignKey(u'rooms.id'), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey(u'users.id'), nullable=False)
    status = db.Column(db.String(), nullable=False, default=u'created')
    room = relationship("Room", foreign_keys='Question.room_id')
    user = relationship("User", foreign_keys='Question.user_id')

    def __repr__(self):
        return u'<Question {} {}>'.format(self.room_id, self.user_id)

    def __init__(self, data):
        self.text = data.get('text')
        self.room_id = data.get('room_id')
        self.user_id = data.get('user_id')
        self.status = u'created'

    def json(self):
        return {
            'id': self.id,
            'text': self.text,
            'room_id': self.room.__json__(),
            'user_id': self.user.__json__(),
            'status': self.status,
        }
