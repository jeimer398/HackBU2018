from flask import Flask, render_template, request
import sys
from auth import *

app = Flask(__name__, static_folder='static', static_url_path='/static', template_folder="../HackBU2018/site")

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/contact.php')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/preauth/')
def preauth():
	auth_url = start_auth()
	return redirect(auth_url);



if __name__ == "__main__":
    app.run(debug=True)
