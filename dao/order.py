from config.dbconfig import pg_config
from config.tuple_config import order,user_cons
import psycopg2

class OrderDAO:
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
        r = []
        for row in order:
            r.append(row)
        result.append(r)
        return result

    #   not used in phase 1
    #def getConsumerIdByName(self, firstname, lastname):
        # cursor = self.conn.cursor()
        # query = "select cid from consumer where firstname = %s and lastname = %s;"
        # cursor.execute(query, (firstName, lastName))
        #result = cursor.fetchone()
        #return result

    def getOrderById(self, oid):

        if oid == order[0]:
            return order
        else:
            return

    def getOrderByResourceName(self, rname):

        result = []
        if rname['name'] == 'water':
            for row in order:
                result.append(row)
        return result

    def insert(self, cid,rname, ammountReserved, ammountBought, date):
        if cid == user_cons[0]:
            print("HEREEEEEEEEEEEEEE")
            return 2
        else:
            return

    def update(self, oid, cid,rname,  ammountReserved, ammountBought, date):
        if oid == order[0] and cid == order[1]:
            return oid
        else:
            return

    def delete(self, oid):
        if oid == order[0]:
            return oid
        else:
            return