from datetime import datetime
from ModelAPI import *
from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
import os
import time
#app.debug = True
app = Flask(__name__)
#below creates the instance of the database
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
#connects to the database file
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'
#change the secret key later
app.config["SECRET_KEY"] = "SECRETKEY123"
#auto reload templates
app.config["TEMPLATES_AUTO_RELOAD"] = True

#Allows falsk to load users
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#folder path were new users folder will be created
FODLER_PATH = r"users"

#file path to house the directory for the .csv files
FilePath = "dataSets/car data.csv"

# model
Linear_Model = None

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# creates a Login form
class LoginForm(FlaskForm):
    username = StringField(validators=[
        InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[
        InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField('Login')

#gets the date and time the file was created
def GetTime():
    #hopefully gives access to the users current login name
    form = LoginForm()
    user = User.query.filter_by(username=form.username.data).first()

    os.chdir(FODLER_PATH)
    mod_time = os.stat(user).st_mtime
    return (datetime.fromtimestamp(mod_time))

#creates the table for our database
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)


#Second table used to store user data files from training
class Storage(db.Model, UserMixin):

    usersname = db.Column(db.String(20), nullable=False, unique=True, primary_key=True)
    date = db.Column(db.DateTime(), nullable=False)
    path = db.Column(db.String(80), nullable=False)
    size = db.Column(db.String(80),nullable=False)


#creates a registration form
class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField('Register')

    #validation check to make sure the username doesnt already exist
    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')



#=====================================================================================================================
#Food For Thought. Problems occurs when trying to give access to files based on Users that dont exist yet
#Possible Solution, run the function to create the files from the entries in the column in the database, than comapre if the
# user name is unique when creating a new one or checking for a specific version.from
# Also create a check to stop from creating duplicate folder names.


#creates a new folder based on the users name
def createNewDir(FODLER_PATH):
    #hopefully gives access to the users current login name
    form = LoginForm()
    user = User.query.filter_by(username=form.username.data).first()

    os.chdir(FODLER_PATH)
    os.mkdir(user)

#List all the files in a dir and their path
def listDir(FODLER_PATH):
    os.chdir(FODLER_PATH)
    print("File Name: " + fileName)
    print("Folder Path: " + os.path.abspath(os.path.join(dir, fileName)), sep="\n")

# returns the file path
def GetFilePath(FODLER_PATH):
    os.chdir(FODLER_PATH)
    return(os.path.abspath(os.path.join(dir, fileName)))


#naviagates to the user path and hopefully returns the file size of the files named after the user name
def GetFileSize():
    #hopefully gives access to the users current login name
    form = LoginForm()
    user = User.query.filter_by(username=form.username.data).first()

    os.chdir(FODLER_PATH )
    return(os.stat(user).st_size)



#=====================================================================================================================

#various routes to html files
@app.route("/")
def index():
    print("home")
    return render_template("home1.html")

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard1.html")

@app.route("/dashboard2")
def dashboard2():
    return render_template("dashboard2.html")

@app.route("/about")
def about():
    return render_template("about1.html")

@app.route("/help")
def help():
    return render_template("help.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/account")
def account():
    return render_template("account.html")

@app.route("/train", methods=["POST","GET"])
def train():
    if request.method == "POST":
        xInputs = [request.form["x1"], request.form["x2"], request.form["x3"], request.form["x4"], request.form["x5"], request.form["x6"], request.form["x7"], request.form["x8"]]
        yInput = request.form["y1"]
        global Linear_Model
        Linear_Model = ModelAPI("dataSets/car_web_dataset.csv", xInputs, yInput) 
        Linear_Model.train()
        return render_template("train.html")
    else:
        return render_template("train.html")

@app.route("/test")
def test():
    # if request.method == "POST":
    #     xInputs2 = [requst.form["x2-1"], request.form["x2-2"], request.form["x2-3"], request.form["x2-4"], request.form["x2-5"], request.form["x2-6"], request.form["x2-7"]]
    #     Linear_Model.predict(xInputs2, yInput2)
    # else:
    #     return render_template("Test.html")
    performance = Linear_Model.performance()
    return render_template("test.html", data = performance)

@app.route("/results2", methods=["POST","GET"])
def results2():
    if request.method == "POST":
        xInputs = [float(request.form["x1"]), int(request.form["x2"]), int(request.form["x3"]), int(request.form["x4"]), int(request.form["x5"]), int(request.form["x6"]), int(request.form["x7"]), int(request.form["x8"])]
        predict = Linear_Model.predict([xInputs])
        predict = str(round(predict[0]*1000, 2))
        return render_template("results2.html", data = predict)
    else:
        return render_template("results2.html")

@app.route("/home")
def home():
    return render_template("home1.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)

@ app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    #creates a hased version of the password whenever one is submitted
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.static_folder = 'static'
    app.run()
