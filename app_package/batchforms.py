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
    coursename=SelectField("Course Name: ",coerce=str,validators=[DataRequired()])
    batch_status=SelectField("Batch Status: " , choices=[('Disabled','Disabled'),('Active','Active')])
    res_name=SelectField("Resource Name:" ,coerce=str,validators=[DataRequired()])
    submit=SubmitField("Add New Batch")

class ModifyBatchForm(FlaskForm):
    start_date=DateTimeField("Start Date")
    end_date=DateTimeField("End Date")
    batch_status=SelectField("Batch Status: " , choices=[('Disabled','Disabled'),('Active','Active')])
    submit=SubmitField("Modify Batch")



       
    
