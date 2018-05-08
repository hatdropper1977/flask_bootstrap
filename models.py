from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, TextAreaField
from wtforms.validators import Length, Email, InputRequired

# Form ORM
class QuizForm(FlaskForm):
        essay_question = TextAreaField('Who do you think won the console wars of 1991, Sega Genesis or Super Nintendo? (2048 characters)', validators=[InputRequired(),Length(max=2047)] )
        email_addr = TextField('Enter Your Email', validators=[InputRequired(), Email()])
        submit = SubmitField('Submit')
