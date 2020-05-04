from config.dbconfig import pg_config
from config.tuple_config import resource
import psycopg2

# The purpose of the resource DAO is to extract the information of a resource that has been requested

class ResourcesDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # returns all the resources in the Resources table
    def getAllResources(self):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type where aviable = true order by resourcetypename;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Resources have an id, this functions finds the resource with the id input, if it exists
    def getResourceById(self, resourceid):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type where resourceid = %s and aviable = true order by resourcetypename;"
        cursor.execute(query, (resourceid,))
        result = cursor.fetchone()
        self.conn.commit()
        return result

    # uses the input resource id to find the suppliers that supplies a specific resource
    def getAllResourceByUserID(self, userid):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join supplies natural inner join users where userid = %s and aviable = true order by resourcetypename;"
        cursor.execute(query, (userid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # returns the resources with the same name and cost as the input
    def getAllResourcesByName(self, resourceTypeNumber):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type where resourcetypenumber = %s and aviable = true order by;"
        cursor.execute(query, (resourceTypeNumber,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # returns the resource with the name that is used in the input
    def getAllResourcesByPurchaseType(self, purchaseTypeNumber):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type where purchasetypenumber = %s and aviable = true order by resourcetypename;"
        cursor.execute(query, (purchaseTypeNumber,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllResourcesByOrderID(self, oid):
        cursor = self.conn.cursor()
        query = "select resourceid, orderid, resourceTypeName, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type where orderid = %s and aviable = true order by resourcetypename;"
        cursor.execute(query, (oid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllResourcesBeingRequested(self):
        cursor = self.conn.cursor()
        query = "select resourceid, orderid, resourceTypeName, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type aviable = true order by resourcetypename;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # returns the resource with a specified cost
    def getAllResourcesOrderedByCost(self):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type where aviable = true group by cost;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # inserts a resource with its id, supplier id, name, cost, and reserved amount
    def insert(self,sid, rname, cost, resv_amount):
        return

    # deletes a resource (specified by id) if it exists
    def delete(self, rid):
            return