from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
	logout_user()
	flash("Successfully Logged Out" , category='success')
	return redirect(url_for('auth.login'))





@auth.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']

		user = User.query.filter_by(email=email).first()
		if user:
			if check_password_hash(user.password, password):
				flash("Logged in Successfully", category='success')
				login_user(user, remember=True)
				return redirect(url_for('views.homepage'))
			else:
				flash("Incorrect Password, Try Again", category='error')
		else:
			flash("User does not exist: Sign Up For An Account", category='error')
			return redirect(url_for('auth.sign_up'))
	
	return render_template('login.html', user=current_user)







@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
	if request.method == 'POST':
		email = request.form['email']
		first_name = request.form['first_name']
		password1 = request.form['password1']
		password2 = request.form['password2']

		if len(email) < 4:
			flash('Email is invalid', category='error')
		elif len(first_name) < 4:
			flash("Username is too short", category='error')
		elif password1 != password2:
			flash('Passwords do not match', category= 'error')   
		else:
			new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
			db.session.add(new_user)
			try:
				db.session.commit()
			except:
				db.session.rollback
				flash('Email already in use', category='error')
				return render_template("sign_up.html", user=current_user)

			flash(f'Account created: Welcome {first_name}!', category='success')
			login_user(new_user)
			return redirect(url_for('views.homepage'))


	return render_template("sign_up.html", user=current_user) 

