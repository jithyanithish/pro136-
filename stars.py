from flask import Flask,jsonify,request
from data import data

app=Flask(__name__)
@app.route("/")
def index():
    return jsonify({
        "starsdata":data
    })

@app.route("/star")
def planet():
    name=request.args.get("name")
    starsdata=next(i for i in data if i["name"]==name)
    return jsonify({"data":starsdata})
app.run()