from flask import Flask, Blueprint, render_template, url_for, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import Patient
from . import db

auth = Blueprint("health_auth", __name__)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('first') +" "+ request.form.get('last')
        email = request.form.get('useremail')
        pwd = request.form.get('userpass')

        patient = Patient.query.filter_by(email=email).first()
        if patient:
            return redirect(url_for('health_auth.signup'))
        
        new_patient = Patient(name=name, email=email, pwd=generate_password_hash(pwd, method="sha256"))
        db.session.add(new_patient)
        db.session.commit()

        return redirect(url_for('health_auth.login'))
    
    return render_template("signup.html")

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('useremail')
        pwd = request.form.get('userpass')
        remember = True if request.form.get('remember') else False

        patient = Patient.query.filter_by(email=email).first()
        if not patient or not check_password_hash(patient.pwd, pwd):
            return redirect(url_for('health_auth.login'))

        login_user(patient, remember=remember)
        return redirect(url_for('health_main.health'))

    return render_template("login.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('health_main.index'))