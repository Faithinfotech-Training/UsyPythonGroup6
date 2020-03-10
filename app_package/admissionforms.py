from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SelectField,BooleanField,SubmitField,IntegerField,RadioField,TextAreaField
from wtforms.validators import DataRequired, EqualTo
#from app_package.models import User

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
    batch_name=SelectField("Batch Assigned:",choices=[],coerce=str,validators=[DataRequired()])
    e_guardianname=StringField("Gaurdian Name:",validators=[DataRequired()])
    e_guardianphone=IntegerField("Guardian Phone:",validators=[DataRequired()])
    e_address=TextAreaField("Address:")
    submit=SubmitField("Add")

class AdmissionUpdateForm(FlaskForm):
    ad_name=StringField("Name:",validators=[DataRequired()])
    ad_phone=IntegerField("Phone:",validators=[DataRequired()])
    ad_email=StringField("Email:",validators=[DataRequired()])
    ad_qualification=StringField("Highest Qualification:",validators=[DataRequired()])
    ad_year_of_pass=IntegerField("Passout Yaer:",validators=[DataRequired()])
    ad_batch=SelectField("Batch Assigned:",choices=[],coerce=str,validators=[DataRequired()])
    ad_guardianname=StringField("Gaurdian Name:",validators=[DataRequired()])
    ad_guardianphone=IntegerField("Guardian Phone:",validators=[DataRequired()])
    ad_address=TextAreaField("Address:")
    submit=SubmitField("Update")
