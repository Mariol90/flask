from flask import Flask

app = Flask(__name__)
# /welcome
#     Returns “welcome”
# /welcome/home
#     Returns “welcome home”
# /welcome/back
#     Return “welcome back” 

@app.route('/')
def main_page():
    return "Hi"

@app.route('/welcome')
def welcome():
    return "Welcome"

@app.route('/welcome_home')
def welcome_home():
    return "Welcome home"

@app.route('/welcome_back')
def welcome_back():
    return "Welcome back"
    
