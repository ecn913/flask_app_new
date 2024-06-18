from flask import Flask, render_template, Blueprint, request
from bands import BandEntry

my_view = Blueprint("my_view", __name__)

band_objects = []

@my_view.route("/")
def index():
    return render_template("index.html")

@my_view.route("/page2", methods=["GET", "POST"])
def page2():
    if request.method == "POST":
        new_band = BandEntry(request.form["added_band"], 
        request.form["added_song"], 
        request.form["added_album"], 
        int(request.form["added_rate"]))
        band_objects.append(new_band)
    return render_template("page2.html", band_objects = band_objects)

@my_view.route("/page3")
def page3():
    my_name = "Evan"
    return render_template("page3.html", my_name = my_name)

if __name__ == "__main__":
    app.run(debug = True, port = 8000)