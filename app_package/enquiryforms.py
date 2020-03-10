from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,IntegerField,RadioField,SelectField
from wtforms.validators import DataRequired, EqualTo
#from app_package.models import User

class EnquiryForm(FlaskForm):
    e_name=StringField("Name:",validators=[DataRequired(message="Name Required")])
    e_gender=RadioField("Gender:",choices = [('Male','Male'),('Female','Female'),('Other','Other')])
    e_phone=IntegerField("Phone:",validators=[DataRequired()])
    e_email=StringField("Email:",validators=[DataRequired()])
    e_qualification=StringField("Highest Qualification:",validators=[DataRequired(message="Qualification Required")])
    e_course_of_interest=StringField("Course Of Interest:",validators=[DataRequired(message="Course of interest required")])
    e_year_of_pass=IntegerField("Passout Year:",validators=[DataRequired()])
    e_status=SelectField("Status:",choices = [('New','New'),('Intersted','Intersted'),('Not Intersted','Not Intersted'),('Exam Passed','Exam Passed'),('Exam Failed','Exam Failed')])
    submit=SubmitField("Add")

class EnquirySearchForm(FlaskForm):
    es_type=RadioField("Type:",choices=[('Name','Name')])
    es_name=StringField("Search:",validators=[DataRequired(message="Name required")])
    submit=SubmitField("Search")

class EnquiryFilterForm(FlaskForm):
    ef_status=SelectField("Status:",choices = [('New','New'),('Intersted','Intersted'),('Not Intersted','Not Intersted'),('Exam Passed','Exam Passed'),('Exam Failed','Exam Failed'),('Joined','Joined')])
    submit=SubmitField("Filter")

class EnquiryUpdateForm(FlaskForm):
    eu_name=StringField("Name:",validators=[DataRequired(message="Name required")])
    eu_phone=IntegerField("Phone:",validators=[DataRequired()])
    eu_email=StringField("Email:",validators=[DataRequired()])
    eu_qualification=StringField("Highest Qualification:",validators=[DataRequired(message="Qualifiaction required")])
    eu_course_of_interest=StringField("Course Of Interest:",validators=[DataRequired(message="Course of Interest Required")])
    eu_year_of_pass=IntegerField("Passout Year:",validators=[DataRequired()])
    eu_status=RadioField("Status:",choices = [('Intersted','Intersted'),('Not Intersted','Not Intersted'),('Exam Passed','Exam Passed'),('Exam Failed','Exam Failed')])
    submit=SubmitField("Update")