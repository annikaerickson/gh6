# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask.ext.wtf import Form, TextField, TextAreaField, DateTimeField, PasswordField
from flask.ext.wtf import Required

class ExampleForm(Form):
	title = TextField(u'Title', validators = [Required()])
	content = TextAreaField(u'Content')
	date = DateTimeField(u'Date', format='%d/%m/%Y %H:%M')
	#recaptcha = RecaptchaField(u'Recaptcha')

class LoginForm(Form):
	user = TextField(u'Username', validators = [Required()])
	password = PasswordField(u'Password', validators = [Required()])
