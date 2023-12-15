from connect import *
def getAllDates():
    con = connection()
    cur = con.cursor()  # создание курсора
    cur.execute("SELECT * FROM buba;")  # это сам запрос
    result = cur.fetchall()  # перевод ответа запроса в виде строки

    cur.close()  # закрытие курсова
    con.close()  # закрытие соединения

    print(result)