from app import db
from sqlalchemy import Integer


class Room(db.Model):
    __tablename__ = 'rooms'

    id = db.Column(Integer(), primary_key=True)
    major = db.Column(Integer(), nullable=False)
    minor = db.Column(Integer(), nullable=False)
    name = db.Column(db.String())
    speaker_name = db.Column(db.String(), nullable=True)
    start_date = db.Column(db.DateTime(), nullable=False)
    end_date = db.Column(db.DateTime(), nullable=False)
    type = db.Column(db.String(), nullable=False, default=u'qa')
    photo = db.Column(db.String(), nullable=True)
    created_at = db.Column(
        db.DateTime(), nullable=False, server_default=db.text('now()'))
    updated_at = db.Column(
        db.DateTime(), nullable=True, server_onupdate=db.FetchedValue())

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
