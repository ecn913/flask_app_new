from flask import Flask, render_template, Blueprint

my_view = Blueprint("my_view", __name__)

@my_view.route("/")
def index():
    return render_template("index.html")

@my_view.route("/page2")
def page2():
    return render_template("page2.html")

@my_view.route("/page3")
def page3():
    my_name = "Evan"
    return render_template("page3.html", my_name = my_name)

if __name__ == "__main__":
    app.run(debug = True, port = 8000)