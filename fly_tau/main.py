from flask import Flask, render_template, request, redirect, url_for, session
import re
from datetime import datetime
app = Flask(__name__)
@app.route('/')

def homepage():
    return render_template("home_page.html")

@app.route('/flights_board')
def flights_board():
    return render_template("flights_board.html")

@app.route('/signup_page' ,methods=['GET', 'POST']) #creating signup page with forms
def signup_page():
    if request.method == "POST":
        registration_date = datetime.now()
        signup_first_name = request.form.get('signup_first_name')
        signup_last_name = request.form.get('signup_last_name')
        email_user=request.form.get('email_user')
        phones=request.form.getlist('phone_number_user')
        phones=[p for p in phones if p]
        passport_code=request.form.get('passport_code')
        birth_date=request.form.get('birth_date')
        password_user=request.form.get('password_user')
        confirm_password_user=request.form.get('confirm_password_user')
        if password_user != confirm_password_user:
            return"unmatched passwords"

        if not checking_validation(signup_first_name) or not checking_validation(signup_last_name): #checking if the names are really just in english letters
            return "name must contain only English letters"
        return render_template("flights_board.html")
    else:
        return render_template("signup_page.html")


def checking_validation(text):
    if not text:
        return False
    return bool(re.fullmatch(r'[A-Za-z ]+', text))

print("hello world")