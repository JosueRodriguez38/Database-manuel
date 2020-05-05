from config.dbconfig import pg_config
from config.tuple_config import order,user_cons
import psycopg2



class esencialesDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def insertUserConsumer(self,firstname,lastname,phone,email,status):
        cursor = self.conn.cursor()
        query = "insert into users(accountype, firstname,lastname,phone,email,status) values (2, %s, %s,%true) returning uid;"
        cursor.execute(query, (firstname,lastname,phone,email,status))
        orderid = cursor.fetchone()[0]
        self.conn.commit()
        return orderid

    def insertOrder(self, userid, ammount, date, resourceid):
        cursor = self.conn.cursor()
        query = "insert into orders(uid, paymentmethodnumber,totalcost,datebought) values (%i, %i, %d,%s) returning oid;"
        cursor.execute(query, (userid,ammount,date,resourceid))
        orderid = cursor.fetchone()[0]
        self.conn.commit()
        return orderid


    def getAllResources(self):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName , ammount, cost, purchaseTypeName, name from resources natural inner join resource_type natural inner join purchase_type where aviable = true order by resourcetypenumber;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcebyid(self, resourceid):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName , ammount, cost, purchaseTypeName, name from resources natural inner join resource_type natural inner join purchase_type where aviable = true and resourceid = %s order by resourcetypenumber;"
        cursor.execute(query,[resourceid])
        result = cursor.fetchone()
        self.conn.commit()
        return result

    def getOrdersbyUser(self,userid):
        cursor = self.conn.cursor()
        query = "select * from orders wher userid = %i "
        cursor.execute(query,(userid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrderbyId(self, orderid):
        cursor = self.conn.cursor()
        query = "select * from orders where orderid = %i"
        cursor.execute(query,(orderid))
        result = cursor.fetchone()
        self.conn.commit()
        return result