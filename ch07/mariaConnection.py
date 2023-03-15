import pymysql

# Maria연결에 필요한 host랑 
db = pymysql.connect(host='localhost',user='root',password ='1234',db='mariaSample' ,charset='utf8')
# 데이터베이스 연결
cur = db.cursor()
# query를 선언하고 
cur.execute('SELECT * from tblRegister')
# query실행
rows = cur.fetchall()
print(rows)
db.close()