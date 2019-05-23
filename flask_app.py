from flask import Flask, render_template, request, session
from random import randint
import random
import math
import sqlite3
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
@app.route('/')
def main():
	a = False
	try: 
		print(session['email'])
		a = True
	except: pass
	if a == True:
		return render_template("home.html",e=session['email'])
	else: 
		e = "not logged in" 
		return render_template("home.html",e=e)
#LOGANG CODE

@app.route('/logout')
def logout():
    session.pop('email', None)
    session.pop('ID', None)
    session.pop('username', None)
    session.pop('role', None)
    return render_template('logout.html')
@app.route('/exponentssub', methods=['GET','POST'])
def exponentssub():
    correct = 0
    a=0
    b=0
    c=0
    if request.method=='GET':
        a = random.randint(1,12)
        b = random.randint(1,20)
        c = random.randint(1,3)
        calcanswer = a**c - b
        useranswer = 0
        return render_template('exponentssub.html',a=a,b=b,c=c,calcanswer=calcanswer,useranswer=useranswer,correct=correct)
    else:
        calcanswer = int(request.form['calcanswer'])
        useranswer = int(request.form['useranswer'])
        if calcanswer == useranswer:
            correct=1
        else:
            correct=-1
        return render_template('exponentssub.html',a=a,b=b,c=c,calcanswer=calcanswer,useranswer=useranswer,correct=correct)
@app.route('/exponentsadd', methods=['GET','POST'])
def exponentsadd():
	correct = 0
	a=0
	b=0
	c=0
	if request.method=='GET':
		a = random.randint(1,12)
		b = random.randint(1,20)
		c = random.randint(1,3)
		calcanswer = a**c + b
		useranswer = 0
		return render_template('exponentsadd.html',a=a,b=b,c=c,calcanswer=calcanswer,useranswer=useranswer,correct=correct)
	else:
		calcanswer = int(request.form['calcanswer'])
		useranswer = int(request.form['useranswer'])
		a = request.form['a']
		b = request.form['b']
		c = request.form['c']
		if calcanswer == useranswer:
			correct=1
		else:
			correct=-1
		return render_template('exponentsadd.html',a=a,b=b,c=c,calcanswer=calcanswer,useranswer=useranswer,correct=correct)
@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=='GET':
        return render_template('signup.html',display='',session=session)
    else:
        e = request.form['email']
        p = request.form['password']
        confirm = request.form['confirm']
        conn = sqlite3.connect("./static/Main.db")
        c = conn.cursor()
        sql = "SELECT email FROM user"
        c.execute(sql)
        for row in c.fetchall():
            if row[0] == e: return render_template('signup.html',display='Email allready registered',session=session)

        if p!=confirm: return render_template('signup.html',email=e,display='Passwords do not match',session=session)
        
        sql = 'INSERT INTO User (email, password) values(\'{}\',\'{}\')'.format(e,p)
        c.execute(sql)
        conn.commit()
        sql = "SELECT seq FROM sqlite_sequence WHERE name = 'user'"
        c.execute(sql)
        session['email'] = e
        session['ID'] = c.fetchall()[0][0]
        c.close()
        conn.close()
        return render_template('signup.html',display=("Successfully logged in as: " + e),session=session)
		
@app.route('/login',methods=['GET','POST'])
def login():
  if request.method=='GET':
    return render_template('login.html',display='',session=session)
  else:
    conn = sqlite3.connect("./static/Main.db")
    c = conn.cursor()
    sql = "SELECT email, password, id FROM user"
    c.execute(sql)
    msg = "Invalid Credentials"
    e = request.form['email']
    p = request.form['password']
    for row in c.fetchall():
      if row[0]==e and row[1]==p:
        msg = "Successfully logged in as: " + e 
        session['email'] = e
        session['ID'] = row[2]
    c.close()
    conn.close()
    return render_template('login.html',display=msg,session=session)

@app.route('/checklogin')
def checklogin():
  if 'email' in session:
    email = session['email']
    return 'Logged in as ' + email + '<br>' + \
    "<b><a href = '/logout'>click here to log out</a></b>"
  return "You are not logged in <br><a href = '/login'></b>log in</b></a>"



@app.route('/add',methods=["GET","POST"])
def add():
	correct = 0
	r = "1; /add"
	if request.method == "GET":
		o = "+"
		n1,n2 = randint(-50,50),randint(-50,50)
		calcanswer = n1 + n2
		
		return render_template("thetemplate.html",o=o,n1=n1,n2=n2,calcanswer=calcanswer,correct=correct,r=r)
	else: 
		calcanswer = request.form['calcanswer']
		useranswer = request.form['useranswer']
		n1 = request.form['n1']
		n2 = request.form['n2']
		o = request.form['o']
		
		if calcanswer == useranswer: correct = 1
		else: correct = 2
		return render_template("thetemplate.html",o=o,n1=n1,n2=n2,correct=correct,useranswer=useranswer,r=r)
		
@app.route('/subtract', methods=["GET","POST"])
def subtract():
	correct = 0
	r = "1; /subtract"
	if request.method == "GET":
		o = "-"
		n1,n2 = randint(-50,50),randint(-50,50)
		calcanswer = n1 - n2
		
		return render_template("thetemplate.html",o=o,n1=n1,n2=n2,calcanswer=calcanswer,correct=correct,r=r)
	else: 
		calcanswer = request.form['calcanswer']
		useranswer = request.form['useranswer']
		n1 = request.form['n1']
		n2 = request.form['n2']
		o = request.form['o']
	
		if calcanswer == useranswer: correct = 1
		else: correct = 2
		return render_template("thetemplate.html",o=o,n1=n1,n2=n2,correct=correct,useranswer=useranswer,r=r)

		
@app.route('/multiply', methods=['GET','POST'])
def multiply():
    correct = 0
    if request.method=='GET':
        a = random.randint(-50,50)
        b = random.randint(-50,50)
        c = random.randint(-50,50)
        calcanswer = a*b*c
        useranswer=0
        return render_template('multiply.html',a=a,b=b,c=c,calcanswer=calcanswer,useranswer=useranswer,correct=correct)
    else:
        a = request.form['a']
        b = request.form['b']
        c = request.form['c']
        calcanswer = int(a)*int(b)*int(c)
        useranswer = request.form['useranswer']
        if request.form['useranswer'].strip() == request.form['calcanswer'].strip():
            correct=1
        else:
            correct=-1
        return render_template('multiply.html',a=a,b=b,c=c,calcanswer=calcanswer,useranswer=useranswer,correct=correct)
		
@app.route('/divide', methods=["GET","POST"])
def divide():
	correct = 0
	r = "1; /divide"
	if request.method == "GET":
		o = "/"
		n1,n2 = randint(-12,12),randint(-12,12)
		while n2 ==0:
			n1,n2 = randint(-12,12),randint(-12,12)
		calcanswer = n1 / n2
		return render_template("thetemplate.html",o=o,n1=n1,n2=n2,calcanswer=calcanswer,correct=correct,r=r)
	else: 
		calcanswer = request.form['calcanswer']
		useranswer = request.form['useranswer']
		n1 = request.form['n1']
		n2 = request.form['n2']
		o = request.form['o']
		useranswer = float(useranswer)
		try: useranswer = int(useranswer)
		except: pass
		calcanswer = float(calcanswer)
		try: calcanswer = int(calcanswer)
		except: pass
		calcanswer = round(calcanswer, 2)
		useranswer = round(useranswer, 2)
		if calcanswer == useranswer: correct = 1
		else: correct = 2
		return render_template("thetemplate.html",o=o,n1=n1,n2=n2,correct=correct,useranswer=useranswer,r=r)

@app.route('/exponent', methods=["GET","POST"])
def exponent():
	correct = 0
	r = "1; /exponent"
	if request.method == "GET":
		o = "^"
		n1,n2 = randint(-10,10),randint(-2,3)
		calcanswer = n1 ** n2
	
		return render_template("thetemplate.html",o=o,n1=n1,n2=n2,calcanswer=calcanswer,correct=correct,r=r)
	else: 
		calcanswer = request.form['calcanswer']
		useranswer = request.form['useranswer']
		n1 = request.form['n1']
		n2 = request.form['n2']
		o = request.form['o']
		
		if calcanswer == useranswer: correct = 1
		else: correct = 2
		return render_template("thetemplate.html",o=o,n1=n1,n2=n2,correct=correct,useranswer=useranswer,r=r)	
		
		
#Gross other code		
@app.route('/multiplytwo', methods=['GET','POST'])
def multiplytwo():
    correct = 0
    if request.method=='GET':
        a = random.randint(1,25)
        b = random.randint(1,25)
        calcanswer = a*b
        useranswer=0
        return render_template('multiplytwo.html',a=a,b=b,calcanswer=calcanswer,useranswer=useranswer,correct=correct)
    else:
        a = request.form['a']
        b = request.form['b']
        calcanswer = int(a)*int(b)
        useranswer = request.form['useranswer']
        if request.form['useranswer'].strip() == request.form['calcanswer'].strip():
            correct=1
        else:
            correct=-1
        return render_template('multiplytwo.html',a=a,b=b,calcanswer=calcanswer,useranswer=useranswer,correct=correct)



@app.route('/exponents', methods=['GET','POST'])
def exponents():
    correct = 0
    if request.method=='GET':
        a = random.randint(1,10)
        b = random.randint(1,5)
        calcanswer = a**b
        useranswer=0
        return render_template('exponents.html',a=a,b=b,calcanswer=calcanswer,useranswer=useranswer,correct=correct)
    else:
        a = request.form['a']
        b = request.form['b']
        calcanswer = int(a)**int(b)
        useranswer = request.form['useranswer']
        if request.form['useranswer'].strip() == request.form['calcanswer'].strip():
            correct=1
        else:
            correct=-1
        return render_template('exponents.html',a=a,b=b,calcanswer=calcanswer,useranswer=useranswer,correct=correct)
		
@app.route('/pythago',methods=['GET','POST'])
def pythago():
    correct = 0
    img = random.randint(1,5)
    if request.method=='GET':
        a = random.randint(1,15)
        b = random.randint(1,15)
        calcanswer = round(math.sqrt((a*a)+(b*b)),2)
        useranswer=0
        return render_template('pythag.html',a=a,b=b,calcanswer=calcanswer,useranswer=useranswer,correct=correct,img=img)
    else:
        a = request.form['a']
        b = request.form['b']
        calcanswer = round(math.sqrt((int(a)* int(a))+(int(b)*int(b))),2)
        useranswer = request.form['useranswer']
        if request.form['useranswer'].strip() == request.form['calcanswer'].strip():
            correct=1
        else:
            correct=-1
        return render_template('pythag.html',a=a,b=b,calcanswer=calcanswer,useranswer=useranswer,correct=correct,img=img)
@app.route('/addfractions', methods=['GET','POST'])
def addfractions():
    correct = 0
    if request.method=='GET':
        a = random.randint(1,10)
        b = random.randint(2,6)
        c = random.randint(1,10)
        d = random.randint(2,6)
        calcanswer = (a/b)+(c/d)
        useranswer=0
        return render_template('addtwofractions.html',a=a,b=b,c=c,d=d,calcanswer=calcanswer,useranswer1=useranswer,useranswer2=useranswer,correct=correct)
    else:
        a = request.form['a']
        b = request.form['b']
        c = request.form['c']
        d = request.form['d']
        calcanswer = (int(a)/int(b))+(int(c)/int(d))
        useranswer1 = int(request.form['useranswer1'])
        useranswer2 = int(request.form['useranswer2'])
        useranswerfull = useranswer1/useranswer2
        if useranswerfull == calcanswer:
            correct=1
        else:
            correct=-1
            
        return render_template('addtwofractions.html',a=a,b=b,c=c,d=d,calcanswer=calcanswer,useranswer1=useranswer1,useranswer2=useranswer2,correct=correct)

@app.route('/syseq',methods=['GET','POST'])
def syseq():
	correct = 0
	if request.method == 'GET':
		# ax + b = y, cx + d = y
		a = random.randint(-10,10)
		b = random.randint(-10,10)
		c = random.randint(-10,10)
		d = random.randint(-10,10)
		return render_template('syseq.html',a=a,b=b,c=c,d=d,correct=correct)
	else:
		a = int(request.form['a'])
		b = int(request.form['b'])
		c = int(request.form['c'])
		d = int(request.form['d'])
		x = request.form['x']
		y = request.form['y']
		if len(x.split('/')) == 2:
			x = float(x.split('/')[0]) / float(x.split('/')[1])
			
		if len(y.split('/')) == 2:
			y = float(y.split('/')[0]) / float(y.split('/')[1])
	
		x = float(x)
		y = float(y)
		rx = (d-b)/(a-c)
		ry = a*rx + b
	
		if rx == x and ry == y:
			correct = 1
		else:
			correct = 2
		return render_template('syseq.html',a=a,b=b,c=c,d=d,correct=correct)

@app.route('/special',methods=['GET','POST'])
def spec():
    correct = 0
    prob = random.randint(1,3)
    img = random.randint(1,2)
    x = 0
    calcanswer = 0
    useranswer = 0
    if request.method=='GET':
        if prob == 1:
            x = 'trip'
            calcanswer = 'trip'
            useranswer = 0
            return render_template('special.html',img=img,x=x,calcanswer=calcanswer,useranswer=useranswer,correct=correct)
        elif prob == 2:
            x = 'thir'
            calcanswer = 'thir'
            useranswer = 0
            return render_template('special.html',img=img,x=x,calcanswer=calcanswer,useranswer=useranswer,correct=correct)
        elif prob == 3:
            x = 'four'
            calcanswer = 'four'
            useranswer = 0
            return render_template('special.html',img=img,x=x,calcanswer=calcanswer,useranswer=useranswer,correct=correct)
    else:
        img = request.form['img']
        x = request.form['x']
        useranswer = request.form['useranswer']
        if request.form['useranswer'].strip() == request.form['calcanswer'].strip():
            correct=1
        else:
            correct=-1
        return render_template('special.html',calcanswer=calcanswer,useranswer=useranswer,correct=correct,img=img,x=x)