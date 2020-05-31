from config.dbconfig import pg_config
from config.tuple_config import user_cons
import psycopg2

#

class SelectedDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def insertSelected(self, requestid, resourceid,ammount):
        cursor = self.conn.cursor()
        query = "insert into selected(requestid,resourceid, ammountselected,dateselected) values (%s,%s,%s,current_date) returning selectedid  "
        cursor.execute(query, (requestid, resourceid,ammount ))
        result = cursor.fetchall()
        query = "update resources set ammount=ammount - %s where resourceid = %s returning ammount"
        cursor.execute(query, ( ammount,resourceid ))
        rest = cursor.fetchone()
        if rest==0:
            query = "update resources set aviable=false where resourceid = %s returning ammount"
            cursor.execute(query, (ammount, resourceid))
            cursor.fetchone()
        self.conn.commit()
        return result