# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import url_for, redirect, render_template, flash, g, session, request
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, lm, db
from forms import ExampleForm, LoginForm
from models import OrganizationUser, HomelessUser, HelpfulUser

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/new/')
@login_required
def new():
	form = ExampleForm()
	return render_template('new.html', form=form)

@app.route('/save/', methods = ['GET','POST'])
@login_required
def save():
	form = ExampleForm()
	if form.validate_on_submit():
		print "salvando os dados:"
		print form.title.data
		print form.content.data
		print form.date.data
		flash('Dados salvos!')
	return render_template('new.html', form=form)

# Helpful
@app.route('/dashboard/helpful')
def helpfulDashboard():
	return render_template('helpful/helpful_dashboard.html.j2')

@app.route('/register/helpful', methods=["GET", "POST"])
def helpfulRegister():
	if request.method == "POST":
		password = request.form.get('password', None)
		firstname = request.form.get('firstname', None)
		lastname = request.form.get('lastname', None)
		email = request.form.get('email', None)
		newUser = HelpfulUser(password, firstname, lastname, email)
		db.session.add(newUser)
		db.session.commit()
		return render_template('helpful/helpful_login.html.j2')
	else:
		return render_template('helpful/helpful_register.html.j2')

@app.route('/login/helpful', methods=["GET", "POST"])
def helpfulLogin():
	if request.method == "POST":
		password = request.form.get('password', None)
		email = request.form.get('email', None)
		query = OrganizationUser.query.filter_by(email=email, password=password).first()
		if (query):
			return render_template('helpful/helpful_dashboard.html.j2')
		else:
			flash('Incorrect login!')
			return render_template('helpful/helpful_login.html.j2')
	else:
		return render_template('helpful/helpful_login.html.j2')

# Homeless
@app.route('/dashboard/homeless')
def homelessDashboard():
	return render_template('homeless/homeless_dashboard.html.j2')

@app.route('/register/homeless', methods=["GET", "POST"])
def homelessRegister():
	if request.method == "POST":
		password = request.form.get('password', None)
		firstname = request.form.get('firstname', None)
		lastname = request.form.get('lastname', None)
		email = request.form.get('email', None)
		newUser = HomelessUser(password, firstname, lastname, email)
		db.session.add(newUser)
		db.session.commit()
		return render_template('homeless/homeless_login.html.j2')
	else:
		return render_template('homeless/homeless_register.html.j2')

@app.route('/login/homeless', methods=["GET", "POST"])
def homelessLogin():
	if request.method == "POST":
		password = request.form.get('password', None)
		email = request.form.get('email', None)
		query = OrganizationUser.query.filter_by(email=email, password=password).first()
		if (query):
			return render_template('homeless/homeless_dashboard.html.j2')
		else:
			flash('Incorrect login!')
			return render_template('homeless/homeless_login.html.j2')
	else:
		return render_template('homeless/homeless_login.html.j2')

# Care Provider
@app.route('/dashboard/careprovider')
def careproviderDashboard():
	return render_template('careprovider/careprovider_dashboard.html.j2')

@app.route('/register/careprovider', methods=["GET", "POST"])
def careproviderRegister():
	if request.method == "POST":
		password = request.form.get('password', None)
		firstname = request.form.get('firstname', None)
		lastname = request.form.get('lastname', None)
		email = request.form.get('email', None)
		newUser = OrganizationUser(password, firstname, lastname, email)
		db.session.add(newUser)
		db.session.commit()
		return render_template('careprovider/careprovider_login.html.j2')
	else:
		return render_template('careprovider/careprovider_register.html.j2')

@app.route('/login/careprovider', methods=["GET", "POST"])
def careproviderLogin():
	if request.method == "POST":
		password = request.form.get('password', None)
		email = request.form.get('email', None)
		query = OrganizationUser.query.filter_by(email=email, password=password).first()
		if (query):
			return render_template('careprovider/careprovider_dashboard.html.j2')
		else:
			flash('Incorrect login!')
			return render_template('careprovider/careprovider_login.html.j2')
		# careproviderDashboard()
	else:
		return render_template('careprovider/careprovider_login.html.j2')

@app.route("/testlist")
def listCareProviders():
	orgs = HelpfulUser.query.all()
	return render_template("test.html", orgs = orgs)

# === User login methods ===

@app.before_request
def before_request():
    g.user = current_user

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods = ['GET', 'POST'])
def register():
	if request.method == "GET":
	    form = LoginForm()
	    return render_template('register.html', 
	        title = 'Sign In',
	        form = form)
	else: 
		# Get Data
		return ""

# ====================
