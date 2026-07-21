from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Database create
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
email TEXT,
message TEXT
)
""")
conn.commit()
conn.close()

@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/applications")
def applications():
    return render_template("applications.html")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/users")
def users():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    conn.close()
    return render_template("users.html", data=data)

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users(name,email,message) VALUES(?,?,?)",
                   (name,email,message))
    conn.commit()
    conn.close()

    return """
<!DOCTYPE html>
<html>
<head>
    <title>Success</title>
    <style>
        body{
            font-family:Arial,sans-serif;
            background:#0f2027;
            color:white;
            text-align:center;
            padding-top:100px;
        }
        .box{
            width:450px;
            margin:auto;
            background:#203a43;
            padding:30px;
            border-radius:10px;
            box-shadow:0 0 15px cyan;
        }
        h2{
            color:#00ff99;
        }
        a{
            color:white;
            background:#00bcd4;
            padding:10px 20px;
            text-decoration:none;
            border-radius:5px;
        }
    </style>
</head>
<body>

<div class="box">
    <h2>✅ Data Saved Successfully!</h2>
    <p>Your details have been stored in the database.</p>
    <br>
    <a href="/">Go Back to Home</a>
</div>

</body>
</html>
"""

@app.route("/healthcare")
def healthcare():
    return render_template("healthcare.html")

@app.route("/banking")
def banking():
    return render_template("banking.html")

@app.route("/education")
def education():
    return render_template("education.html")

@app.route("/cybersecurity")
def cybersecurity():
    return render_template("cybersecurity.html")

@app.route("/selfdriving")
def selfdriving():
    return render_template("selfdriving.html")

if __name__ == "__main__":
    app.run(debug=True)