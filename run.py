import os
from flask import Flask, render_template

""" 
   The first argument of the Flask is the name of the applications module - our package. 
   Since we're just using a single module, we can use __name__
   Flask needs this so that it knows where to look for templates and static files
"""   
#we are creating an instance of this and storing it in a variable called app
app = Flask(__name__)


"""
  A decorator is a way of wrapping functions. As in JS all functions are objects
  and can be passed around, so when we try to browse to the root directory as indicated by the "/"
  then flask triggers the index fucntion underneath and returns the Hello, World

"""

#here we use the app.route decorator. A decorator in Python starts with the @ sing
#which is also called a pie notation
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")
    
@app.route("/contact")
def contact():
    return render_template("contact.html")    


@app.route("/careers")
def careers():
    return render_template("careers.html")     
    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)