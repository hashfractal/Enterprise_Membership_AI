import sys
import pymysql.cursors
from PyQt5.QtWidgets import QApplication

class mySqlDB():
    global connection
    def __init__(self):
        pymysql.version_info = (1, 4, 2, "final", 0)
        pymysql.install_as_MySQLdb()
        global connection
        super().__init__()
        connection = pymysql.connect(
            host='218.237.147.91',
            user='iyrc', 
            passwd='Dodan1004!',              
            db='aisw',
            charset='utf8',    
            port = 3307,
            cursorclass=pymysql.cursors.DictCursor)        
    
    def insert(self,code, name, tel, addr):
        global connection
        connection.connect()
        with connection:
            with connection.cursor() as cursor:                
                sql = "INSERT INTO custom (code, name, tel, addr) \
                            VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (code, name, tel, addr))
                connection.commit()                
                
        connection.close()
        
    def update(self,code,name,tel,addr):
        global connection
        connection.connect()     
        try:
            with connection:
                with connection.cursor() as cursor:                
                    sql = "UPDATE custom SET name = %s, tel = %s, addr = %s WHERE code = %s" 
                    values = (name,tel,addr,code)                    
                    cursor.execute(sql,values )
                    result = cursor.rowcount
                    print(result)
                    connection.commit()                    
            connection.close()           
            return result
        except Exception as e:
            print(e)
            return None
    def customSearch(self, key):
        global connection
        connection.connect()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM custom WHERE code LIKE %s OR name LIKE %s OR tel LIKE %s OR addr LIKE %s"
            key = '%' + key + '%'
            cursor.execute(sql, (key, key, key, key))
            result = cursor.fetchone()
            connection.close()           
        return result
    def delete(self,code):
        global connection
        connection.connect()
        with connection.cursor() as cursor:
            # Read a single record
            sql = "DELETE FROM `custom` WHERE `code` = %s"
            cursor.execute(sql,code)
            connection.commit()
        connection.close()           


if __name__ == "__main__":
    app = QApplication(sys.argv)
    db = mySqlDB()
    # result = db.customInsert('0001','황동하상회','010-2512-6818','지구별 어느 나라')
    # result = db.customInsert('0002','아솔회사','010-1234-0987','M573행성 어느 나라 구석탱이')
    result = db.customSearch('황')
    print(result)    
    app.exit(-1)
    