# Stores functions defining Login, Logout, Sign up
# Try to get so it so that if password don't match, only remove password, don't refresh the whole page

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, logout_user, current_user, login_required

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=False)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('Email does not exist', category='error')
        
    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
    
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists', category='error')
        elif len(email) < 4:
            flash('Please enter a valid email address.', category='error')
        elif len(first_name) < 1:
            flash('First name must be greater than 1 character', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 7 characters.', category='error')
        elif password1.isupper() == True or password2.islower() == True:
            flash('Password must contain uppercase.', category='error')
        elif password1 != password2:
            flash('Password do not match', category='error')
        else:
            new_user = User(email=email,first_name=first_name, 
                            password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created', category='success')
            return redirect(url_for('views.home'))
    
    return render_template('sign_up.html', user=current_user)
