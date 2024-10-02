from flask import Flask, render_template, request,flash
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')
@app.route("/hello")
def index():
    flash("what is your name?")
    return render_template("index.html")

@app.route("/greet",methods=["POST","GET"])
def greet():
    flash("Hi "+ str(request.form["name_input"])+", great to see you!!")
    request.form['name_input']
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)