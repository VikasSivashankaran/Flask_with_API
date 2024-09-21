#
import pandas as pd
import openpyxl

from flask import Flask, render_template, request,make_response,Response, request, make_response

app = Flask(__name__, template_folder='template4')

@app.route('/', methods = ['GET','POST' ])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'vikas' and password =='password':
            return 'Success'

        else:
            return 'Failure'

@app.route('/file_upload',methods=['POST'])
def file_upload():
    file = request.files['file']
    if file.content_type == 'text/plain':
        return file.read().decode()
    elif file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'or file.content_type=='application/vnd.ms-excel':
        df=pd.read_excel(file)
        return df.to_html()


@app.route('/convert_csv', methods=['POST'])
def convert_csv():
    file = request.files['file']
    df = pd.read_excel(file)

    # Convert DataFrame to CSV
    csv_data = df.to_csv(index=False)

    # Create response with appropriate headers
    response = make_response(csv_data)
    response.headers['Content-Disposition'] = 'attachment; filename=result.csv'
    response.headers['Content-Type'] = 'text/csv'

    return response

if __name__ == '__main__':
    app.run(debug=True )