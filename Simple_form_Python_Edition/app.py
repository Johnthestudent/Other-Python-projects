# importing Flask and other modules
from flask import Flask, request, render_template 
import webbrowser
from threading import Timer

# Flask constructor
app = Flask(__name__)   
 
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")
       # getting input with name = lname in HTML form 
       last_name = request.form.get("lname") 
       return "Your name is "+first_name + " " + last_name
    return render_template("index.html")

def open_browser():
      webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":
      Timer(1, open_browser).start()
      app.run(port=5000)
