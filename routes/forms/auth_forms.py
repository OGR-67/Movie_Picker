from flask_wtf import FlaskForm  # type: ignore
from wtforms import StringField, PasswordField, SubmitField  # type: ignore
from wtforms import ValidationError
from wtforms.validators import DataRequired, Length  # type: ignore


def no_spaces(form: FlaskForm, field: StringField) -> None:
    if " " in str(field.data):
        raise ValidationError("Username cannot contain spaces")


class LoginOrRegistrationForm(FlaskForm):  # type: ignore
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Length(min=4, message="Username is too short"),
            no_spaces
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=8, message="Password is too short")
        ])
    submit_button = SubmitField('Submit')
