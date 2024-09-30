import pymysql

# dbinfo =
{
    "host": "182.365.5.1",
    "post" : 3306,
    "user" : "",
    "password":"",
    "database":""
}

class Db:
    def __init__(self, dbinfo):
        self.conn = pymysql.connect(**dbinfo)
        self.cur = self.conn.cursor()

    def dbselect(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchall()
        print(result)

    def dbcommit(self, sql):
        self.cur.execute(sql)
        self.conn.commit()

    def dbclose(self):
        self.cur.close()
        self.conn.close()
