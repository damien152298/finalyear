from django.shortcuts import redirect, render
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Courses, User
from .import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():

    return render_template("home.html", user=current_user)


@views.route('/addcourse', methods=['GET', 'POST'])
def addcourse():

    if request.method == 'POST':
        courseName = request.form.get('courseName')
        institute = request.form.get('institute')
        neededSubject = request.form.get('neededSubject')
        about = request.form.get('about')
        courseimg = request.form.get('courseimg')
        modules = request.form.get('modules')
        careers = request.form.get('careers')
        new_course = Courses(courseName=courseName, institute=institute, neededSubject=neededSubject, about=about, courseimg=courseimg, 
        modules=modules, careers=careers, user_id=current_user.id)
        db.session.add(new_course)
        db.session.commit()
        flash('Course added!', category="success")
  
 
    return render_template("addcourse.html", user=current_user)


 

@views.route('/myaccount')
def myaccount():
    our_courses = Courses.query.order_by(Courses.courseName)
    q = request.args.get('q')
    if q:
        our_courses = Courses.query.filter(Courses.courseName.contains(q) |
        Courses.institute.contains(q)  | Courses.neededSubject.contains(q))
    else:
        our_courses = Courses.query.all()
    return render_template("myaccount.html", user=current_user, our_courses=our_courses)

@views.route('/courses')
def courses():
    our_courses = Courses.query.order_by(Courses.courseName)
    marks = User
    q = request.args.get('q')
    if q:
        our_courses = Courses.query.filter(Courses.courseName.contains(q) |
        Courses.institute.contains(q) | Courses.neededSubject.contains(q))
    else:
        our_courses = Courses.query.all()
    return render_template("courses.html", our_courses=our_courses, user=current_user, marks=marks)


@views.route('/update/<int:id>', methods=["POST", "GET"])
def update(id):
    course_to_update = Courses.query.get_or_404(id)
    if request.method == 'POST':
        course_to_update.courseName = request.form['courseName']
        course_to_update.neededSubject = request.form['neededSubject']
        course_to_update.about = request.form['about']
        course_to_update.modules = request.form['modules']
        course_to_update.careers = request.form['careers']
        course_to_update.courseimg = request.form['courseimg']
        try:
            db.session.commit()
            return redirect('/myaccount')
        except:
            return render_template('home.html')
    else:
        return render_template('update.html', course_to_update=course_to_update)

@views.route('/updateuser/<int:id>', methods=["POST", "GET"])
def updateuser(id):
    user_to_update = User.query.get_or_404(id)
    if request.method == 'POST':
        user_to_update.first_name = request.form['first_name']
        try:
            db.session.commit()
            return redirect('/myaccount')
        except:
            return render_template('home.html')
    else:
        return render_template('updateuser.html', user_to_update=user_to_update)

@views.route('/updateuni/<int:id>', methods=["POST", "GET"])
def updateuni(id):
    uni_to_update = User.query.get_or_404(id)
    if request.method == 'POST':
        uni_to_update.first_name = request.form['first_name']
        uni_to_update.aboutuni = request.form['aboutuni']
        uni_to_update.instituteimg = request.form['instituteimg']
        uni_to_update.institutelogo = request.form['institutelogo']
        try:
            db.session.commit()
            return redirect('/myaccount')
        except:
            return render_template('home.html')
    else:
        return render_template('updateuni.html', uni_to_update=uni_to_update)

@views.route('/updatemarks/<int:id>', methods=["POST", "GET"])
def updatemarks(id):
    marks_to_update = User.query.get_or_404(id)
    if request.method == 'POST':
        marks_to_update.maths = request.form['maths']
        marks_to_update.english = request.form['english']
        marks_to_update.maltese = request.form['maltese']
        marks_to_update.accounts = request.form['accounts']
        marks_to_update.computer_studies = request.form['computer_studies']
        marks_to_update.chemistry = request.form['chemistry']
        marks_to_update.biology = request.form['biology']
        marks_to_update.physics = request.form['physics']
        marks_to_update.italian = request.form['italian']
        marks_to_update.french = request.form['french']
        marks_to_update.home_economics = request.form['home_economics']
        try:
            db.session.commit()
            return redirect('/myaccount')
        except:
            return render_template('home.html')
    else:
        return render_template('updatemarks.html', marks_to_update=marks_to_update)


@views.route('/delete/<int:id>')
def delete(id):
    course_to_delete = Courses.query.get_or_404(id)

    try:
        db.session.delete(course_to_delete)
        db.session.commit()
        return redirect('/myaccount')

    except:
        return render_template('home.html')


@views.route('/course/<int:id>')
def course(id):
    course = Courses.query.get_or_404(id)
    return render_template('course.html', course=course)

@views.route('/institute/<int:id>')
def institute(id):
    institute = User.query.get_or_404(id)
    return render_template('institute.html', institute=institute)









        
        