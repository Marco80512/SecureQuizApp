from flask import Flask, url_for, render_template, request, Markup, session
import os

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

app.secret_key = os.environ['SECRET_KEY']

@app.route("/")
def render_layout():
    session.clear()
    return render_template('layout.html')  
   
    

    
    
@app.route("/p",methods=['GET', 'POST'])
def render_pageI():
    if "q1" not in session:
        session["q1"] = request.form["President"]
    return render_template('page1.html')    
   
    
    
@app.route("/pp",methods=['GET', 'POST'])
def render_pagez():
    if "q2" not in session:
        session["q2"] = request.form["SAO"]
    return render_template('page2.html')   
    
    
    
        
        
@app.route("/c",methods=['GET', 'POST'])
def render_pages():
    if "q3" not in session:
        session["q3"] = request.form["Money"]
    results= ""
    if session ["q1"] == "GW":
       results += Markup ('<div class="green"></div>')
    else: 
        results += Markup ('<div class="red"></div>')
        
    if session ["q2"] == "KK":
       results += Markup ('<div class="green"></div>')
    else: 
        results += Markup ('<div class="red"></div>')  
        
    if session ["q3"] == "AH":
       results += Markup ('<div class="green"></div>')
    else: 
        results += Markup ('<div class="red"></div>')  
    
    return render_template('page3.html',Results=results) 
    

    
  
  
if __name__=="__main__":
    app.run(debug=True)

 
