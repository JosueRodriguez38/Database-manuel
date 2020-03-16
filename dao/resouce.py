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
        result.append(resource)
        return result

    def getResourcesById(self, pid):
        cursor = self.conn.cursor()
        query = "select pid, pname, pmaterial, pcolor, pprice from supplies where pid = %s;"
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        return result

    def getSuppliersByResourcesId(self, pid):
        cursor = self.conn.cursor()
        query = "select sid, sname, scity, sphone from supplies natural inner join supplier natural inner join supplies where pid = %s;"
        cursor.execute(query, (pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
