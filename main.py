from flask import Flask, redirect, request, render_template, flash

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


@app.route('/welcome', methods=['POST', 'GET'])
def validate_signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
    return render_template('welcome.html')
    # username and password musn't have spaces and
    # and be between 3-20 characters

    # user's password and verify don't match
    # if not password == verify:
    # flash("Verify Password does not match Password.")
    # return redirect('/signup')
    # else:
    # pass
    # user provided a non-valid email. valid email has
    # one @, a single ., no spaces, and is between 3-20 characters


if __name__ == '__main__':
    app.run()
