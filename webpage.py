from flask import Flask
# this gets the name of the file so Flask knows it's name
app = Flask(__name__)


# this tells you the URL the method below is related to
@app.route("/")
def hello_world():
    # this prints HTML to the webpage
    return "<p>Hello, World!</p>"


# this should always be at the end
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
