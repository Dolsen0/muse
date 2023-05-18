from flask import Flask, render_template
from scales import get_scale

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return "About Page"

@app.route("/contact")
def contact():
    return "Contact Page"

@app.route("/user/<username>")
def user(username):
    return f"Hello, {username}!"

@app.route("/scales/major")
def major():
    root = "C"
    scale_name = "major"
    major_scale = get_scale(root, scale_name)
    return render_template("major_scale.html", major_scale=major_scale)

if __name__ == '__main__':
    app.run()
