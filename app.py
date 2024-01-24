from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        print("Data received from Webhook is: ", request.json)
        return "OK!"
    else:
        print ("This is a get request")
        return render_template('webhook.html')

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/')
def home():
    return render_template('home.html')

app.run(host='0.0.0.0', debug=True, port=8000)