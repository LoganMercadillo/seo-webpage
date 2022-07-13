from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm
from flask_behind_proxy import FlaskBehindProxy
from flask_sqlalchemy import SQLAlchemy


# this gets the name of the file so Flask knows it's name
app = Flask(__name__)
proxied = FlaskBehindProxy(app)
app.config['SECRET_KEY'] = 'f469b62dd5d493ae3bb500382bb84961'

# database set-up
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


# this tells you the URL the method below is related to
@app.route("/")
@app.route("/home")
def home():
    # this prints HTML to the webpage
    return render_template('home.html', subtitle='Home Page',
                           text='This is the home page')


# second page
@app.route("/second_page")
def second_page():
    return render_template('second_page.html', subtitle='Second Page',
                           text='This is the second page')


# Registration page
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    # entries are valid
    if form.validate_on_submit():
        # send form data to database
        user = User(username=form.username.data,
                    email=form.email.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        # notify user of success
        flash(f'Account created for {form.username.data}!', 'success')
        # send to home page
        return redirect(url_for('home'))

    # entries are invalid - reload registration page
    return render_template('register.html', title='Register', form=form)


# this should always be at the end
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
