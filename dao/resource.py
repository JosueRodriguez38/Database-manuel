from config.dbconfig import pg_config
from config.tuple_config import resource
import psycopg2

# The purpose of the resource DAO is to extract the information of a resource that has been requested

class ResourcesDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # returns all the resources in the Resources table
    def getAllResources(self):
        result = []
        r = []
        for row in resource:
            r.append(row)
        result.append(r)
        return result

    # Resources have an id, this functions finds the resource with the id input, if it exists
    def getResourceById(self, pid):
        if pid == resource[0]:
            return resource
        else:
            return

    # uses the input resource id to find the suppliers that supplies a specific resource
    def getSuppliersByResourcesId(self, pid):
        cursor = self.conn.cursor()
        query = "select sid, sname, scity, sphone from supplies natural inner join supplier natural inner join supplies where pid = %s;"
        cursor.execute(query, (pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # returns the resources with the same name and cost as the input
    def getResourcesByNameAndCost(self, name, cost):
        result = []

        if float(cost) == resource[3] and name == resource[2]:
            result.append(resource)

        return result

    # returns the resource with the name that is used in the input
    def getResourcesByName(self,name):
        result = []

        if name == resource[2]:
            result.append(resource)

        return result

    # returns the resource with a specified cost
    def getResourcesByCost(self,cost):
        result = []

        if float(cost) == resource[3]:
            result.append(resource)

        return result

    # inserts a resource with its id, supplier id, name, cost, and reserved amount
    def insert(self,sid, rname, cost, resv_amount):

        if sid == resource[1]:
            return resource[0]
        return

    # deletes a resource (specified by id) if it exists
    def delete(self, rid):

        if rid==resource[0]:
            return "ok"
        else:
            return