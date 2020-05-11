

from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import Form, BooleanField, PasswordField
from wtforms import TextField, TextAreaField, SelectField, DateField
from wtforms import validators, ValidationError

from wtforms.validators import DataRequired





class QueryFormStructure(FlaskForm):
    name   = StringField(' Name:  ' , validators = [DataRequired()])
    submit = SubmitField('Submit')




    #user login
class LoginFormStructure(FlaskForm):
    username   = StringField('User name:  ' , validators = [DataRequired()])
    username   = StringField('User name:  ' , validators = [DataRequired()])
    username   = StringField('User name:  ' , validators = [DataRequired()])
    username   = StringField('User name:  ' , validators = [DataRequired()])
    username   = StringField('User name:  ' , validators = [DataRequired()])
    password   = PasswordField('Pass word:  ' , validators = [DataRequired()])
    submit = SubmitField('Submit')



    #user registration
class UserRegistrationFormStructure(FlaskForm):
    FirstName  = StringField('First name:  ' , validators = [DataRequired()])
    LastName   = StringField('Last name:  ' , validators = [DataRequired()])
    PhoneNum   = StringField('Phone number:  ' , validators = [DataRequired()])
    EmailAddr  = StringField('E-Mail:  ')
    username   = StringField('User name:  ' , validators = [DataRequired()])
    password   = PasswordField('Pass word:  ' , validators = [DataRequired()])
    submit = SubmitField('Submit')




    #query forms
    ## This class have the fields that the user can set, to have the query parameters for analysing the data
    ## This form is where the user can set different parameters, in my project the parameters are: start year and end year.
    ##that will be used to do the data analysis (using Pandas etc.)
class enteryears(FlaskForm):
    start_year= StringField('Enter a start year:' , validators = [DataRequired])
    end_year= StringField('Enter an end year:' , validators = [DataRequired])
    submit = SubmitField('submit')

