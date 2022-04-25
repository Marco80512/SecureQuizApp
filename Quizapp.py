from flask import Flask, url_for, render_template, request, Markup

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/", methods=['GET', 'POST'])
def render_layout():
    return render_template('layout.html')  
    if request.method == 'POST': 
        do_the_Radio_Button() 
    else: 
        show_the_Radio_Button()

    
    
@app.route("/p")
def render_pageI():
    return render_template('page1.html')    
    if request.method == 'POST': 
        do_the_Radio_Button() 
    else: 
        show_the_Radio_Button
    
    
    
@app.route("/pp")
def render_pagez():
    return render_template('page2.html')   
    if request.method == 'POST': 
        do_the_Radio_Button() 
    else: 
        show_the_Radio_Button   
        
        
        
@app.route("/c")
def render_pages():
    return render_template('page3.html')  
  
     
   


    
  
  
if __name__=="__main__":
    app.run(debug=True)

 
