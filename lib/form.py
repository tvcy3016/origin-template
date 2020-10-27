# coding=UTF-8
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, PasswordField, RadioField, IntegerField, TextAreaField, SelectMultipleField, widgets
from wtforms.fields.html5 import EmailField, DateTimeLocalField, DateField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea
from flask_wtf.file import FileField, FileRequired, FileAllowed

