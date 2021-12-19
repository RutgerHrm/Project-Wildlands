# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_login import UserMixin
from sqlalchemy import Binary, Column, Integer, String
from app import db, login_manager
from app.base.util import hash_pass

class User(db.Model, UserMixin):

    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(Binary)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == 'password':
                value = hash_pass( value ) # we need bytes here (not plain str)
                
            setattr(self, property, value)

    def __repr__(self):
        return str(self.username)


@login_manager.user_loader
def user_loader(id):
    return User.query.filter_by(id=id).first()

@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = User.query.filter_by(username=username).first()
    return user if user else None


class Dier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    voornaam = db.Column(db.String(45), nullable=False)
    achternaam = db.Column(db.String(45), nullable=False)
    soort = db.Column(db.String(45), nullable=False)
    kleur = db.Column(db.String(45), nullable=False)
    geslacht = db.Column(db.String(45), nullable=False)
    leeftijd = db.Column(db.Integer, nullable=False)
    geboortedatum = voornaam = db.Column(db.Date, nullable=False)
    levensverwachting = db.Column(db.Integer, nullable=False)
    gebied_id = db.Column(db.Integer, db.ForeignKey('gebied.id'), nullable=False)
    opnamens_id = db.Column(db.Integer, db.ForeignKey('opnamens.id'), nullable=False)

    def __repr__(self):
        return f"Dier('{self.voornaam}', '{self.achternaam}', '{self.soort}', '{self.kleur}', '{self.geslacht}', '{self.leeftijd}', '{self.geboortedatum}', '{self.levensverwachting}')"

class Gebied(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.String(45), nullable=False)
    soort = db.Column(db.String(45), nullable=False)
    grootte = db.Column(db.String(45), nullable=False)
    ontsnappingen = db.Column(db.Integer, nullable=False)


class Opnamen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.String(45), nullable=False)
    kwaliteit = db.Column(db.String(45), nullable=False)
    duur = db.Column(db.String(45), nullable=False)
    current_time = db.Column(db.Time, nullable=False)