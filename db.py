import pymysql

host = "192.168.201.180"
user = "root"
password = "qwer1234"
db = "lth_db"
port = 31180
corn = pymysql.connect(host=host, user=user, db=db, password=password,port= port , charset='utf8')
curs = corn.cursor()
sql = "select * from student";
curs.execute(sql)
rows = curs.fetchall()
print(rows)
corn.commit()
corn.close()