from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,IntegerField,SelectField
from wtforms.validators import DataRequired, EqualTo,NumberRange
#from app_package.models import User

class AddCourseForm(FlaskForm):
    coursename=StringField("Name: ",validators=[DataRequired(message="Enter a valid course name")])
    courseduration=IntegerField("Duration in Days: ",validators=[NumberRange(min=0,message="Enter valid duration")])
    coursefee=IntegerField("Fee: ",validators=[DataRequired(message="Enter a valid course name"),NumberRange(min=1000,message="Enter valid fee")])
    coursestatus=SelectField('Status', choices = [('Running','Running'),('Disabled','Disabled')])
    coursedescription=StringField("Description: ",validators=[DataRequired(message="Enter a valid course description")])
    submit=SubmitField("Add Course")

    
class ModifyCourseForm(FlaskForm):
    coursename=StringField("Name: ",)
    courseduration=IntegerField("Duration in Days: ",validators=[NumberRange(min=0,message="Enter valid duration")])
    coursefee=IntegerField("Fee: ",validators=[NumberRange(min=0,message="Enter valid duration")])
    coursestatus=SelectField('Status', choices = [('Running','Running'),('Disabled','Disabled')])
    coursedescription=StringField("Description: ")
    submit=SubmitField("Modify Course")


