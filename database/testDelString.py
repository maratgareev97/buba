from flask import Flask, render_template, request, redirect
import sqlRequests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("testdelstring.html")

@app.route('/del', methods=['GET', 'POST'])
def check():
    if request.method=="POST":
        print(request.form["id"])
    return redirect("/")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
