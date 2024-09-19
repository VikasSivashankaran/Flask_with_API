
from flask import Flask, render_template

app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    myvalue = 'NeuralNine'
    myresult = 10 + 20
    mylist  = [1,2,3,4,5,6,7,30]
    return render_template('index.html',mylist1= mylist, myvalue1=myvalue,myresult1=myresult)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=7410)