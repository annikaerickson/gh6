# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import url_for, redirect, render_template, flash, g, session, request
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, lm, db
from forms import ExampleForm, LoginForm
from models import OrganizationUser, HomelessUser, HelpfulUser, CareProviderRating

@app.route('/')
def index():
	return render_template('index.html')

# Helpful
@app.route('/dashboard/helpful')
def helpfulDashboard():
	if not session.has_key("helpfulEmail"):
		return redirect('login/helpful')
	return render_template('helpful/helpful_dashboard.html.j2')

@app.route('/register/helpful', methods=["GET", "POST"])
def helpfulRegister():
	if request.method == "POST":
		# Get form data
		password = request.form.get('password', None)
		firstname = request.form.get('firstname', None)
		lastname = request.form.get('lastname', None)
		email = request.form.get('email', None)

		# User Exists
		query = HelpfulUser.query.filter_by(email=email, password=password).first()
		if (query):
			flash('User already exists!')
			return redirect('login/helpful')

		# add new user
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
		query = HelpfulUser.query.filter_by(email=email, password=password).first()
		if (query):
			session['helpfulEmail'] = email
			return redirect('dashboard/helpful')
		else:
			flash('Incorrect login!')
			return render_template('helpful/helpful_login.html.j2')
	else:
		if not session.has_key("helpfulEmail"):
			return redirect('dashboard/helpful')
		return render_template('helpful/helpful_login.html.j2')

# Homeless
@app.route('/dashboard/homeless')
def homelessDashboard():
	if not session.has_key("homelessEmail"):
		return redirect('login/homeless')
	return render_template('homeless/homeless_dashboard.html.j2')

@app.route('/register/homeless', methods=["GET", "POST"])
def homelessRegister():
	if request.method == "POST":
		# Get form data
		password = request.form.get('password', None)
		firstname = request.form.get('firstname', None)
		lastname = request.form.get('lastname', None)
		email = request.form.get('email', None)

		# User Exists
		query = HomelessUser.query.filter_by(email=email, password=password).first()
		if (query):
			flash('User already exists!')
			return redirect('login/homeless')

		# add new user
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
		query = HomelessUser.query.filter_by(email=email, password=password).first()
		if (query):
			session['homelessEmail'] = email
			return redirect('dashboard/homeless')
		else:
			flash('Incorrect login!')
			return render_template('homeless/homeless_login.html.j2')
	else:
		if not session.has_key("homelessEmail"):
			return redirect('dashboard/homeless')

		return render_template('homeless/homeless_login.html.j2')

# Ratings
@app.route('/rateCareProvider', methods=["GET", "POST"])
def rateCareProvider():
	if request.method == "POST":
		placeName = request.form.get('placeName', None)
		rating = request.form.get('rating', None)
		description = request.form.get('description', None)

		newRating = CareProviderRating(rating, placeName, description)
		db.session.add(newRating)
		db.session.commit()
		return redirect('/ratings')

	else:
		return render_template('homeless/homeless_rating.html.j2')

# Ratings
@app.route('/ratings')
def viewRatings():
	ratings = CareProviderRating.query.all()
	return render_template('homeless/ratings.html.j2', ratings = ratings)

# Care Provider
@app.route('/dashboard/careprovider')
def careproviderDashboard():
	if not session.has_key("careproviderEmail"):
		return redirect('login/careprovider')
	clients = HomelessUser.query.all()
	return render_template('careprovider/careprovider_dashboard.html.j2', clients=clients)

@app.route('/register/careprovider', methods=["GET", "POST"])
def careproviderRegister():
	if request.method == "POST":
		# Get form data
		password = request.form.get('password', None)
		firstname = request.form.get('firstname', None)
		lastname = request.form.get('lastname', None)
		email = request.form.get('email', None)

		# User Exists
		query = OrganizationUser.query.filter_by(email=email, password=password).first()
		if (query):
			flash('User already exists!')
			return redirect('login/careprovider')

		# add new user
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
			session['careproviderEmail'] = email
			return redirect('dashboard/careprovider')
		else:
			flash('Incorrect login!')
			return render_template('careprovider/careprovider_login.html.j2')
		# careproviderDashboard()
	else:
		if not session.has_key("careproviderEmail"):
			return redirect('dashboard/careprovider')
		return render_template('careprovider/careprovider_login.html.j2')

@app.route('/careprovider/careprovider_review', methods=["GET", "POST"])
def careproviderReviewLogin():
	return render_template('careprovider/careprovider_dashboard_review.html.j2')

@app.route("/testlist")
def listCareProviders():
	helpfuls = HelpfulUser.query.all()
	homelesses = HomelessUser.query.all()
	organizations = OrganizationUser.query.all()
	return render_template("test.html", helpfuls = helpfuls, homelesses = homelesses, organizations = organizations)

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
