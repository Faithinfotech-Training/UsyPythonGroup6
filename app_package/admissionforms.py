from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,IntegerField,RadioField,TextAreaField
from wtforms.validators import DataRequired, EqualTo
from app_package.models import User

class AdmissionSearchForm(FlaskForm):
    e_phone=IntegerField("Phone:",validators=[DataRequired()])
    submit=SubmitField("Search")

class AdmissionAddForm(FlaskForm):
    e_name=StringField("Name:",validators=[DataRequired()])
    e_gender=RadioField("Gender:",choices = [('Male','Male'),('Female','Female'),('Other','Other')])
    e_phone=IntegerField("Phone:",validators=[DataRequired()])
    e_email=StringField("Email:",validators=[DataRequired()])
    e_qualification=StringField("Highest Qualification:",validators=[DataRequired()])
    e_course_of_interest=StringField("Course Of Interest:",validators=[DataRequired()])
    e_year_of_pass=IntegerField("Passout Yaer:",validators=[DataRequired()])
    e_status=RadioField("Status:",choices = [('Joined','Joined')])
    e_phone=IntegerField("Phone:",validators=[DataRequired()])
    e_batch=IntegerField("Batch Assigned:",validators=[DataRequired()])
    e_guardianname=StringField("Gaurdian Name:",validators=[DataRequired()])
    e_guardianphone=IntegerField("Guardian Phone:",validators=[DataRequired()])
    e_address=TextAreaField("Address:")
    submit=SubmitField("Add")
