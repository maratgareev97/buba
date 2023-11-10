from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def test():
    return render_template("post_another_postrequest.html")


@app.route('/post', methods=['POST'])
def tset():
    id = request.form['id']
    name = request.form['name']


    return render_template("post_another_postrequest.html",id=id,name=name)
    # return redirect("/")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
