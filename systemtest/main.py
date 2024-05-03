# https://82.146.35.88:1501/vhyqSfRzzO6eAely/phpmyadmin/index.php?route=/database/structure&server=1&db=school

from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)


@app.route('/addquestion')
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

    try:
        connection = pymysql.connect(host='82.146.35.88',
                                     user='school',
                                     password='Q1w2e3r4',
                                     db='school',
                                     charset='cp1251',
                                     cursorclass=pymysql.cursors.DictCursor)

        cur = connection.cursor()  # создание курсора
        cur.execute("""INSERT INTO correct (
        textquestion, selectone, selecttwo, selectthree, selectfour, answer)
        VALUES (%s,%s,%s,%s,%s,%s);""",
                    (textQuestion,selectOne,selectTwo,selectThree,selectFoo,answer))  # это сам запрос
        connection.commit()  # подтверждение записи данных

        cur.close()
        connection.close()

        print("Данные внесены")
    except:
        print("Ошибка соединения")

    return redirect("/")

@app.route('/')
def getAllDates():
    try:
        connection = pymysql.connect(host='82.146.35.88',
                                     user='school',
                                     password='Q1w2e3r4',
                                     db='school',
                                     charset='cp1251',
                                     cursorclass=pymysql.cursors.DictCursor)

        cur = connection.cursor()  # создание курсора
        cur.execute("SELECT * FROM correct;")  # это сам запрос
        result = cur.fetchall()  # перевод ответа запроса в виде строки

        cur.close()  # закрытие курсова
        connection.close()  # закрытие соединения
        # for i in result:
        #     print(i)
        #     print(type(i))
        return render_template("all.html", result=result)

    except:
        print("Ошибка соединения")

@app.route("/delete", methods=['POST'])
def deleteString():
    id = request.form['drone']
    connection = pymysql.connect(host='82.146.35.88',
                                 user='school',
                                 password='Q1w2e3r4',
                                 db='school',
                                 charset='cp1251',
                                 cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()  # создание курсора
    cur.execute("""DELETE FROM `correct` WHERE id=%s;""",(id))  # это сам запрос
    connection.commit()  # перевод ответа запроса в виде строки
    cur.close()
    connection.close()
    return redirect("/")

@app.route('/update/<id>')
def izmenit(id):
    try:
        connection = pymysql.connect(host='82.146.35.88',
                                     user='school',
                                     password='Q1w2e3r4',
                                     db='school',
                                     charset='cp1251',
                                     cursorclass=pymysql.cursors.DictCursor)

        cur = connection.cursor()  # создание курсора
        cur.execute("""SELECT * FROM `correct` WHERE id=%s;""",(id))  # это сам запрос
        result = cur.fetchall()  # перевод ответа запроса в виде строки  # подтверждение записи данных

        cur.close()
        connection.close()

        print("Данные внесены")
    except:
        print("Ошибка соединения")
    return render_template("update.html",result=result)

@app.route('/update/<id>', methods=['POST'])
def izmenit_post(id):
    textQuestion = request.form['text_question']
    selectOne = request.form['select_one']
    selectTwo = request.form['select_two']
    selectThree = request.form['select_three']
    selectFoo = request.form['select_foo']
    answer = request.form['answer']
    id = request.form['id']
    print("id ",id)
    try:
        connection = pymysql.connect(host='82.146.35.88',
                                     user='school',
                                     password='Q1w2e3r4',
                                     db='school',
                                     charset='cp1251',
                                     cursorclass=pymysql.cursors.DictCursor)

        cur = connection.cursor()  # создание курсора
        cur.execute("""UPDATE `correct` SET `textquestion`='%s', `selectone`='%s',`selecttwo`='%s', `selectthree`='%s',`selectfour`='%s',`answer`='%s' WHERE id='%s'""", (textQuestion, selectOne, selectTwo, selectThree, selectFoo, answer, id))
        connection.commit()
        print("+++")
        cur.close()
        connection.close()

        print("Данные внесены")
    except:
        print("Ошибка соединения")
    return redirect("/")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
