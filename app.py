from bs4 import BeautifulSoup
import requests
from flask import Flask,jsonify, render_template,request
from utils import wallpaper
app = Flask(__name__)

@app.route('/img/<string:name>',methods =["GET", "POST"])
def img(name):
    array_of_link  = wallpaper.img(name)
    result = { 
        "links" : array_of_link,
        "Provider" : "nanashi"
               }
    
    return jsonify(result)


@app.route("/",methods =["GET", "POST"])
def home():
    # return render_template("index.html")
    if request.method == "POST":
       # getting input with name = fname in HTML form
        name = request.form.get("name")
       # getting input with name = lname in HTML form 
        array_of_link  = wallpaper.img(name)
        result = { 
        "links" : array_of_link,
        "Provider" : "nanashi"
               }
    
        return render_template("img.html", links=array_of_link)
        
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    