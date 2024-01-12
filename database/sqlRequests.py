from database import connect


def getAllDates():
    con = connect.connection()
    cur = con.cursor()  # создание курсора
    cur.execute("SELECT * FROM buba;")  # это сам запрос
    result = cur.fetchall()  # перевод ответа запроса в виде строки

    cur.close()  # закрытие курсова
    con.close()  # закрытие соединения

    return result

def addDataRequest(id,name,second_name):
    con = connect.connection()
    cur = con.cursor()  # создание курсора
    cur.execute("""insert into buba(id,name,second_name) values (%s,%s, %s);""",
                (id, name, second_name))  # это сам запрос
    con.commit() # подтверждение записи данных

    cur.close()
    con.close()

def delDataRequest(id):
    con = connect.connection()
    cur = con.cursor()  # создание курсора
    cur.execute("""DELETE FROM buba WHERE id=%s;""",(id))  # это сам запрос
    con.commit()

    cur.close()
    con.close()

def updateDataRequest(id,name, second_name):
    con = connect.connection()
    cur = con.cursor()  # создание курсора
    cur.execute("""UPDATE buba SET name=%s, second_name=%s WHERE id=%s;""",(name, second_name, id))  # это сам запрос
    con.commit()

    cur.close()
    con.close()