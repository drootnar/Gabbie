from app import db


class Question(db.Model):
    __tablename__ = 'questions'
    '''Status: created, answered, rejected'''

    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.String(), nullable=False)
    room_id = db.Column(db.Integer(), db.ForeignKey(u'rooms.id'), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey(u'users.id'), nullable=False)
    status = db.Column(db.String(), nullable=False, default=u'created')
    room = db.relationship("Room", foreign_keys='Question.room_id')
    user = db.relationship("User", foreign_keys='Question.user_id')

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
