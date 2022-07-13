from flask import Flask, render_template
# this gets the name of the file so Flask knows it's name
app = Flask(__name__)


# this tells you the URL the method below is related to
@app.route("/")
@app.route("/home")
def hello_world():
    # this prints HTML to the webpage
    return render_template('home.html', subtitle='Home Page',
                           text='This is the home page')


@app.route("/second_page")
def second_page():
    return render_template('second_page.html', subtitle='Second Page',
                           text='This is the second page')


# this should always be at the end
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
