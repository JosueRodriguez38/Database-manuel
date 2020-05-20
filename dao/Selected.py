from config.dbconfig import pg_config
from config.tuple_config import user_cons
import psycopg2

# Atributos de Baby Food: (Name, Flavor, Size, Expiration Date, ResourceID)

class SelectedDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def insertSelected(self, requestid, resourceid,ammount,date):
        cursor = self.conn.cursor()
        query = "insert into selected(requestid,resourceid, ammountselected,dateselected) values (%s,%s,%s,%s) returning selectedid  "
        cursor.execute(query, (requestid, resourceid,ammount,date ))
        result = cursor.fetchall()
        self.conn.commit()
        return result