from flask import Flask, render_template, request, redirect

from database.connect import *

app = Flask(__name__)

@app.route('/')
def zopros():
    con = connection()
    cur = con.cursor()  # создание курсора
    cur.execute("SELECT * FROM buba;")  # это сам запрос
    result = cur.fetchall()  # перевод ответа запроса в виде строки

    cur.close()  # закрытие курсова
    con.close()  # закрытие соединения

    print(result)
    return render_template("zapros.html", res=result)


@app.route('/add', methods=['GET', 'POST'])
def addData():
    if request.method == "POST":
        id = request.form['id']
        name = request.form['name']
        second_name = request.form["second_name"]
    con = connection()
    cur = con.cursor()  # создание курсора
    cur.execute("""insert into buba(id,name,second_name) values (%s,%s, %s);""",
                (id, name, second_name))  # это сам запрос
    con.commit()

    cur.close()
    con.close()
    return redirect("/")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
