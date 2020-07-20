from flask import Flask, render_template, url_for, request, redirect
import csv


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/contact.html')
def html_page():
    return render_template('contact.html')
@app.route('/About.html')
def my_page():
    return render_template('About.html')
    
@app.route('/index.html')
def index_page():
    return render_template('index.html')

    
@app.route('/thankyou.html')
def thankyou_page():
    return render_template('thankyou.html')


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        Name = data["Name"]
        Email = data["Email"]
        Phone = data["Phone"]
        Subject = data["Subject"]
        Message = data["Message"]
        file = database.write(f'\n{Name}, {Email}, {Phone}, {Subject}, {Message}')

def write_to_csv(data):
    
    with open('database.txt', mode='a') as database:
        Name = data["Name"]
        Email = data["Email"]
        Phone = data["Phone"]
        Subject = data["Subject"]
        Massage = data["massage"]
        csv_writer = csv_writer(database, delimiter=',', quotechar='!', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([Name,Email,Phone,Subject,Massage])
    
        

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wronhg. Try again!' 