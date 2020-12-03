from flask import Flask, render_template
import matplotlib

app = Flask(__name__, static_folder="Statics")

@app.route("/")
def crawlInfo():

    # running spider


    # Read information


    # Drawing plot

    return render_template("index.html")
