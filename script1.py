from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/subpage/")
def subpage():
    return render_template("subpage.html")

if __name__ == "__main__":
    app.run(debug=True)
