from config.dbconfig import pg_config
from config.tuple_config import resource
import psycopg2


class ResourcesDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllResources(self):

        result = []
        r = []
        for row in resource:
            r.append(row)
        result.append(r)
        return result

    def getResourcesById(self, rid):
        if rid == resource[0]:
            return resource
        else:
            return

    def getSuppliersByResourcesId(self, rid):
        cursor = self.conn.cursor()
        query = "select sid, sname, scity, sphone from supplies natural inner join supplier natural inner join supplies where rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByNameAndCost(self, name, cost):
        result = []

        if float(cost) == resource[3] and name == resource[2]:
            result.append(resource)

        return result

    def getResourcesByName(self,name):
        result = []

        if name == resource[2]:
            result.append(resource)

        return result

    def getResourcesByCost(self,cost):
        result = []

        if float(cost) == resource[3]:
            result.append(resource)

        return result

    def insert(self,rid,sid, rname, cost, resv_amount):

        if sid == resource[1]:
            return 3
        return

    def delete(self, rid):

        if rid==resource[0]:
            return "ok"
        else:
            return