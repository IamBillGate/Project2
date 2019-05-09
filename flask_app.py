from flask import Flask, render_template, request
from random import randint
app = Flask(__name__)
@app.route('/')
def main():
	return render_template("home.html")
@app.route('/add',methods=["GET","POST"])
def add():
	correct = 0
	r = "1; /add"
	if request.method == "GET":
		o = "+"
		n1,n2 = randint(-100,100),randint(-100,100)
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
		n1,n2 = randint(-100,100),randint(-100,100)
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
		n1,n2 = randint(-100,100),randint(-100,100)
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
		n1,n2 = randint(-100,100),randint(-100,100)
		calcanswer = n1 / n2
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

@app.route('/exponent', methods=["GET","POST"])
def exponent():
	correct = 0
	r = "1; /exponent"
	if request.method == "GET":
		o = "^"
		n1,n2 = randint(-100,100),randint(-100,100)
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
		
