from flask import Flask, redirect, request, render_template, session, flash

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run()
