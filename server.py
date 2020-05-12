# כדי להפעיל את המערכת (MyWebsite) PS C:\Users\misha\Documents\MyWebsite> Scripts\activate.ps1
import os
import csv 
from flask import Flask, render_template, send_from_directory, url_for, request
app = Flask(__name__)
# activate anv - $env:FLASK_APP = "server.py"
# activate debug - $env:FLASK_ENV = "development"
# flask run

@app.route('/') 
def my_home(): 
    return render_template('index.html')

@app.route('/<string:page_name>') 
def html_page(page_name): 
    return render_template(page_name)


# def write_to_file(data):
#     with open("database.txt", mode="a") as database:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         text = database.write(f"\n{email}, {subject}, {message}")

def write_to_csv(data):
    with open("database.csv", mode="a", newline='') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['post', 'get'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return "form submitted"
        except:
            return "did not save to database"
    else:
        return "something went worng"