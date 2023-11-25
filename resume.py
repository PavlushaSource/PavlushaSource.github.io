from flask import Flask, render_template, url_for

# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import DeclarativeBase

app = Flask(__name__, template_folder="templates")


@app.route("/")
def start_server():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
