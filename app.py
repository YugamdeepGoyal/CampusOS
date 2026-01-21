from flask import Flask, render_template

app = Flask(__name__)


# home
@app.route("/")
def home():
    return render_template("index.html")


# login
@app.route("/login.html")
def login():
    return render_template("login.html")



# dashboard
@app.route("/dashboard.html")
def dashboard():
    return render_template("dashboard.html")


# classrooms
@app.route("/classrooms.html")
def classrooms():
    return render_template("classrooms.html")


# faculty dashboard
@app.route("/faculty_dashboard.html")
def faculty_dashboard():
    return render_template("faculty_dashboard.html")


# myclasses
@app.route("/myclasses.html")
def myclasses():
    return render_template("myclasses.html")


# notices
@app.route("/notices.html")
def notices():
    return render_template("notices.html")


# post_notice
@app.route("/post_notice.html")
def post_notice():
    return render_template("post_notice.html")


if __name__ == "__main__":
    app.run(debug=True)
