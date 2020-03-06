from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,SelectField,DateTimeField
import datetime
#from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, EqualTo
#from app_package.models import User

class AddBatchForm(FlaskForm):
    batch_name=StringField("Batch Name: ",validators=[DataRequired()])
    date=datetime.datetime.today()
    start_date=DateTimeField("Start Date",default=date.today())
    end_date=DateTimeField("End Date",default=date.today())
    course_name=SelectField("Course Name: ",choices=[('Java','Java'),('Python','Python'),('.net','.net')])
    batch_status=SelectField("Batch Status: " , choices=[('Disabled','Disabled'),('Active','Active')])
    submit=SubmitField("Add New Batch")

class ModifyBatchForm(FlaskForm):
    start_date=DateTimeField("Start Date",format='%Y-%m-%d')
    end_date=DateTimeField("End Date",format='%Y-%m-%d')
    batch_status=SelectField("Batch Status: " , choices=[('Disabled','Disabled'),('Active','Active')])
    submit=SubmitField("Modify Batch")



       
    
