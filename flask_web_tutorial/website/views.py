from flask import Blueprint, render_template, request, flash
from flask_login import current_user, login_required
from .models import Message
from . import db




views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def homepage():
	if request.method =='POST':
		message = request.form['message']
		if len(message) < 1:
			flash("Message Too Short", category='error')
		else:
		
			new_message = Message(data=message, user_id = current_user.id)
			db.session.add(new_message)

		try:
			db.session.commit()
		except:
			db.session.rollback()
			return render_template("home.html", user=current_user)
			
		flash("Message Added", category='success')

	return render_template("home.html", user=current_user)
