from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def helloworld():
    return render_template("hello.html")

@app.route('/<name>')
def helloname(name):
    return f"<p>hello, {name}!</p>"