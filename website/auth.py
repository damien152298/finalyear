from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Courses
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)



@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/studentsignup', methods=['GET', 'POST'])
def studentsignup():
    if request.method == 'POST':
        email = request.form.get('email')
        usertype = request.form.get('usertype')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        aboutuni = request.form.get('aboutuni')
        instituteimg = request.form.get('instituteimg')
        institutelogo = request.form.get('institutelogo')
        maths = request.form.get('maths')
        english = request.form.get('english')
        maltese = request.form.get('maltese')
        computer_studies = request.form.get('computer_studies')
        biology = request.form.get('biology')
        physics = request.form.get('physics')
        chemistry = request.form.get('chemistry')
        italian = request.form.get('italian')
        french = request.form.get('french')
        home_economics = request.form.get('home_economics')
        accounts = request.form.get('accounts')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 7:
            flash('Email must be greater than 7 characters.', category='error')
        elif '@' not in email:
            flash('Email entered is not valid.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, usertype=usertype, first_name=first_name, aboutuni=aboutuni, 
            instituteimg = instituteimg, institutelogo=institutelogo,maths=maths, english=english, chemistry=chemistry, accounts=accounts, italian=italian, french=french, home_economics=home_economics, maltese=maltese,computer_studies=computer_studies,biology=biology,physics=physics, password=generate_password_hash(
            password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("studentsignup.html", user=current_user)

@auth.route('/adminsignup', methods=['GET', 'POST'])
def adminsignup():
    if request.method == 'POST':
        email = request.form.get('email')
        usertype = request.form.get('usertype')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        aboutuni = request.form.get('aboutuni')
        instituteimg = request.form.get('instituteimg')
        institutelogo = request.form.get('institutelogo')
        maths = request.form.get('maths')
        english = request.form.get('english')
        maltese = request.form.get('maltese')
        computer_studies = request.form.get('computer_studies')
        biology = request.form.get('biology')
        physics = request.form.get('physics')
        chemistry = request.form.get('chemistry')
        italian = request.form.get('italian')
        french = request.form.get('french')
        home_economics = request.form.get('home_economics')
        accounts = request.form.get('accounts')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 7:
            flash('Email must be greater than 7 characters.', category='error')
        elif '@' not in email:
            flash('Email entered is not valid.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, usertype=usertype, first_name=first_name, aboutuni=aboutuni, instituteimg = instituteimg, institutelogo=institutelogo,maths=maths, english=english, chemistry=chemistry, accounts=accounts, italian=italian, french=french, home_economics=home_economics, maltese=maltese,computer_studies=computer_studies,biology=biology,physics=physics, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("adminsignup.html", user=current_user)