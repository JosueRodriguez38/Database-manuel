from config.dbconfig import pg_config
from config.tuple_config import order
import psycopg2

class OrdersDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllOrders(self):
       # cursor = self.conn.cursor()
       # query = "select oid, rname, firstname, ammountbought, ammountsreserved, date from order natural join belongs natural join resources natural join consumer natural join user;"
       # cursor.execute(query)
        result = []
        for row in order:
            result.append(row)
        return result

    #   not used in phase 1
    #def getConsumerIdByName(self, firstname, lastname):
        # cursor = self.conn.cursor()
        # query = "select cid from consumer where firstname = %s and lastname = %s;"
        # cursor.execute(query, (firstName, lastName))
        #result = cursor.fetchone()
        #return result

    def getOrderById(self, oid):
        #cursor = self.conn.cursor()
        #query = "select * from order where oid = %s;"
        #cursor.execute(query, (oid,))
        result = []
        for row in order:
            result.append(row)
        return result

    def getOrderByResourceName(self, rname):
        # cursor = self.conn.cursor()
        # query = "select * from order where rname = %s;"
        # cursor.execute(query, (rname,))
        result = []
        for row in order:
            result.append(row)
        return result

    def insert(self, rname, firstName, ammountReserved, ammountBought, date):
        cursor = self.conn.cursor()
        query = "insert into order(pname, pcolor, pmaterial, pprice) values (%s, %s, %s, %s) returning pid;"
        cursor.execute(query, (rname, firstName, ammountReserved, ammountBought, date))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid

    def update(self, oid, rname, firstName, ammountReserved, ammountBought, date):
        cursor = self.conn.cursor()
        query = "update order set pname = %s, pcolor = %s, pmaterial = %s, pprice = %s where oid = %s) values (%s, %s, %s, %s) returning pid;"
        cursor.execute(query, (rname, firstName, ammountReserved, ammountBought, date, oid))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid

    def delete(self, oid):
        cursor = self.conn.cursor()
        query = "delete from order where oid = %s;"
        cursor.execute(query, (oid,))
        self.conn.commit()
        return oid