from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,IntegerField,RadioField,SelectField,FloatField
from wtforms.validators import DataRequired,EqualTo,ValidationError,NumberRange
from app_package import app,mongo

class CourseForm(FlaskForm):
	courseName=SelectField("Course :",validators=[DataRequired()])
	submit=SubmitField("Submit ")
	
class AddModuleForm(FlaskForm):
	courseName=StringField("Course :",validators=[DataRequired()])
	name=SelectField("Modules :",validators=[DataRequired()])
	submit=SubmitField("Add ")