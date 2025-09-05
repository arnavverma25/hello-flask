import random
from flask import Flask, render_template

app = Flask(__name__)

def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

@app.route('/')
def helloworld():
    return render_template("hello.html")

@app.route('/<name>')
def helloname(name):
    return f"<p>hello, {name}!</p>"

@app.route("/rainbow")
def rainbow():
    return f"""
<head>
    <style>
        body {{
            background-color: {random_color()};
        }}
    </style>
</head>
<body>
    <p>Rainbow Flask</p>
</body>
    """

# ...existing code...

if __name__ == "__main__":
    app.run(debug=True)