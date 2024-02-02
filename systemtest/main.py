# https://82.146.35.88:1501/vhyqSfRzzO6eAely/phpmyadmin/index.php?route=/database/structure&server=1&db=school

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("addquestion.html")


@app.route('/addquestion', methods=['POST'])
def addQuestion():
    textQuestion=request.form['text_question']
    selectOne = request.form['select_one']
    selectTwo = request.form['select_two']
    selectThree = request.form['select_three']
    selectFoo = request.form['select_foo']
    answer = request.form['answer']
    print(textQuestion,selectOne,selectTwo,selectThree,selectFoo,answer)
    return redirect("/")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
