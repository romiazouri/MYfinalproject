

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
from flask   import Flask, flash
from wtforms import Form, BooleanField, PasswordField, validators
from wtforms import TextField, TextAreaField, SelectField, DateField
from wtforms import ValidationError


from DemoFormProject.Models.QueryFormStructure import QueryFormStructure
from DemoFormProject.Models.QueryFormStructure import UserRegistrationFormStructure
from DemoFormProject.Models.QueryFormStructure import LoginFormStructure 
from DemoFormProject.Models.QueryFormStructure import enteryears
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
db_Functions = create_LocalDatabaseServiceRoutines() 


#This is a rout to the home page

@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )


#This is a rout to the contact page
@app.route('/contact')
def contact():
    return render_template(
        'contact.html',
        title='Contact page',
        year=datetime.now().year,
        message='Please contact me'
    )


#This is a rout to about page
@app.route('/about')
def about():
    return render_template(
        'about.html',
        title='Some about Hurricanes',
        year=datetime.now().year,
        message='What is "Hurricane"?'
    )


#This is a rout to the album page
@app.route('/Album')
def Album():
    return render_template(
        'PictureAlbum.html',
        title='Pictures',
        year=datetime.now().year,
        message='Welcome to my picture album'
    )


#This is a rout to the data page
@app.route('/data')
def data():
    return render_template(
        'data.html',
        title='WORLD HURRICANE REPORT',
        year=datetime.now().year,
        message='World Hurricane Report'
    )


#This is a rout to Easy hurricane dataset page 
@app.route('/Easy')
def Easy():
    
    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\Data\\hurricNamed.csv'))
    raw_data_table = df.to_html(classes = 'table table-hover')
    return render_template(
        'Easy.html',
        title='WORLD HURRICANE REPORT',
        year=datetime.now().year,
                    raw_data_table = raw_data_table,
        message='Easy Hurricane Report'
    )


#This is a rout to Camille hurricane dataset page 
@app.route('/Camille')
def Camille():
    return render_template(
        'Camille.html',
        title='WORLD HURRICANE REPORT',
        year=datetime.now().year,
        message='Camille Hurricane Report'
    )


#This is a rout to Kathrina hurricane dataset page 
@app.route('/Katrina')
def Katrina():
    return render_template(
        'Katrina.html',
        title='WORLD HURRICANE REPORT',
        year=datetime.now().year,
        message='Katrina Hurricane Report'
    )

#This is a rout to register page
@app.route('/register', methods=['GET', 'POST'])
def Register():
    form = UserRegistrationFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (not db_Functions.IsUserExist(form.username.data)):
            # If there isn't another user with that username
            db_Functions.AddNewUser(form)
            db_table = ""
             # Adds a new user to the system.


            flash('Thanks for registering new user - '+ form.FirstName.data + " " + form.LastName.data )
            #Here you should put what to d (or where to go) if registration is good
           
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


#This is a rout to login page
@app.route('/login', methods=['GET', 'POST'])
def Login():
    form = LoginFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (db_Functions.IsLoginGood(form.username.data, form.password.data)):
            # Checks if the input matches the information in the system:
            flash('Login approved!')
            return redirect('Query')
            #If login is good open the query page
        else:
            flash('Error in - Username and/or password')
   
    return render_template(
        'login.html', 
        form=form, 
        title='Login to data analysis',
        year=datetime.now().year,
        repository_name='Pandas',
        )


#This is a rout to the query page
@app.route('/Query', methods=['GET', 'POST'])
def Query():
    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\Data\\hurricNamed.csv'))
    form = enteryears()
    chart = "https://papers.co/wallpaper/papers.co-mc83-wallpaper-between-storm-clouds-sky-40-wallpaper.jpg"
    if (request.method == 'POST' ):
        startyear = form.start_year.data
        endyear = form.end_year.data
        df=df[["Year", "deaths"]]
        df=df.groupby("Year").sum()
        df=df.loc[startyear:endyear]
        fig = plt.figure()
        ax = fig.add_subplot(111)
        df.plot(kind="bar", ax=ax)
        #Creates the graph
        chart = plot_to_img(fig)
        #Converts the graph to an image so it could be displayed


    return render_template('Query.html', 
            form = form, 
            title='Query by the user',
            chart = chart
        )


def plot_to_img(fig):
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    return pngImageB64String




