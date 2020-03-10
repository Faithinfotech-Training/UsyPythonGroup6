from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,IntegerField,RadioField,SelectField
from wtforms.validators import DataRequired, EqualTo,ValidationError,NumberRange
from wtforms.validators import Email
from wtforms.fields.html5 import EmailField
from app_package.models import Role,Login,Registration

class LoginForm(FlaskForm):

    username=StringField("Username: ",validators=[DataRequired()])
    password=PasswordField("Password: ",validators=[DataRequired()])
    remember_me=BooleanField("Remember Me")
    submit=SubmitField("Sign in")

class RegistrationForm(FlaskForm):

    fullname=StringField("Fullname: ",validators=[DataRequired()])
    username=StringField("Username: ",validators=[DataRequired()])
    mobile=IntegerField("Mobile:",validators=[DataRequired()])
    email=StringField("Email:",validators=[DataRequired(),Email()])
    role_id=RadioField('Role', choices = [('1','admin'),('2','cordinator')],validators=[DataRequired()])
    password=PasswordField("Password: ",validators=[DataRequired()])
    password2=PasswordField("Confirm Password: ",validators=[DataRequired(),EqualTo("password")])
    submit=SubmitField("Register")


                
