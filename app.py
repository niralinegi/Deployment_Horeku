# import a library

from flask import Flask, render_template
from flask.globals import request

# Create an instance of an app
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('landing.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/data', methods = ['POST'])
def data():

    first_name = request.form.get('First_Name')
    second_name = request.form.get('Last_Name')
    phone = request.form.get('Number')
    email = request.form.get('email')

    print(first_name)
    print(second_name)
    print(phone)
    print(email)

    return 'form submitted'

if __name__== '__main__':
    app.run(debug=True)