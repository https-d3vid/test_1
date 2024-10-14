
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('Home.html')

@app.route('/signin', methods=["POST","GET"])
def Signin():
    return render_template('Signin.html')

@app.route('/signup', methods=["POST","GET"])
def Signup():
    return render_template('Signup.html')

@app.route('/profile')
def Profile():
    return render_template('Profile.html')

if __name__ == '__main__':
    app.run(debug=True)
