from flask import Flask, redirect, request, render_template
import cgi
import os
app = Flask(__name__)
app.config['DEBUG'] = True


def check_emptiness(string):

    if len(string) == 0:
        return True
    else:
        return False


@app.route('/signup')
def display_signup_page():
    return render_template('signup.html')


@app.route('/signup', methods=['POST'])
def validate_signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']
        # error variables
        username_error = ''
        password_error = ''
        verify_error = ''
        email_error = ''
    # username and password musn't have spaces and be between 3-20 characters
    if len(username) < 3 or len(username) > 20:
        username_error = 'Username must be between 3-20 charaters'

    if ' ' in username:
        username_error = 'Username cannot contain spaces'

    if len(password) < 3 or len(password) > 20:
        password_error = 'Password must be between 3-20 charaters'

    if ' ' in password:
        password_error = 'Password cannot contain spaces'

    # user's password and verify don't match
    if password != verify:
        verify_error = "Password and Verify Password don't match"

    # email has one @, a single ., no spaces, and between 3-20 characters
    if email == '':
        pass
    if ' ' in email:
        email_error = "Email can't have spaces"
    else:
        if '@' not in email and '.' not in email:
            email_error = "Your email must contain one @ symbol and one '.'"

    if len(email) < 3 or len(email) > 20:
        email_error = "Email must have one @, a single ., no spaces, and be between 3-20 character"

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username)
    else:
        return render_template('signup.html', name=username, email=email, username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)

if __name__ == '__main__':
    app.run()
