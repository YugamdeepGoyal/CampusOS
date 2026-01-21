from flask import Flask, render_template, request, redirect, url_for, session
from sqlalchemy import create_engine, MetaData, Table, select, Integer, String, Column

app = Flask(__name__)
app.secret_key = "230710"
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
    flag = 0
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        with engine.connect() as conn:
            stmt = select(data)
            result = conn.execute(stmt)
            all_rows = result.fetchall()
            for row in all_rows:
                if row.email == username and row.password == password:
                    session["user"] = username
                    if row.member_type == "student":
                        flag = 1
                        return redirect(url_for("dashboard"))
                    elif row.member_type == "faculty":
                        flag = 1
                        return redirect(url_for("faculty_dashboard"))
                    else:
                        flag = 1
                        return "ERROR"
            if not flag:
                return "INVALID"
    return render_template("login.html")


# dashboard
@app.route("/dashboard.html")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html")


# classrooms
@app.route("/classrooms.html")
def classrooms():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("classrooms.html")


# faculty dashboard
@app.route("/faculty_dashboard.html")
def faculty_dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("faculty_dashboard.html")


# myclasses
@app.route("/myclasses.html")
def myclasses():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("myclasses.html")


# notices
@app.route("/notices.html")
def notices():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("notices.html")


# post_notice
@app.route("/post_notice.html")
def post_notice():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("post_notice.html")


if __name__ == "__main__":
    app.run(debug=True)
