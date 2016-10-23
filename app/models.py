# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from app import db

class OrganizationUser(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    password = db.Column(db.String(500))
    firstname = db.Column(db.String(500))
    lastname = db.Column(db.String(500))
    email = db.Column(db.String(120), unique = True)
    # posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')

    def __init__(self, password, firstname, lastname, email):
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def is_authenticated(self):
        return True

    def get_id(self):
        return unicode(self.id)

class HelpfulUser(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True)
    password = db.Column(db.String(500))
    firstname = db.Column(db.String(500))
    lastname = db.Column(db.String(500))
    email = db.Column(db.String(120), unique = True)
    # posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')

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


class HomelessUser(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True)
    personalID = db.Column(db.String(64), unique = True)
    password = db.Column(db.String(500))
    firstname = db.Column(db.String(500))
    lastname = db.Column(db.String(500))
    email = db.Column(db.String(120), unique = True)
    age = db.Column(db.Integer())
    gender = db.Column(db.String(20))
    lastvisit = db.Column(db.DateTime())
    lastupdate = db.Column(db.DateTime())


    # posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')

    def __init__(self, password, firstname, lastname, email):
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def is_authenticated(self):
        return True

    def get_id(self):
        return unicode(self.id)

class CareProviderRating(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    rating = db.Column(db.Integer())
    placeName = db.Column(db.String(250))
    description = db.Column(db.String(3000))


    # posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')

    def __init__(self, rating, placeName, description):
        self.rating = rating
        self.placeName = placeName
        self.description = description

    def is_authenticated(self):
        return True

    def get_id(self):
        return unicode(self.id)
