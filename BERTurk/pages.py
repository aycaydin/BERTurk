from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/sums")
def sums():
    return render_template("sums.html")

if __name__ == "__main__":
    app.run(debug=True)