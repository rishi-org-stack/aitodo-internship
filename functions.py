from flask import Flask, app,render_template
from flask.globals import request
from loginmodel import *

app =Flask(__name__)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login/<string:name>/<string:password>/<string:db>",methods=['POST','GET'])
def logined(name,password,db):
    # name = request.form['username']
    # password = request.form['password']
    return serchbynameandpassword(name,password,db)

if __name__ == "__main__":
    app.run(debug=True)