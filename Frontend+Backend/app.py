from flask import Flask,request,render_template
import pickle

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("homePage.html")

database={'nachi':'123','james':'aac','karthik':'asdsf'}

@app.route('/login',methods=['POST','GET'])
def login():
    name1=request.form['Username']
    pwd=request.form['Password']
    print(name1)
    print(pwd)
    if name1 not in database:
	    return render_template('login.html',info='Invalid User')
    else:
        return render_template('index.html')

@app.route('/index')
def index():
	return render_template('index.html')	

if __name__ == '__main__':
   	app.run()