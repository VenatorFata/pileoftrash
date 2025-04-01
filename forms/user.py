from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    surname = StringField('Фамилия Марсианина', validators=[DataRequired()])
    name = StringField('Имя Марсианина', validators=[DataRequired()])
    age = StringField('Возраст', validators=[DataRequired()])
    position = StringField('Позиция (ранг) Марсианина', validators=[DataRequired()])
    speciality = StringField('Специализация Марсианина', validators=[DataRequired()])
    address = StringField('Модуль работы Марсианина', validators=[DataRequired()])
    submit = SubmitField('Войти')