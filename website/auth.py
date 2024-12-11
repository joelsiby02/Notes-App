from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

# login route 
# @auth.route('/login', methods = ['GET', 'POST'])
# def login():
#     data = request.form
#     print(data)
#     return render_template("login.html")
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print(f'Email: {email}, Password: {password}')
    return render_template("login.html")

# Signup route
@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html",  methods = ['GET', 'POST'])

# logout route
# @auth.route('/logout')
# def logout():
#     return render_template("logout.html")
