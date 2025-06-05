from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired, Email

class BookingForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    destination = StringField('Destination', validators=[DataRequired()])
    date = DateField('Travel Date', validators=[DataRequired()])
    submit = SubmitField('Book Now')
