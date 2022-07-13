from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm
from flask_behind_proxy import FlaskBehindProxy
from flask_sqlalchemy import SQLAlchemy


# this gets the name of the file so Flask knows it's name
app = Flask(__name__)
proxied = FlaskBehindProxy(app)
app.config['SECRET_KEY'] = 'f469b62dd5d493ae3bb500382bb84961'


# this tells you the URL the method below is related to
@app.route("/")
@app.route("/home")
def hello_world():
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
    # checks if entries are valid
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        # if valid - load home page
        return redirect(url_for('home'))
    # if not valid - reload registration page
    return render_template('register.html', title='Register', form=form)


# this should always be at the end
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
