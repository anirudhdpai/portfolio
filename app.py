from flask import Flask, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/contactus')
def contactus():
    return render_template("contactus.html")

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")

@app.route('/hello')
def hello():
    json = { "name": "anirudh", "last": "pai"}
    return jsonify(json)

if __name__=="__main__":
    app.run(debug=True)