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
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename,googlemapurl from resources natural inner join supplies natural inner join location natural inner join purchase_type natural inner join resource_type  where aviable = true order by resourcetypename;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # returns resource type name given the resource id
    def getResourceTypeByResourceId(self,resourceid):
        cursor = self.conn.cursor()
        query = "select resourceTypeName,resourceTypeNumber  from Resources natural inner join resource_type where resourceid = %s;"
        cursor.execute(query, [resourceid])
        result = cursor.fetchone()
        self.conn.commit()
        return result

    # Resources have an id, this functions finds the resource with the id input, if it exists
    def getResourceById(self, resourceid):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type where resourceid = %s and aviable = true;"
        cursor.execute(query, [resourceid])
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
    def getAllResourcesByResourceTypeName(self, resourceTypeNumber):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type where resourcetypenumber = %s and aviable = true;"
        cursor.execute(query, (resourceTypeNumber))
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
        query = "select resourceid, orderid, resourceTypeName, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join orders where orderid = %s and aviable = true;"
        cursor.execute(query, (oid,))
        result = cursor.fetchone()
        self.conn.commit()
        return result

    # returns all resource currently being requested
    def getAllResourcesBeingRequested(self):
        cursor = self.conn.cursor()
        query = "select resourceid, orderid, resourceTypeName, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join orders where aviable = true order by resourcetypename;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # returns the resource with a specified cost
    def getAllResourcesOrderedByCost(self, cost):
        cursor = self.conn.cursor()
        query = "select resourceid, orderid, resourceTypeName, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join orders where aviable = true and cost <= 0;"
        cursor.execute(query, cost)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllResourceByUserIDAndResourceTypeName(self, userid, resourceTypeName):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join supplies natural inner join users where userid = %s and resourcetypenumber = %s and aviable = true;"
        cursor.execute(query, (userid, resourceTypeName,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllResourcesByResourceTypeNameAndPurchaseType(self, resourceTypeNumber,purchaseTypeNumber):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type where resourcetypenumber = %s and purchaseTypeNumber = %s and aviable = true;"
        cursor.execute(query, (resourceTypeNumber, purchaseTypeNumber))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByName(self,name):
        cursor = self.conn.cursor()
        query = "select resourceid, name, resourceTypeName, ammount, cost, purchaseTypeName,googlemapurl from Resources natural inner join supplies natural inner join location natural inner join resource_type natural inner join purchase_type where name ~* %s and aviable = true order by name;"
        cursor.execute(query, [name])
        result = []
        for row in cursor:
            result.append(row)
        return result


    # inserts a resource with its id, supplier id, name, cost, and reserved amount
    def insert(self,resourcetypenumber,ammount,cost, name,  purchasetypenumber):
        cursor =self.conn.cursor()
        query ="INSERT INTO resources (resourcetypenumber,ammount,cost,aviable,name,purchasetypenumber) values(%s,%s,%s,true,%s,%s) returning resourceid;"
        cursor.execute(query, (resourcetypenumber,ammount,cost, name,  purchasetypenumber))
        result = cursor.fetchall()
        self.conn.commit()
        return result

    # returns resources added in a given date
    def get_resources_by_date_since(self,date):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename,googlemapurl from resources natural inner join supplies natural inner join location natural inner join purchase_type natural inner join resource_type  where where date>= %s;"
        cursor.execute(query,(date))
        result = cursor.fetchall()
        self.conn.commit()
        return result

    # deletes a resource (specified by id) if it exists
    def delete(self, rid):
            return

    #
    def get_min_resourceid_by_needed_atribute(self, resourcetypenumber, purchasetypenumber, ammountneeded,nameneeded):
        cursor = self.conn.cursor()
        query = "select min(resourceid)from resources where resourcetypenumber=%s and ammount>=%s and resources.purchasetypenumber=%s and name ~* %s resources.aviable=true "
        cursor.execute(query,(resourcetypenumber,ammountneeded,purchasetypenumber,nameneeded))
        results = cursor.fetchone()
        self.conn.commit()
        return results

    # returns a list of all the resources currently needed
    def get_necesitados(self, resourcetypenumber, ammount, purchasetypenumber,name):
        cursor = self.conn.cursor()
        query = "select neededid ,ammountneeded,userid from needed where resourcetypenumber=%s and ammountneeded<=%s and purchasetypenumber=%s and status=true  and nameneeded ~* %s order by ammountneeded asc"
        cursor.execute(query, (resourcetypenumber, ammount, purchasetypenumber,name))
        results = cursor.fetchall()
        self.conn.commit()
        return results

    def get_resource_ammount(self, resourceid):
        cursor = self.conn.cursor()
        query = "select ammount from resources where resourceid = %s"
        cursor.execute(query, (resourceid))
        results = cursor.fetchone()
        self.conn.commit()
        return results
