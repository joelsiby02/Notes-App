from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

# login route 
@auth.route('/login')
def login():
    return render_template("login.html")

# Signup route
@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")

# logout route
# @auth.route('/logout')
# def logout():
#     return render_template("logout.html")
