from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Homepage content :)"

@app.route("/subpage/")
def subpage():
    return "Subpage content."

if __name__ == "__main__":
    app.run(debug=True)
