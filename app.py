from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World Bartu22222 github"
    #return render_template('index.html')

if __name__ == "_main_":
    #app.run(host='0.0.0.0', port=5000)
    app.run(debug = True)

#during the production you should set the debug to False