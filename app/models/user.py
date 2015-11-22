from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), nullable=False)
    password = db.Column(db.Unicode(256), nullable=True, default=u'')
    photo = db.Column(db.String(), nullable=True)
    created_at = db.Column(
        db.DateTime(), nullable=False, server_default=db.text('now()'))
    updated_at = db.Column(
        db.DateTime(), nullable=True, server_onupdate=db.FetchedValue())

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)

    def __repr__(self):
        return u'<{} {}>'.format(self.id, self.username)

    def __init__(self, data):
        if data:
            self.username = data.get('username')
            self.photo = data.get('photo')

    def json(self, verbose=False):
        result = {
            'id': self.id,
            'username': self.username,
            'photo': self.photo,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
        if verbose:
            result['questions'] = [q.json() for q in self.questions.all()]
        return result
