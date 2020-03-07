from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,IntegerField,RadioField,SelectField
from wtforms.validators import DataRequired, EqualTo,ValidationError,NumberRange


class AddResourceForm(FlaskForm):
    res_name=StringField("Resource name ",validators=[DataRequired()])
    res_capacity=IntegerField("Capacity ",validators=[DataRequired(),NumberRange(min=1)])
    res_status=SelectField("Status", choices = [('available','available'),('not available','not available')])
    res_rent=IntegerField("Resource rent ",validators=[DataRequired(),NumberRange(min=0)])
    type_of_use=SelectField("Type of use", choices = [('training','training'),('seminar','seminar'),('practicals','practicals')])
    submit=SubmitField("Create new resource")
    
class UpdateResourceForm(FlaskForm):
    
    res_capacity=IntegerField("New capacity ",validators=[NumberRange(min=1)])
    res_status=SelectField("Status", choices = [('available','available'),('not available','not available')])
    res_rent=IntegerField("Enter the rent  ",validators=[NumberRange(min=0)])
    type_of_use=SelectField("Type of use", choices = [('training','training'),('seminar','seminar'),('practicals','practicals')])
    submit=SubmitField("Update")
                
