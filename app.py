import random
from flask import Flask, render_template

app = Flask(__name__)

def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

@app.route("/")
def helloworld():
    # renders templates/hello.html
    return render_template("hello.html")

@app.route("/<name>")
def helloname(name):
    # renders templates/greet.html with a variable
    return render_template("greet.html", name=name)

@app.route("/rainbow")
def rainbow():
    # pass the color into the template rather than inlining CSS via f-string
    return render_template("rainbow.html", color=random_color())

if __name__ == "__main__":
    app.run(debug=True)
