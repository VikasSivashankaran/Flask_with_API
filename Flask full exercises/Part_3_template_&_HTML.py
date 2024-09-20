
from flask import Flask, render_template, redirect,url_for


app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    myvalue = 'NeuralNine'
    myresult = 10 + 20
    mylist  = [1,2,3,4,5,6,7,30]
    return render_template('index.html',mylist1= mylist, myvalue1=myvalue,myresult1=myresult),201

@app.route('/other')
def other():
    some_text = 'vikassivashankaran'
    return render_template('other.html', some_text = some_text)

@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('other'))


@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]

@app.template_filter('repeat')
def repeat(s, times = 2):
    return s * times

@app.template_filter('alternate_case')
def alternate_case(s):
    return ''.join([c.upper() if i % 2 == 0 else c.lower() for i ,c in enumerate(s)])

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=7410)