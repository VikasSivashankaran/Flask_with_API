from Tools.scripts.make_ctype import method
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello World!</h1>"

@app.route('/vikas', methods = ['GET', 'POST'])
def vikas():
    return "Hello World!"

@app.route('/greet/<name>')          #passing variable in browser "http://127.0.0.1:portno/greet/your name"
def greet(name):
    return f"vanakam {name}"

#adding 2 numbers using its datatypes
@app.route('/add/<int:num1>/<int:num2>')              #http://127.0.0.1:portno/add/2000000/1 in browser
def add(num1, num2):
    return f"{num1} + {num2} = {num1 + num2}"

@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args.get('name')
        return f'{greeting}, {name}'
    else:
        return f"some parameters are missing"



if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True, port = 6789)