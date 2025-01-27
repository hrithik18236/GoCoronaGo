from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy #We can rep our database structures as classes and you will be hearing those classes as MODELS.
import ibm_db
import ibm_db_dbi

app = Flask(__name__)

app.config['SECRET_KEY'] = '457486afbc06732795658e96ba989d1a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/db_gcg'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Connect to DB2


db = SQLAlchemy(app) #SQLAlchemy Database Instance Gets Created here. 

class EMPLOYEEORG(db.Model):
	USERNAME = db.Column(db.String(20), primary_key=True)
	NAME = db.Column(db.String(20),  nullable=False)
	EDUCATION = db.Column(db.String(50), nullable=False)
	INTERNSHIP = db.Column(db.String(120), nullable=True)
	EMAIL_ID = db.Column(db.String(20), nullable=False)
	PASSWORD = db.Column(db.String(20), nullable=False)
	POSOFRESP = db.Column(db.String(120), nullable=True)
	PROJECTS = db.Column(db.String(200), nullable=True)
	SKILLS = db.Column(db.String(150), nullable=False) 
	PHONENO = db.Column(db.String(20), nullable=False)
	# image_file = db.Column(db.String(120), nullable=False, nullable=False)
	# password = db.Column(db.String(60), nullable=False)	


class EMPLOYEEUNORG(db.Model):
	USERNAME = db.Column(db.String(20), primary_key=True)
	NAME = db.Column(db.String(20),  nullable=False)
	EXPERIENCE = db.Column(db.String(150), nullable=True)
	EMAIL_ID = db.Column(db.String(20), nullable=False)
	PASSWORD = db.Column(db.String(20), nullable=False)
	SKILLS = db.Column(db.String(150), nullable=False) 
	PHONENO = db.Column(db.String(20), nullable=False)


class EMPLOYER(db.Model):
	USERNAME = db.Column(db.String(20), primary_key=True)
	NAME = db.Column(db.String(20), nullable=False)
	EMAIL_ID = db.Column(db.String(20), nullable=False)
	COMPANY_NAME = db.Column(db.String(120), unique=False, nullable=False)
	COMPANY_SIZE = db.Column(db.Integer, nullable=False)
	POSITION = db.Column(db.String(20), nullable=False)
	SECTORNAME = db.Column(db.Integer, nullable=False)
	SECTOR_TYPE = db.Column(db.Integer, nullable=False)
	PASSWORD = db.Column(db.String(20), nullable=False)
	WEBSITE = db.Column(db.String(20), nullable=True)
	PHONE = db.Column(db.String(20), nullable=False)


# class USERS(db.Model):
# 	USER_ID = db.Column(db.Integer, primary_key=True)
# 	NAME = db.Column(db.String(20), unique=False, nullable=False)
# 	EMAIL_ID = db.Column(db.String(20), nullable=False)
# 	USER_TYPE = db.Column(db.Integer, nullable=False)
# 	PHONE_NUMBER = db.Column(db.String(20), nullable=False)


class LOGIN(db.Model):     #NEW TABLE
	EMAIL_ID = db.Column(db.String(20), primary_key=True, nullable=False)
	PASSWORD = db.Column(db.String(20), nullable=False)

class REQUIREMENT(db.Model):
	USER_ID = db.Column(db.Integer, primary_key=True)
	POSITION = db.Column(db.String(30), unique=False, nullable=False)
	SKILL_REQ = db.Column(db.String(120), nullable=True)


class SKILLS(db.Model):
	USER_ID = db.Column(db.Integer, primary_key=True)
	SKILL = db.Column(db.String(120), nullable=True)

class CONTACTUS(db.Model):    #NEW TABLE
	YOUR_NAME = db.Column(db.String(20), primary_key=True, nullable=False)
	YOUR_EMAIL = db.Column(db.String(20), unique=False, nullable=False)
	SUBJECT = db.Column(db.String(20), nullable=False)
	MESSAGE = db.Column(db.String(20), nullable=False)
	

@app.route('/')
def home():
	return render_template('homePage.html')

@app.route('/about')
def About():
    return render_template('about.html', title='About')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/RecommendedJobs')
def RecommendedJobs():
    return render_template('recommendedJobs.html')
	
@app.route('/addEducation')
def addEducation():
	return render_template('addEducation.html')

@app.route('/addExperience')
def addExperience():
	return render_template('addExperience.html')

@app.route('/AvailableJobs')
def AvailableJobs():
    return render_template('availableJobs.html')


@app.route('/ResumeBuilder')
def ResumeBuilder():
	return render_template('ResumeBuilder.html')


# employer routing started...
@app.route('/EmployerIndex')
def EmployerIndex():
	return render_template('EmployerIndex.html')


@app.route('/createVacancy')
def createVacancy():
	return render_template('createVacancy.html')

@app.route('/appliedPeople')
def appliedPeople():
	return render_template('appliedPeople.html')

@app.route('/EmployeeProfile')
def EmployeeProfile():
	return render_template('EmployeeProfile.html')


@app.route('/EmployerProfile')
def EmployerProfile():
	return render_template('EmployerProfile.html')


@app.route('/FixMeeting')
def FixMeeting():
	return render_template('FixMeeting.html')


@app.route('/takeMeetings')
def takeMeetings():
	return render_template('takeMeetings.html')


@app.route('/startMeeting')
def startMeeting():
	return render_template('startMeeting.html')


@app.route('/EmployeeInterview')
def EmployeeInterview():
	return render_template('EmployeeInterview.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method=='POST':
		Username = request.form.get('Username')
		Password = request.form.get('Password')
		app.logger.info("******* Username = ", Username)
		app.logger.info("******* Password = ", Password)
		if(Username == "admin" and Password == "admin"):
			return redirect(url_for('index'))
		else:
			return redirect(url_for('login'))


		# entry=LOGIN(EMAIL_ID = Username, PASSWORD = Password)
		# insert = "insert into LOGIN values(?,?)"
		# params = (Username, Password)

	return render_template('login.html')


@app.route('/Employer', methods=['POST','GET'])	
def Employer():
	if request.method=='POST':
		conn.tables('DPS35835', 'EMPLOYER')
		conn_str='database=BLUDB;hostname=dashdb-txn-sbox-yp-dal09-08.services.dal.bluemix.net;port=50000;protocol=tcpip;uid=dps35835;pwd=PleaseGoCovid19@2020'
		ibm_db_conn = ibm_db.connect(conn_str,'','')
		conn = ibm_db_dbi.Connection(ibm_db_conn)
		NAME = str(request.form.get('Name'))
		USERNAME = str(request.form.get('Username'))
		EMAIL_ID = str(request.form.get('Email'))
		SECTOR_TYPE = str(request.form.get('sectType'))
		SECTORNAME = str(request.form.get('SectName'))
		COMPANY_NAME = str(request.form.get('CompName'))
		POSITION = str(request.form.get('Position'))
		COMPANY_SIZE = str(request.form.get('CompSize'))
		# COMPANY_SIZE = int(COMPANY_SIZE)
		PHONE = str(request.form.get('Phone'))
		WEBSITE = str(request.form.get('Website'))
		PASSWORD = str(request.form.get('Password'))
		# entry=EMPLOYER(NAME = NAME, USERNAME = Us,PASSWORD=Password, COMPANY_NAME=CompName,COMPANY_SIZE=CompSize, WEBSITE=Website,POSITION=Position,SECTOR_TYPE=SectType,SECTORNAME=SectName)
		insert = "insert into EMPLOYER values("+NAME+","+USERNAME+","+EMAIL_ID+","+PASSWORD+","+COMPANY_NAME+","+COMPANY_SIZE+","+POSITION+","+PHONE+","+SECTORNAME+","+SECTOR_TYPE+","+WEBSITE+")"
		# params = (NAME,USERNAME,EMAIL_ID,PASSWORD,COMPANY_NAME,COMPANY_SIZE,POSITION,PHONE,SECTORNAME,SECTOR_TYPE,WEBSITE)
		# print(params)
		cur = conn.cursor()
		cur.execute(insert)
		stmt_insert = ibm_db.prepare(ibm_db_conn, insert)
		ibm_db.execute(stmt_insert,params)
	return render_template('Employer.html')

@app.route('/contactus', methods=['POST', 'GET'])
def Contact():
	# select="select * from CONTACTUS"
	# cur = conn.cursor()
	# cur.execute(select)
	# row = cur.fetchall()
	if request.method=='POST':
		"""Add entry to the database here"""
		YourName = request.form.get('name')
		YourEmail = request.form.get('email')
		Subject = request.form.get('subject')
		Message = request.form.get('message')

		# entry=CONTACTUS(YOUR_NAME=name, YOUR_EMAIL=email,SUBJECT=subject,MESSAGE=message)
		# I want to run these 4 lines, when the contactus button is clicked
		insert = "insert into CONTACTUS values(?,?,?,?)"
		params = (YourEmail, YourName, Subject, Message)
		stmt_insert = ibm_db.prepare(ibm_db_conn, insert)
		ibm_db.execute(stmt_insert,params)

	return render_template('contactUs.html')


@app.route('/signup')
def SignUp():
    return render_template('SignUp.html')

@app.route('/sectorType')
def OrganizedOrUnorganized():
    return render_template('OrganizedOrUnorganized.html')  


@app.route('/EmployeeOrganized')
def EmployeeOrganized():
	if request.method=='POST':
		NAME = request.form.get('Name')
		USERNAME = request.form.get('Username')
		EMAIL_ID = request.form.get('Email')
		EDUCATION = request.form.get('Education')
		INTERNSHIP = request.form.get('Internship')
		POSOFRESP = request.form.get('PositionOfResp')
		PROJECTS = request.form.get('Projects')
		SKILLS = request.form.get('Skills')
		PHONENO = request.form.get('Phone')
		PASSWORD = request.form.get('Email')

	return render_template('EmployeeOrganized.html')         



@app.route('/EmployeeUnorganized')
def EmployeeUnorganized():
	if request.method =='POST':
		NAME = request.form.get('Name')
		USERNAME = request.form.get('Username')
		EMAIL_ID = request.form.get('Email')
		EXPERIENCE = request.form.get('Experience')
		SKILLS = request.form.get('Skills')
		PHONE_NO = request.form.get('Phone')
		PASSWORD = request.form.get('Password')

	return render_template('EmployeeUnorganized.html')      

# if '__name__' == '__main__':
app.run(debug=True) 