import mysql.connector

class Dreamlist_operation():
    
    def get_all_data(self):
        ##取得sf db裡面所有資料
        user = 'root'
        pwd = 'eric8767'

        connection = mysql.connector.connect(host='localhost',
                                            port='3306',
                                            user= user,
                                            password= pwd,
                                            database='discord')

        cursor = connection.cursor() #建立sql server連線

        # 取表格所有資料
        cursor.execute('SELECT * FROM `Dream_list`;')


        reg_string = ''
        records = cursor.fetchall()
        for r in records:
            reg_string += str(r) + '\n'

        cursor.close()
        connection.close()

        return reg_string

    
    def sfdb_insert(self , msg):

        user = 'root'
        pwd = 'eric8767'

        connection = mysql.connector.connect(host='localhost',
                                            port='3306',
                                            user= user,
                                            password= pwd,
                                            database='discord')

        cursor = connection.cursor()

        # 把msg插入表格裡面
        sql_insert = "INSERT INTO `Dream_list` VALUES('" + str(msg) + "');"
        cursor.execute(sql_insert)

        
        cursor.close()
        connection.commit()   ##只要有動到資料的最後都一定要補上這句。
        connection.close()

        return 'insert successful'

    def sfdb_delete(self , msg):

        user = 'root'
        pwd = 'eric8767'

        connection = mysql.connector.connect(host='localhost',
                                            port='3306',
                                            user= user,
                                            password= pwd,
                                            database='discord')

        cursor = connection.cursor()

        #預先設置安全刪除規範
        cursor.execute('SET SQL_SAFE_UPDATES = 0;')

        # 把msg插入表格裡面
        sql_insert = "DELETE FROM `Dream_list` WHERE `todo` = '" + msg + "';"
        cursor.execute(sql_insert)

        
        cursor.close()
        connection.commit()   ##只要有動到資料的最後都一定要補上這句。
        connection.close()

        return 'Delete successful'