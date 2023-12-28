from flask import Flask,render_template,session,request
from flask_restful import Api
from Database import db
from Resources import routes
from Database.model import Birdsdb
app = Flask(__name__)
app.secret_key="122344fggdas"
app.config['MONGODB_SETTINGS'] = {'host':'mongodb://localhost:27017/BirdsHeaven'}
db.initialize_db(app)
api = Api(app)
routes.initialize_routes(api)


@app.route("/displaySignUp")
def signup():
    return render_template("SignUp.html")


@app.route("/displayLogin")
def login():
    return render_template("Login.html")

@app.route("/displayAddBird")
def displayAddBird():
    if session["type"] == "Breeder":
        return render_template("AddBirds.html")


@app.route("/displayUpdate")
def updateBird():
    if session["type"] == "Breeder":
        return render_template("UpdateBirds.html")

@app.route("/displayDelete")
def displayDelete():
    if session["type"] == "Breeder":
        return render_template("DeleteBird.html")

@app.route("/signout")
def signout():
    session.clear()
    return render_template("Login.html")

@app.route("/display")
def display():
    if session["type"] == "Breeder":
        return render_template("DisplayBird.html")

@app.route("/displayDashboard")
def displayDashboard():
    if session["type"] == "Breeder":
        return render_template("Dashboard.html",user = session["uname"])

@app.route("/deleteBird", methods=["GET","POST"])
def deleteBird():
    try:
        ringno = request.form["ringno"]
        bird = Birdsdb.objects.get(ringno=ringno)
        if bird:
            Birdsdb.objects.get(ringno=ringno).delete()
            return render_template("Dashboard.html", message="Successfully Deleted!")
        else:
            return render_template("DeleteBird.html", message="Bird Not Found!")
    except Exception as e:
            return render_template("Dashboard.html", message="Bird Not Found")


if __name__ == '__main__':
    app.run()
