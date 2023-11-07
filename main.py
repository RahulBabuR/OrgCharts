from urllib import request
from http.client import responses
from urllib import response
from flask import Flask, render_template,session,make_response,request,send_file,jsonify





 
# WSGI Application
# Provide template folder name
# The default folder name should be "templates" else need to mention custom folder name
app = Flask(__name__, template_folder='templates', static_folder='static')

 
# @app.route('/')
# def welcome():
#     return "This is the home page of Flask Application"

@app.route('/')
def index():
        msg=''
        return render_template('index.html',msg=msg)
if __name__=='__main__':
    app.run(debug = True)
