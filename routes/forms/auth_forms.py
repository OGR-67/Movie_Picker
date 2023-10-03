from flask_wtf import FlaskForm  # type: ignore
from wtforms import StringField, PasswordField, SubmitField  # type: ignore
from wtforms.validators import DataRequired, Length, none_of  # type: ignore


class LoginOrRegistrationForm(FlaskForm):  # type: ignore
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Length(min=2, message="Username is too short"),
            none_of(' ', message='Username cannot contain spaces')
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=8, message="Password is too short")
        ])
    submit_button = SubmitField('Submit')
