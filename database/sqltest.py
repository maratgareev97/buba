import connect

def createTable():
    con = connect.connection()
    cur = con.cursor()  # создание курсора
    cur.execute("CREATE TABLE qwestions (id INT PRIMARY KEY AUTO_INCREMENT,  textq VARCHAR(100),    sone VARCHAR(100),    stwo VARCHAR(100),    sthree VARCHAR(100),    sfoo VARCHAR(100),    answer VARCHAR(100));")
    con.commit() # подтверждение записи данных

    cur.close()
    con.close()

createTable()

# CREATE TABLE qwestions (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     textq VARCHAR,
#     sone VARCHAR,
#     stwo VARCHAR,
#     sthree VARCHAR,
#     sfoo VARCHAR,
#     answer VARCHAR
# );