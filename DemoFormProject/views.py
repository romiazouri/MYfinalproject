"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from DemoFormProject import app

from DemoFormProject.Models.LocalDatabaseRoutines import create_LocalDatabaseServiceRoutines

from datetime import datetime
from flask import render_template, redirect, request

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import json 
import requests

import io
import base64

from os import path

from flask   import Flask, render_template, flash, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms import TextField, TextAreaField, SubmitField, SelectField, DateField
from wtforms import ValidationError


from DemoFormProject.Models.QueryFormStructure import QueryFormStructure
from DemoFormProject.Models.QueryFormStructure import UserRegistrationFormStructure
from DemoFormProject.Models.QueryFormStructure import LoginFormStructure 

db_Functions = create_LocalDatabaseServiceRoutines() 



@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page"""
    return render_template(
        'contact.html',
        title='Contact page',
        year=datetime.now().year,
        message='Please contact me'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='Some about Hurricanes',
        year=datetime.now().year,
        message='What is "Hurricane"?'
    )

@app.route('/Album')
def Album():
    """Renders the about page."""
    return render_template(
        'PictureAlbum.html',
        title='Pictures',
        year=datetime.now().year,
        message='Welcome to my picture album'
    )

@app.route('/data')
def data():
    """Renders the about page."""
    return render_template(
        'data.html',
        title='WORLD HURRICANE REPORT',
        year=datetime.now().year,
        message='World Hurricane Report'
    )

@app.route('/Easy')
def Easy():
    
    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\Data\\hurricNamed.csv'))
    raw_data_table = df.to_html(classes = 'table table-hover')
    """Renders the about page."""
    return render_template(
        'Easy.html',
        title='WORLD HURRICANE REPORT',
        year=datetime.now().year,
                    raw_data_table = raw_data_table,
        message='Easy Hurricane Report'
    )

@app.route('/Camille')
def Camille():
    """Renders the about page."""
    return render_template(
        'Camille.html',
        title='WORLD HURRICANE REPORT',
        year=datetime.now().year,
        message='Camille Hurricane Report'
    )

@app.route('/Katrina')
def Katrina():
    """Renders the about page."""
    return render_template(
        'Katrina.html',
        title='WORLD HURRICANE REPORT',
        year=datetime.now().year,
        message='Katrina Hurricane Report'
    )

@app.route('/register', methods=['GET', 'POST'])
def Register():
    form = UserRegistrationFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (not db_Functions.IsUserExist(form.username.data)):
            db_Functions.AddNewUser(form)
            db_table = ""

            flash('Thanks for registering new user - '+ form.FirstName.data + " " + form.LastName.data )
            # Here you should put what to do (or were to go) if registration was good
        else:
            flash('Error: User with this Username already exist ! - '+ form.username.data)
            form = UserRegistrationFormStructure(request.form)

    return render_template(
        'register.html', 
        form=form, 
        title='Register New User',
        year=datetime.now().year,
        repository_name='Pandas',
        )

# -------------------------------------------------------
# Login page
# This page is the filter before the data analysis
# -------------------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def Login():
    form = LoginFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (db_Functions.IsLoginGood(form.username.data, form.password.data)):
            flash('Login approved!')
            #return redirect('<were to go if login is good!')
        else:
            flash('Error in - Username and/or password')
   
    return render_template(
        'login.html', 
        form=form, 
        title='Login to data analysis',
        year=datetime.now().year,
        repository_name='Pandas',
        )


@app.route('/Query', methods=['GET', 'POST'])
def Query():

    Name = None
    Country = ''
    capital = ''
    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\Data\\hurricNamed.csv'))
    df = df.set_index('Name')

    form = QueryFormStructure(request.form)
     
    if (request.method == 'POST' ):
        name = form.name.data
        Country = name
        if (name in df.index):
            capital = df.loc[name,'Capital']
        else:
            capital = name + ', no such country'
        form.name.data = ''

    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\Data\\hurricNamed.csv'))

    raw_data_table = df.to_html(classes = 'table table-hover')

    return render_template('Query.html', 
            form = form, 
            name = capital, 
            Country = Country,
            raw_data_table = raw_data_table,
            title='Query by the user',
            year=datetime.now().year,
            message='This page will use the web forms to get user input'
        )



