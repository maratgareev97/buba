from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("amogus.html")


@app.route('/test/<a>&<b>')
def mica(a, b):
    s = int(a) + int(b)
    return render_template("tset.html", output=s, aa=a, bb=b)


@app.route('/request/', methods=['GET'])
def req():
    name = request.args.get("first")
    eman = request.args.get("second")
    print(name,eman)
    if name != None and eman != None:
        name = int(name)
        eman = int(eman)
        s = name + eman
    else:
        s = "У тебя тама какой то NONE"
    print(name)
    return render_template("form.html", getR=s)


@app.route('/ppp')
def editStringBook():
    return render_template("postrequest.html")


@app.route('/ppp/post', methods=['POST'])
def editStringBookPost():
    if request.method == "POST":
        print(request.form['file'])
        id = int(request.form['id'])
        name = request.form['name']
        print(id, name)
        # sqlRequests.updateDataById(id, name, phone, description)
    return redirect("/ppp")

@app.route('/jinja', methods=['GET'])
def jinj():
    print(request.args.get("a"))
    print(request.args.get("b"))
    if request.args.get("a")!=None:
        name = int(request.args.get("a"))
        print(name)
        return render_template("jinj.html",s=name)
    else:
        return render_template("jinj.html",s=0)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
