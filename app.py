from flask import Flask, render_template, url_for
import csv

app = Flask(__name__)



def load_csv_data(filename):
    myList = []
    with open(filename) as customers:
        numbers_data = csv.reader(customers, delimiter=',')
        next(numbers_data) #skip the header
        for row in numbers_data:
            myList.append(row)
        return myList

@app.route('/')
def index():
    new_list = load_csv_data('customers.csv')
    return str(new_list)
    #return "Hello World Bartu22222 github"
    #return render_template('index.html')

if __name__ == "_main_":
    #app.run(host='0.0.0.0', port=5000)
    app.run(debug = True)

#during the production you should set the debug to False