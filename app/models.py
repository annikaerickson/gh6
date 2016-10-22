# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from app import db

class ModelExample(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(250))
	content = db.Column(db.Text)
	date = db.Column(db.DateTime)


class OrganizationUser(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    password = db.Column(db.String(500))
    firstname = db.Column(db.String(500))
    lastname = db.Column(db.String(500))
    email = db.Column(db.String(120), unique = True)
    # posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')

# class OrganizationUser(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     username = db.Column(db.String(64), unique = True)
#     password = db.Column(db.String(500))
#     firstname = db.Column(db.String(500))
#     lastname = db.Column(db.String(500))
#     email = db.Column(db.String(120), unique = True)
#     # posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')

    def __init__(self, password, firstname, lastname, email):
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.email = email


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

db.create_all()
db.session.commit()