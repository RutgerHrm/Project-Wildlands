from flask import render_template, redirect, url_for, flash, Blueprint, request, abort
from flask_login import login_required, current_user
from app import login_manager, db
from app.models import User, Dier, Gebied, Opnamen
from app.home.forms import PostForm, PostForm2
from jinja2 import TemplateNotFound
from datetime import date

dieren_blueprint = Blueprint('dieren_blueprint', __name__, url_prefix='',
                             template_folder='templates', static_folder='static')
verblijven_blueprint = Blueprint('verblijven_blueprint', __name__, url_prefix='',
                                 template_folder='templates', static_folder='static')
home_blueprint = Blueprint('home_blueprint', __name__, url_prefix='',
                           template_folder='templates', static_folder='static')
users_blueprint = Blueprint('users_blueprint', __name__, url_prefix='',
                             template_folder='templates', static_folder='static')


@home_blueprint.route('/index')
@login_required
def index():
    datum = date.today()
    return render_template('index.html', datum=datum)

# Database overzicht dieren


@dieren_blueprint.route("/dieren")
@login_required
def dieren():
    posts = Dier.query.all()
    return render_template('dieren.html', title='Dieren', posts=posts)

# Aanmaken Dieren


@dieren_blueprint.route("/dieren/dierencreate", methods=['GET', 'POST'])
@login_required
def dierencreate():
    form = PostForm()
    if form.validate_on_submit():
        dier = Dier(voornaam=form.voornaam.data, achternaam=form.achternaam.data, soort=form.soort.data, kleur=form.kleur.data, geslacht=form.geslacht.data,
                    leeftijd=form.leeftijd.data, geboortedatum=form.geboortedatum.data, levensverwachting=form.levensverwachting.data, gebied_id=form.gebied_id.data, opnamen_id=form.opnamen_id.data)
        db.session.add(dier)
        db.session.commit()
        flash('Het dier is toegevoegd aan de database!', 'success')
        return redirect(url_for('dieren_blueprint.dieren'))
    return render_template('dierencreate.html', title='Dieren Toevoegen', form=form, legend='Dieren Toevoegen')

# View van het dier


@dieren_blueprint.route("/dier/<int:dier_id>")
@login_required
def dier(dier_id):
    dier = Dier.query.get_or_404(dier_id)
    return render_template('dierenread.html', title=dier.voornaam, dier=dier)

# Gegevens van het Dier wijzigen


@dieren_blueprint.route("/dier/<int:dier_id>/edit", methods=['GET', 'POST'])
@login_required
def dierenedit(dier_id):
    dier = Dier.query.get_or_404(dier_id)
    form = PostForm()
    if form.validate_on_submit():
        dier.voornaam = form.voornaam.data
        dier.achternaam = form.achternaam.data
        dier.soort = form.soort.data
        dier.kleur = form.kleur.data
        dier.geslacht = form.leeftijd.data
        dier.geboortedatum = form.geboortedatum.data
        dier.levensverwachting = form.levensverwachting.data
        dier.gebied_id = form.gebied_id.data
        dier.opnamen_id = form.opnamen_id.data
        db.session.commit()
        flash('De gegevens van het dier is aangepast!', 'success')
        return redirect(url_for('dieren_blueprint.dier', dier_id=dier.id))
    elif request.method == 'GET':
        form.voornaam.data = dier.voornaam
        form.achternaam.data = dier.achternaam
        form.soort.data = dier.soort
        form.kleur.data = dier.kleur
        form.geslacht.data = dier.geslacht
        form.geboortedatum.data = dier.geboortedatum
        form.levensverwachting.data = dier.levensverwachting
        form.gebied_id.data = dier.gebied_id
        form.opnamen_id.data = dier.opnamen_id
    return render_template('dierencreate.html', title='Gegevens Bewerken', form=form, legend='Gegevens Bewerken')


# Dier verwijderen
@dieren_blueprint.route("dier/<int:dier_id>/delete", methods=['POST'])
@login_required
def dierendelete(dier_id):
    dier = Dier.query.get_or_404(dier_id)
    db.session.delete(dier)
    db.session.commit()
    flash('Het dier is verwijderd', 'success')
    return redirect(url_for('dieren_blueprint.dieren'))

# Database overzicht dieren

# verblijven


@verblijven_blueprint.route("/verblijven")
@login_required
def verblijven():
    posts = Gebied.query.all()
    return render_template('verblijven.html', title='verblijven', posts=posts)

# Aanmaken verblijven


@verblijven_blueprint.route("/verblijven/verblijvencreate", methods=['GET', 'POST'])
@login_required
def verblijvencreate():
    form = PostForm2()
    if form.validate_on_submit():
        verblijf = Gebied(naam=form.naam.data,
                          soort=form.soort.data, grootte=form.grootte.data)
        db.session.add(verblijf)
        db.session.commit()
        flash('Het verblijf is toegevoegd aan de database!', 'success')
        return redirect(url_for('verblijven_blueprint.verblijven'))
    return render_template('verblijvencreate.html', title='Verblijf toevoegen', form=form, legend='Verblijf toevoegen')


# View van het verblijf


@verblijven_blueprint.route("/verblijf/<int:gebied_id>")
@login_required
def verblijf(gebied_id):
    verblijf = Gebied.query.get_or_404(gebied_id)
    return render_template('verblijvenread.html', title=verblijf.naam, gebied=verblijf)

# gegevens van een verblijf wijzigen


@verblijven_blueprint.route("/verblijf/<int:gebied_id>/edit", methods=['GET', 'POST'])
@login_required
def verblijvenedit(gebied_id):
    verblijf = Gebied.query.get_or_404(gebied_id)
    form = PostForm2()
    if form.validate_on_submit():
        verblijf.naam = form.naam.data
        verblijf.soort = form.soort.data
        verblijf.grootte = form.grootte.data
        db.session.commit()
        flash('De gegevens van het verblijf zijn aangepast!', 'success')
        return redirect(url_for('verblijven_blueprint.verblijven', gebied_id=Gebied.id))
    elif request.method == 'GET':
        form.naam.data = verblijf.naam
        form.soort.data = verblijf.soort
        form.grootte.data = verblijf.grootte
    return render_template('verblijvencreate.html', title='Gegevens Bewerken', form=form, legend='Gegevens Bewerken')

    # Verblijf verwijderen


@verblijven_blueprint.route("verblijf/<int:gebied_id>/delete", methods=['POST'])
@login_required
def verblijvendelete(gebied_id):
    verblijf = Gebied.query.get_or_404(gebied_id)
    db.session.delete(verblijf)
    db.session.commit()
    flash('Het verblijf is verwijderd', 'success')
    return redirect(url_for('verblijven_blueprint.verblijven'))

@verblijven_blueprint.route('/charts')
@login_required
def charts():
    posts = Gebied.query.all()
    serenga = Gebied.query.filter_by(naam='Serenga').first()
    jungola = Gebied.query.filter_by(naam='Jungola').first()
    animazia = Gebied.query.filter_by(naam='Animazia').first()
    nortica = Gebied.query.filter_by(naam='Nortica').first()
    return render_template('test.html', title='Chart', posts=posts, serenga=serenga, jungola=jungola, animazia=animazia, nortica=nortica)

#View van users

