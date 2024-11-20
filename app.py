from flask import Flask, render_template

# 建立 Flask 應用
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/Previous_sessions")
def Previous_sessions():
    return render_template("Previous_sessions.html")

@app.route("/Daily_life")
def Daily_life():
    return render_template("Daily_life.html")

@app.route("/Honor")
def honor():
    return render_template("Honor.html")

if __name__ == "__main__":
    app.run(debug=True)
