from config.dbconfig import pg_config
from config.tuple_config import user_cons
import psycopg2

# This DAO class handles methods regarding orders that are with paid goods

class PaysDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def getAllOrdersOfaTransaction(self,transactionid):
        cursor = self.conn.cursor()
        query ="SELECT name, ammountordered, resources.cost , purchasetypename from pays natural inner join orders natural inner join resources natural inner join purchase_type where transactionid = %s order by name;"
        cursor.execute(query, [transactionid])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getOrdersIdByTransactionId(self,transactionid):
        cursor = self.conn.cursor()
        query = "SELECT orderid from pays natural inner join orders where transactionid = %s;"
        cursor.execute(query, [transactionid])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def InsertPays(self, transactionid,orderid):
        cursor = self.conn.cursor()
        query = "insert into pays(transactionid,orderid) values(%s,%s)returning paysid;"
        cursor.execute(query,(transactionid,orderid))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def deletePays(self,payid):
        return