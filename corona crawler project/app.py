from flask import Flask, render_template
import matplotlib
import RunSpider

app = Flask(__name__, static_folder="Statics")

@app.route("/")
def crawlInfo():

    # running spider
    RunSpider.runSpider()
    
    # Read information


    # Drawing plot

    return render_template("index.html")
