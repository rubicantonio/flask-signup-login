from flask import Flask, redirect, url_for, render_template, request, session
import os
import sqlite3

conn = sqlite3.connect('passwordsdb', check_same_thread=False)
c = conn.cursor()
def getData():
    c.execute("SELECT * from users")
    for i in c.fetchall():
        print(i)
def insert(name1, password1):




    c.execute("INSERT INTO users (name, password) values (?, ?)", (name1, password1))




    conn.commit()



app = Flask(__name__)
app.secret_key = 'ItShouldBeAnythingButSecret'
@app.route("/auth", methods=[ "GET", "POST"])
def auth():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        tup = (name, password)
        print(name)


        c.execute("SELECT * from users")
        for i in c.fetchall():
            if i == tup:

                return render_template("loggedin.html", tup1=tup[0])

@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("login.html")


@app.route("/signup", methods=["POST", "GET"])
def index():

    return render_template("signup.html")

@app.route('/psignup', methods=["POST", "GET"])
def signup():
    if request.method == "POST":


            name = request.form["name"]
            password = request.form["password"]

            insert(name, password)

            return render_template("login.html")
