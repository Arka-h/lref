from flask import Flask, render_template, request

serverlink = Flask(__name__)

@serverlink.route('/<string:name>')#,methods=['POST','GET'] for user to access  the url
def hello_world(name) :
    return f'Hello {name}!'
