from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    voornaam = StringField('Voornaam', validators=[DataRequired()])
    achternaam = StringField('Achternaam')
    soort = StringField('Soort', validators=[DataRequired()])
    kleur = StringField('Kleur', validators=[DataRequired()])
    geslacht = StringField('Geslacht', validators=[DataRequired()])
    leeftijd = IntegerField('Leeftijd', validators=[DataRequired()])
    geboortedatum = DateField('Geboortedatum', format='%Y-%m-%d')
    levensverwachting = IntegerField('Levensverwachting')
    gebied_id = IntegerField('ID Gebied', validators=[DataRequired()])
    opnamen_id = IntegerField('ID Opnamen', validators=[DataRequired()])
    submit = SubmitField('Post')


class PostForm2(FlaskForm):
    naam = StringField('Gebiedsnaam', validators=[DataRequired()])
    soort = StringField('Gebiedssoort', validators=[DataRequired()])
    grootte = IntegerField('Gebiedsgroote', validators=[DataRequired()])
    submit = SubmitField('Post')
