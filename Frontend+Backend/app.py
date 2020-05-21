from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy #We can rep our database structures as classes and you will be hearing those classes as MODELS.
from authentication import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '457486afbc06732795658e96ba989d1a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app) #SQLAlchemy Database Instance Gets Created here. 

class EMPLOYEE(db.Model):
	USER_ID = db.Column(db.Integer, primary_key=True)
	QUALIFICATION = db.Column(db.String(120), unique=False, nullable=False)
	EXPERIENCE = db.Column(db.String(120), nullable=True)
	# image_file = db.Column(db.String(120), nullable=False, nullable=False)
	# password = db.Column(db.String(60), nullable=False)	

	# def __repr__(self):
	# 	return f"User('{}')"


class EMPLOYER(db.Model):
	USER_ID = db.Column(db.Integer, primary_key=True)
	COMPANY_NAME = db.Column(db.String(120), unique=False, nullable=False)
	COMPANY_SIZE = db.Column(db.Integer(20), nullable=False)
	POSITION = db.Column(db.String(20), nullable=False)
	SECTOR = db.Column(db.Integer(20), nullable=False)
	SECTOR_TYPE = db.Column(db.Integer(20), nullable=False)
	WEBSITE = db.Column(db.String(20), nullable=True)


class USERS(db.Model):
	USER_ID = db.Column(db.Integer, primary_key=True)
	NAME = db.Column(db.String(20), unique=False, nullable=False)
	EMAIL_ID = db.Column(db.String(20), nullable=False)
	PASSWORD = db.Column(db.String(20), nullable=False)
	USER_TYPE = db.Column(db.Integer(20), nullable=False)
	PHONE_NUMBER = db.Column(db.String(20), nullable=False)


class REQUIREMENT(db.Model):
	USER_ID = db.Column(db.Integer, primary_key=True)
	POSITION = db.Column(db.String(30), unique=False, nullable=False)
	SKILL_REQ = db.Column(db.String(120), nullable=True)


class SKILLS(db.Model):
	USER_ID = db.Column(db.Integer, primary_key=True)
	SKILL = db.Column(db.String(120), nullable=True)


@app.route('/')
@app.route('/home')
def home():
    return render_template('homePage.html')

@app.route('/about')
def About():
    return render_template('about.html', title='About')

@app.route('/login', methods=['POST', 'GET'])
def login():
	form = LoginForm()
	if request.method == 'POST':
		user = request.form['nm']
		return redirect(url_for('index', usr=index))
	else:  
		return render_template('login.html', title='login', form=form)

@app.route("/userdashboard")
def index(usr):
	return render_template('index.html')


@app.route('/contact', methods=['POST', 'GET'])
def Contact():
	if request.method=='POST':
		"""Add entry to the database here"""
		YourName = request.form.get('name')
		YourEmail = request.form.get('email')
		Subject = request.form.get('subject')
		Message = request.form.get('message')
	return render_template('contact.html')


# @app.route('/signup')
# def SignUp():
#     return render_template('SignUp.html')

# @app.route('/register')
# def register():
#    form = RegistrationForm()
#    return render_template('SignUp.html', title='SignUp', form=form)


if '__name__' == '__main__':
	app.run(debug=True) 