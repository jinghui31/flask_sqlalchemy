from setting import db

class Role(db.Model):
    id = db.Column(db.Integer, nullable = False, primary_key = True, autoincrement = True)
    name = db.Column(db.String(16), nullable = False, server_default = '', unique = True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    id = db.Column(db.Integer, nullable = False, primary_key = True, autoincrement = True)
    username = db.Column(db.String(32), nullable = False, unique = True, server_default = '', index = True)
    role_id = db.Column(db.Integer, nullable = False, server_default = '0')

    def __init__(self, username, role_id):
        self.username = username
        self.role_id = role_id

    def __repr__(self):
        return '<User %r, Role id %r>' % (self.username, self.role_id)