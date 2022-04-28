from flask import Flask, url_for, render_template, request, Markup

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/", methods=['GET', 'POST'])
def render_layout():
    session.clear()
    return render_template('layout.html')  
   
    

    
    
@app.route("/p")
def render_pageI():
    session["q1"] = request.form["President"]
    return render_template('page1.html')    
   
    
    
@app.route("/pp")
def render_pagez():
    session["q2"] = request.form["SAO"]
    return render_template('page2.html')   
    
        
        
@app.route("/c")
def render_pages():
    session["q3"] = request.form["Money"]
    if session ["q1"] == "Alexander Hamilton":
        Markup 
    return render_template('page3.html',Results=) 
    
    
  
     
   


    
  
  
if __name__=="__main__":
    app.run(debug=True)

 
