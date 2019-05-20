from flask import Flask, render_template, request
from random import randint
import random
import math
app = Flask(__name__)
@app.route('/')
def main():
	return render_template("home.html")
#LOGANG CODE





@app.route('/add',methods=["GET","POST"])
def add():
	correct = 0
	r = "1; /add"
	if request.method == "GET":
		o = "+"
		n1,n2 = randint(-50,50),randint(-50,50)
		calcanswer = n1 + n2
		print([o,n1,n2,calcanswer])
		return render_template("thetemplate.html",o=o,n1=n1,n2=n2,calcanswer=calcanswer,correct=correct,r=r)
	else: 
		calcanswer = request.form['calcanswer']
		useranswer = request.form['useranswer']
		n1 = request.form['n1']
		n2 = request.form['n2']
		o = request.form['o']
		print([calcanswer,useranswer,n1,n2,o])
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
		print([o,n1,n2,calcanswer])
		return render_template("thetemplate.html",o=o,n1=n1,n2=n2,calcanswer=calcanswer,correct=correct,r=r)
	else: 
		calcanswer = request.form['calcanswer']
		useranswer = request.form['useranswer']
		n1 = request.form['n1']
		n2 = request.form['n2']
		o = request.form['o']
		print([calcanswer,useranswer,n1,n2,o])
		if calcanswer == useranswer: correct = 1
		else: correct = 2
		return render_template("thetemplate.html",o=o,n1=n1,n2=n2,correct=correct,useranswer=useranswer,r=r)

		
@app.route('/multiply', methods=["GET","POST"])
def multiply():
	correct = 0
	r = "1; /multiply"
	if request.method == "GET":
		o = "x"
		n1,n2 = randint(-12,12),randint(-12,12)
		calcanswer = n1 * n2
		print([o,n1,n2,calcanswer])
		return render_template("thetemplate.html",o=o,n1=n1,n2=n2,calcanswer=calcanswer,correct=correct,r=r)
	else: 
		calcanswer = request.form['calcanswer']
		useranswer = request.form['useranswer']
		n1 = request.form['n1']
		n2 = request.form['n2']
		o = request.form['o']
		print([calcanswer,useranswer,n1,n2,o])
		if calcanswer == useranswer: correct = 1
		else: correct = 2
		return render_template("thetemplate.html",o=o,n1=n1,n2=n2,correct=correct,useranswer=useranswer,r=r)
		
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
		print([o,n1,n2,calcanswer])
		return render_template("thetemplate.html",o=o,n1=n1,n2=n2,calcanswer=calcanswer,correct=correct,r=r)
	else: 
		calcanswer = request.form['calcanswer']
		useranswer = request.form['useranswer']
		n1 = request.form['n1']
		n2 = request.form['n2']
		o = request.form['o']
		print([calcanswer,useranswer,n1,n2,o])
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
            print(calcanswer)
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
			#print('x',x)
		if len(y.split('/')) == 2:
			y = float(y.split('/')[0]) / float(y.split('/')[1])
			#print('y',y)
		x = float(x)
		y = float(y)
		rx = (d-b)/(a-c)
		ry = a*rx + b
		print(x,y)
		print(rx,ry)
		if rx == x and ry == y:
			correct = 1
		else:
			correct = 2
		return render_template('syseq.html',a=a,b=b,c=c,d=d,correct=correct)
