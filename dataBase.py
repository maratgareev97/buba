import pymysql

try:
    connection = pymysql.connect(host='82.146.35.88',
                                         user='school',
                                         password='Q1w2e3r4',
                                         db='school',
                                         charset='cp1251',
                                         cursorclass=pymysql.cursors.DictCursor)
    print("С базой соединились")
except:
    print("Ошибка соединения")


cur = connection.cursor() # создание курсора
cur.execute("SELECT * FROM buba;") # это сам запрос
result = cur.fetchall()  # перевод ответа запроса в виде строки

cur.close() # закрытие курсова
connection.close() # закрытие соединения

print(result)