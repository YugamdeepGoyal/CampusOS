from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, MetaData, Table, select, Integer, String, Column

app = Flask(__name__)
engine = create_engine("sqlite:///CampusOSdb.db")
meta = MetaData()
data = Table(
    "users_data",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("email", String, nullable=False),
    Column("password", String, nullable=False),
    Column("member_type", String, default="student", nullable=False),
)
meta.create_all(engine)


# home
@app.route("/")
def home():
    return render_template("index.html")


# login
@app.route("/login.html", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        with engine.connect() as conn:
            stmt = select(data)
            result = conn.execute(stmt)
            all_rows = result.fetchall()
            for row in all_rows:
                if row.email == username and row.password == password and row.member_type == "student":
                    return redirect(url_for("dashboard"))
                else:
                    return "INVALID"
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
