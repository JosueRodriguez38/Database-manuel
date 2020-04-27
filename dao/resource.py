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
    def getAllAvailableResources(self):
        cursor = self.conn.cursor()
        query = "select resourceName, reservedAmmount, buyableAmmount from Resources where reservedAmmount > 0 or buyableAmmount > 0"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Resources have an id, this functions finds the resource with the id input, if it exists
    def getResourceById(self, rid):
        cursor = self.conn.cursor()
        query = "select resourceName, reservedAmmount, buyableAmmount, location from Resources where rid = &s"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    # uses the input resource id to find the suppliers that supplies a specific resource
    def getSuppliersByResourcesId(self, pid):
        cursor = self.conn.cursor()
        query = "select sid, sfirstName, sphone from supplies natural inner join supplier where pid = %s;"
        cursor.execute(query, (pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    # AVERIGUAR SI LOS PRECIOS SON IGUALES PARA EL MISMO TIPO DE ARTICULO

    # def getResourcesByNameAndCost(self, name, cost):
    #     result = []
    #
    #     if float(cost) == resource[3] and name == resource[2]:
    #         result.append(resource)
    #
    #     return result



    # returns the resource with the name that is used in the input
    def getResourcesByName(self, resourceName):
        cursor = self.conn.cursor()
        # INCOMPLETO, NEED HELP/EXPLICAME EL QUERY MEJOR
        if(resourceName == "agua" || resourceName == "fuel"):
            query = "select resourceName, ammountReserved, ammountBought from orders natural inner join belongs natural inner join resources natural inner join water natural inner join fuel where "" order by ResourceName "
            cursor.execute(query, (resourceName,))
            result = cursor.fetchone()
            return result
        else:
             query = "select resourceName, ammountReserved, ammountBought from Order where resourceName = %s"
             cursor.execute(query, (resourceName,))
             result = cursor.fetchone()
             return result

    # inserts a resource with its id, supplier id, name, cost, and reserved amount
    def insert(self, sid, rname, cost, resv_amount):

        if sid == resource[1]:
            return resource[0]
        return

    # deletes a resource (specified by id) if it exists
    def delete(self, rid):

        if rid == resource[0]:
            return "ok"
        else:
            return
