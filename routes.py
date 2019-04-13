from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
import csv
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'



# Homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("Template.html")

@app.route('/view', methods=['GET', 'POST'])
def view():
    return render_template("view.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")


@app.route('/logdata', methods=['GET', 'POST'])
def logdata():
    name = request.form['username']
    age = request.form['userage']
    # number = request.form['usernumber']
    email = request.form['useremail']
    password = request.form['userpassword']
    phone = request.form['userphone']
        
    record = {
            "full_name": name,
            "email": email,
            "age": age,
            "password": password,
            "phone":  phone
    }

    keys = []
    csv_columns = ['Full Name', 'Email Address', 'Age (in years)', 'Password', 'Phone Number']
    csv_file = "database.csv"
    try:
        with open (csv_file, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames= record.keys())
            writer.writeheader()
            writer.writerow(record)
    except IOError:
        print("I/O Error")
    return render_template('template.html')

@app.route('/validate', methods=['GET', 'POST'])
def validate():
    return render_template('template.html')

if __name__ == "__main__":
        app.run(debug=True)