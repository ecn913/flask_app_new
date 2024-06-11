from flask import Flask, render_template

app = Flask(__name__)
app.register_blueprint(my_view)

if __name__ == "__main__":
    app.run(debug = True, port = 8000)