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
        query = "select uid, firstname, lastname, oid, ammount, dateOrdered, resourceTypeName, purchaseTypeName from order natural inner join order_resource natural inner join Resources natural inner join Resource_Types natural inner join users natural inner join Purchase_Type"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Returns an order if its id matches the input
    def getOrderById(self, oid):
        cursor = self.conn.cursor()
        query = "select uid, firstname, lastname, ammount, dateOrdered, resourceTypeName, purchaseTypeName from order natural inner join order_resource natural inner join Resources natural inner join Resource_Types natural inner join users natural inner join Purchase_Type where oid = %s"
        cursor.execute(query, (oid,))
        result = cursor.fetchone()
        self.conn.commit()
        return result

    # Returns the orders that has the resource specified by the input
    def getAllOrdersByResourceName(self, resourceTypeNumber):
        cursor = self.conn.cursor()
        query = "select uid, firstname, lastname, oid, ammount, dateOrdered, resourceTypeName, purchaseTypeName from order natural inner join order_resource natural inner join Resources natural inner join Resource_Types natural inner join Purchase_Type where resourceTypeNumber = %s"
        cursor.execute(query, (resourceTypeNumber,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getALLOrdersByUserID(self, uid):
        cursor = self.conn.cursor()
        query = "select uid, firstname, lastname, oid, ammount, dateOrdered, resourceTypeName, purchaseTypeName from order natural inner join order_resource natural inner join Resources natural inner join Resource_Types natural inner join Purchase_Type where resourceTypeNumber = %s"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByTransactionID(self, tid):
        cursor = self.conn.cursor()
        query = "select uid, firstname, lastname, oid, ammount, dateOrdered, resourceTypeName, purchaseTypeName from order natural inner join Transaction_orders natural inner join Transaction natural inner join Resources naturalinner join Resource_Type natural inner join Purchase_Type where tid = %s"
        cursor.execute(query, (tid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByPurchaseType(self, purchsaeTypeNumer):
        cursor = self.conn.cursor()
        query = "select uid, firstname, lastname, oid, ammount, dateOrdered, resourceTypeName, purchaseTypeName from order natural inner join order_resource natural inner join Resources natural inner join Resource_Types natural inner join Purchase_Type where PurchaseTypeNumber = %s"
        cursor.execute(query, (purchsaeTypeNumer,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByDate(self, dateOrdered):
        cursor = self.conn.cursor()
        query = "select uid, firstname, lastname, oid, ammount, dateOrdered, resourceTypeName, purchaseTypeName from order natural inner join order_resource natural inner join Resources natural inner join Resource_Types natural inner join Purchase_Type where dateOrdered = %s"
        cursor.execute(query, (dateOrdered,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # inserts an order, linked to a consumer's id
    def insert(self, cid,rname, ammountReserved, ammountBought, dateOrdered):
            return

    # updates a consumer's order
    def update(self, oid, cid,rname,  ammountReserved, ammountBought, date):
            return

    # deletes an order identified by an input order id
    def delete(self, oid):
            return