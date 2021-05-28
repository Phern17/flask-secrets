from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap


class MyForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email()])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=4)])
    submit = SubmitField(label="log in")


app = Flask(__name__)
Bootstrap(app)
app.secret_key = "random_secret_string"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['POST', 'GET'])
def login():
    path_url = 'login.html'
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            path_url = "success.html"
        else:
            path_url = "denied.html"

    return render_template(path_url, form=form)


if __name__ == '__main__':
    app.run(debug=True)