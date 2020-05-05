from config.dbconfig import pg_config
from config.tuple_config import order,user_cons
import psycopg2

# The purpose of the order DAO is to extract the information of an order that has been requested

class OrderDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # returns all the orders, the items and amounts bought, via a natural join from
    # the tables Resources, Consumer, and User, and the relationship Belongs
    def getAllOrders(self):
        cursor = self.conn.cursor()
        query = "select uid, firstname, lastname, orderid, ammount, dateOrdered, resourceTypeName, purchaseTypeName from order natural inner join order_resource natural inner join Resources natural inner join Resource_Types natural inner join users natural inner join Purchase_Type order by resourcetypenumber"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Returns an order if its id matches the input
    def getOrderById(self, oid):
        cursor = self.conn.cursor()
        query = "select userid, firstname, lastname, ammount, dateOrdered, resourceTypeName, purchaseTypeName from order natural inner join order_resource natural inner join Resources natural inner join Resource_Types natural inner join users natural inner join Purchase_Type where oid = %s order by resourcetypenumber"
        cursor.execute(query, (oid,))
        result = cursor.fetchone()
        self.conn.commit()
        return result

    # Returns the orders that has the resource specified by the input
    def getAllOrdersByResourceName(self, resourceTypeNumber):
        cursor = self.conn.cursor()
        query = "select userid, firstname, lastname, orderid, ammount, dateOrdered, resourceTypeName, purchaseTypeName from order natural inner join order_resource natural inner join Resources natural inner join Resource_Types natural inner join Purchase_Type where resourceTypeNumber = %s"
        cursor.execute(query, (resourceTypeNumber,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getALLOrdersByUserID(self, uid):
        cursor = self.conn.cursor()
        query = "select userid, firstname, lastname, orderid, ammount, dateOrdered, resourceTypeName, purchaseTypeName from order natural inner join order_resource natural inner join Resources natural inner join Resource_Types natural inner join Purchase_Type where resourceTypeNumber = %s order by resourcetypenumber"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByTransactionID(self, tid):
        cursor = self.conn.cursor()
        query = "select userid, firstname, lastname, orderid, ammount, dateOrdered, resourceTypeName, purchaseTypeName from order natural inner join Transaction_orders natural inner join Transaction natural inner join Resources naturalinner join Resource_Type natural inner join Purchase_Type where tid = %s order by resourcetypenumber"
        cursor.execute(query, (tid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByPurchaseType(self, purchaseTypeNumer):
        cursor = self.conn.cursor()
        query = "select userid, firstname, lastname, orderid, ammount, dateOrdered, resourceTypeName, purchaseTypeName from order natural inner join order_resource natural inner join Resources natural inner join Resource_Types natural inner join Purchase_Type where PurchaseTypeNumber = %s order by resourcetypenumber"
        cursor.execute(query, (purchaseTypeNumer,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByDate(self, dateOrdered):
        cursor = self.conn.cursor()
        query = "select userid, firstname, lastname, orderid, ammount, dateOrdered, resourceTypeName, purchaseTypeName from order natural inner join order_resource natural inner join Resources natural inner join Resource_Types natural inner join Purchase_Type where dateOrdered = %s order by resourcetypenumber"
        cursor.execute(query, (dateOrdered,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByResourceNameAndUserID(self, resourceTypeNumber, userid):
        cursor = self.conn.cursor()
        query = "select userid, firstname, lastname, orderid, ammount, dateOrdered, resourceTypeName, purchaseTypeName from order natural inner join order_resource natural inner join Resources natural inner join Resource_Types natural inner join Purchase_Type where resourceTypeNumber = %s and userid = %s"
        cursor.execute(query, (resourceTypeNumber, userid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByPurchaseTypeAndResourceName(self, purchaseTypeNumer, resourceTypeNumber):
        cursor = self.conn.cursor()
        query = "select userid, firstname, lastname, orderid, ammount, dateOrdered, resourceTypeName, purchaseTypeName from order natural inner join order_resource natural inner join Resources natural inner join Resource_Types natural inner join Purchase_Type where purchasetypenumber = %s and resourcetypenumber = %s order by resourcetypenumber"
        cursor.execute(query, (purchaseTypeNumer, resourceTypeNumber,))
        result = []
        for row in cursor:
            result.append(row)
        return result


        # CHECK FILE ESENCIALES
    # # inserts an order, linked to a consumer's id
    # def insert(self, userid,ammount,date,resourceid):
    #     cursor = self.conn.cursor()
    #     query = "insert into transaction(uid, paymentmethodnumber,totalcost,datebought) values (%i, %i, %i,%s) returning uid;"
    #     cursor.execute(query, (userid,ammount,date,resourceid))
    #     orderid = cursor.fetchone()[0]
    #     self.conn.commit()
    #     return orderid



    # updates a consumer's order
    def update(self, orderid, userid,ammount, date,resourceid):
            return

    # deletes an order identified by an input order id
    def delete(self, oid):
            return