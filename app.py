from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import json

app = Flask(__name__)

# ✅ This is your actual working MongoDB Atlas connection
client = MongoClient("mongodb+srv://flaskuser:flaskpass123@cluster0.3uwcffx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["mydatabase"]
collection = db["mycollection"]

@app.route('/api')
def api():
    with open("data.json", "r") as f:
        data = json.load(f)
    return data

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        try:
            collection.insert_one({"name": name, "age": int(age)})
            return redirect(url_for('success'))
        except Exception as e:
            return render_template("form.html", error=str(e))
    return render_template("form.html")

@app.route('/success')
def success():
    return render_template("success.html")

if __name__ == '__main__':
    app.run(debug=True)
