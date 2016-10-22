# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import url_for, redirect, render_template, flash, g, session, request
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, lm
from forms import ExampleForm, LoginForm
from models import User

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/list/')
def posts():
	return render_template('list.html')

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

@app.route('/register/helpful')
def helpfulRegister():
	return render_template('helpful/helpful_register.html.j2')

@app.route('/login/helpful')
def helpfulLogin():
	return render_template('helpful/helpful_login.html.j2')

# Homeless
@app.route('/dashboard/homeless')
def homelessDashboard():
	return render_template('homeless/homeless_dashboard.html.j2')

@app.route('/register/homeless')
def homelessRegister():
	return render_template('homeless/homeless_register.html.j2')

@app.route('/login/homeless')
def homelessLogin():
	return render_template('homeless/homeless_login.html.j2')

# Care Provider
@app.route('/dashboard/careprovider')
def careproviderDashboard():
	return render_template('careprovider/careprovider_dashboard.html.j2')

@app.route('/register/careprovider')
def careproviderRegister():
	return render_template('careprovider/careprovider_register.html.j2')

@app.route('/login/careprovider')
def careproviderLogin():
	return render_template('careprovider/careprovider_login.html.j2')

# === User login methods ===

@app.before_request
def before_request():
    g.user = current_user

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/login/', methods = ['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        login_user(g.user)

    return render_template('login.html', 
        title = 'Sign In',
        form = form)

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
