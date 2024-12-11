#Libraries
from flask import Flask, render_template, jsonify, request
from berturk import rougeScore, text, count, randomScore

#Flask
app = Flask(__name__)

#Main page view function
@app.route("/")
def main():
    return render_template("main.html")

#News page view function
@app.route("/news")
def news():
    return render_template("news.html", rScore=rougeScore, copy="")

#Sums page view function
@app.route("/sums")
def sums():
    return render_template("sums.html")

#Running randomScore function from berturk.py to give ROUGE-1 score random value
@app.route("/rscore_increase", methods=["POST"])
def randScore():
    input_text = request.json.get("text", "")
    new_score, new_text, count = randomScore(input_text)
    #new_text = copyText(input_text)
    return jsonify({"copy": new_text,"rScore": new_score,"count":count})

if __name__ == "__main__":
    app.run(debug=True)