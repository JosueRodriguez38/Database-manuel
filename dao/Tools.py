from config.dbconfig import pg_config
from config.tuple_config import user_cons
import psycopg2

# The purpose of the consumer DAO is to extract the information regarding a consumer that has been requested

class ToolsDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def getToolByResourceId(self,resourceid):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename,size,googlemapurl  from  tool natural inner join resources  natural inner join supplies natural inner join location natural inner join purchase_type natural inner join resource_type  where resourceid=%s;"
        cursor.execute(query,[resourceid])
        result = cursor.fetchone()
        self.conn.commit()
        return result

    def getALlTools(self):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename,size from  tool natural inner join resources natural inner join purchase_type natural inner join resource_type ;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllToolSortedBySizeAsc(self):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename,size from  tool natural inner join resources natural inner join purchase_type natural inner join resource_type  order by size asc;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllToolSortedBySizeDes(self):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename,size from  tool natural inner join resources natural inner join purchase_type natural inner join resource_type  order by size desc;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result
    def insertTools(self,resourceid,size):
        cursor = self.conn.cursor()
        query = "insert into tool(resourceid,size) values(%s,%s) returning toolid;"
        cursor.execute(query, [resourceid, size])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result