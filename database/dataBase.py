from flask import Flask, render_template, request, redirect
import sqlRequests

app = Flask(__name__)

@app.route('/')
def zopros():
    result= sqlRequests.getAllDates()
    print(result)
    return render_template("zapros.html", res=result)


@app.route('/add', methods=['GET', 'POST'])
def addData():
    if request.method == "POST":
        id = request.form['id']
        name = request.form['name']
        second_name = request.form["second_name"]
    sqlRequests.addDataRequest(id, name, second_name)
    return redirect("/")

@app.route('/del', methods=['GET', 'POST'])
def delData():
    if request.method == "POST":
        id=request.form["id"]
        sqlRequests.delDataRequest(id)
    return redirect("/")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
