from flask import Flask, url_for, render_template, request, Markup

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_layout():
    return render_template('layout.html')  

@app.route("/p")
def render_Definition():
    return render_template('page1.html')    

@app.route("/pp")
def render_main():
    return render_template('page2.html')   
        


    
  
  
if __name__=="__main__":
    app.run(debug=True)

 
