# importing Flask and other modules
from xml.dom import minidom
import os
from flask import Flask, request, render_template, json, url_for 
import webbrowser
from threading import Timer

# Flask constructor
app = Flask(__name__)   

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def letmehaveit():
    try:
        filename = os.path.join(app.static_folder, 'data', 'secretsAPI.json')

        with open(filename) as test_file:
            data = json.load(test_file)
        if request.method == "POST":
            # getting input
            secret_number = request.form.get("quantity")
            converted_number = int(secret_number)
            if converted_number == 1:
                presented_secret = data["secrets"][0]["secretText"]
                if(data["secrets"][0]["secretText"]):
                    return "<h1>Secret: </h1>" + f"<h3><i>{presented_secret}</i></h3>" + render_template("secretpresenter.html")
                    #return render_template("secretpresenter.html")
                else:
                    return f"<h1>Secret cannot be found! Please go back to the forms section to create the secret!</h1>"
            elif converted_number == 2:
                presented_secret = data["secrets"][1]["secretText"]
                if(data["secrets"][1]["secretText"]):
                    return "<h1>Secret: </h1>" + f"<h3><i>{presented_secret}</i></h3>" + render_template("secretpresenter.html")
                else:
                    return f"<h1>Secret cannot be found! Please go back to the forms section to create the secret!</h1>"
            elif converted_number == 3:
                presented_secret = data["secrets"][2]["secretText"]
                if(data["secrets"][2]["secretText"]):
                    return "<h1>Secret: </h1>" + f"<h3><i>{presented_secret}</i></h3>" + render_template("secretpresenter.html")
                else:
                    return f"<h1>Secret cannot be found! Please go back to the forms section to create the secret!</h1>"
            elif converted_number == 4:
                presented_secret = data["secrets"][3]["secretText"]
                if(data["secrets"][3]["secretText"]):
                    return "<h1>Secret: </h1>" + f"<h3><i>{presented_secret}</i></h3>" + render_template("secretpresenter.html")
                else:
                    return f"<h1>Secret cannot be found! Please go back to the forms section to create the secret!</h1>"
            elif converted_number == 5:
                presented_secret = data["secrets"][4]["secretText"]
                if(data["secrets"][4]["secretText"]):
                    return "<h1>Secret: </h1>" + f"<h3><i>{presented_secret}</i></h3>" + render_template("secretpresenter.html")
                else:
                    return f"<h1>Secret cannot be found! Please go back to the forms section to create the secret!</h1>"
            elif converted_number == 6:
                presented_secret = data["secrets"][5]["secretText"]
                if(data[5]["secretText"]):
                    return "<h1>Secret: </h1>" + f"<h3><i>{presented_secret}</i></h3>" + render_template("secretpresenter.html")
                else:
                    return f"<h1>Secret cannot be found! Please go back to the forms section to create the secret!</h1>"
            elif converted_number == 7:
                presented_secret = data["secrets"][6]["secretText"]
                if(data[6]["secretText"]):
                    return "<h1>Secret: </h1>" + f"<h3><i>{presented_secret}</i></h3>" + render_template("secretpresenter.html")
                else:
                    return f"<h1>Secret cannot be found! Please go back to the forms section to create the secret!</h1>"
            elif converted_number == 8:
                presented_secret = data["secrets"][7]["secretText"]
                if(data[7]["secretText"]):
                    return "<h1>Secret: </h1>" + f"<h3><i>{presented_secret}</i></h3>" + render_template("secretpresenter.html")
                else:
                    return f"<h1>Secret cannot be found! Please go back to the forms section to create the secret!</h1>"
            elif converted_number == 9:
                presented_secret = data["secrets"][8]["secretText"]
                if(data[8]["secretText"]):
                    return "<h1>Secret: </h1>" + f"<h3><i>{presented_secret}</i></h3>" + render_template("secretpresenter.html")
                else:
                    return f"<h1>Secret cannot be found! Please go back to the forms section to create the secret!</h1>"
            elif converted_number == 10:
                presented_secret = data["secrets"][9]["secretText"]
                if(data[9]["secretText"]):
                    return "<h1>Secret: </h1>" + f"<h3><i>{presented_secret}</i></h3>" + render_template("secretpresenter.html")
                else:
                    return f"<h1>Secret cannot be found! Please go back to the forms section to create the secret!</h1>"
    except Exception:
        return f"<h1>Secret cannot be found! Please go back to the forms section to create the secret!</h1>"
    return render_template("index.html", jsonfile=json.dumps(data))

@app.route('/creatednewfile', methods =["GET", "POST"])
def letcreateit():
    try:
        filename = os.path.join(app.static_folder, 'data', 'secretsAPI.json')

        with open(filename) as test_file:
            data = json.load(test_file)
        if request.method == "POST":
            # getting input
            secret_number1 = request.form.get("quantity2")
            converted_number1 = int(secret_number1)
            if converted_number1 == 1:
                if(data["secrets"][0]["secretText"]):
                    # Serializing json
                    json_object = json.dumps(data["secrets"][0]["secretText"], indent=4)
                    
                    # Writing to sample.json
                    with open("sample.json", "w") as outfile:
                        outfile.write(json_object)
                else:
                    return f"<h1>Secret cannot be found! Please go back to the forms section to create the secret!</h1>"
            elif converted_number1 == 2:
                if(data["secrets"][1]["secretText"]):
                    # Serializing json
                    json_object = json.dumps(data["secrets"][1]["secretText"], indent=4)
                    
                    # Writing to sample.json
                    with open("sample.json", "w") as outfile:
                        outfile.write(json_object)
                else:
                    return f"<h1>Secret cannot be found! Please go back to the forms section to create the secret!</h1>"
            elif converted_number1 == 3:
                if(data["secrets"][2]["secretText"]):
                    # Serializing json
                    json_object = json.dumps(data["secrets"][2]["secretText"], indent=4)
                    
                    # Writing to sample.json
                    with open("sample.json", "w") as outfile:
                        outfile.write(json_object)
                else:
                    return f"<h1>Secret cannot be found! Please go back to the forms section to create the secret!</h1>"
            elif converted_number1 == 4:
                if(data["secrets"][3]["secretText"]):
                    # Serializing json
                    json_object = json.dumps(data["secrets"][3]["secretText"], indent=4)
                    
                    # Writing to sample.json
                    with open("sample.json", "w") as outfile:
                        outfile.write(json_object)
                else:
                    return f"<h1>Secret cannot be found! Please go back to the forms section to create the secret!</h1>"
            elif converted_number1 == 5:
                if(data["secrets"][4]["secretText"]):
                    # Serializing json
                    json_object = json.dumps(data["secrets"][4]["secretText"], indent=4)
                    
                    # Writing to sample.json
                    with open("sample.json", "w") as outfile:
                        outfile.write(json_object)
                else:
                    return f"<h1>Secret cannot be found! Please go back to the forms section to create the secret!</h1>"
    except Exception:
        return "Secret cannot be found! Please go back to the forms section to create the secret!"
    return render_template("index.html", jsonfile=json.dumps(data))              

@app.route('/appendtofile', methods =["GET", "POST"])
def addnewone():
    #with open("sample.json", "w") as outfile:
    if request.method == "POST":
        # Serializing json
        filename = os.path.join(app.static_folder, 'data', 'secretsAPI.json')

        with open(filename) as test_file:
            data = json.load(test_file)
        new_secret = request.form.get("newsecret")
        json_object = json.dumps(new_secret, indent=4)
        # Writing to sample.json
        with open("sample.json", "w") as outfile:
            outfile.write(str(data))
            outfile.write(json_object)
    return render_template("index.html")

def open_browser():
      webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":
      Timer(1, open_browser).start()
      app.run(port=5000)