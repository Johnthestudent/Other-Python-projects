from flask import Flask, render_template
import webbrowser
from threading import Timer

app = Flask(__name__)

@app.route('/')
def enteringgame():
	return render_template('index.html')

def open_browser():
      webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":
      Timer(1, open_browser).start()
      app.run(port=5000)