from config.dbconfig import pg_config
from config.tuple_config import user_cons
import psycopg2

# Ice Attributes: weght

class IceDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # Returns all ice resource in ice table
    def getAllIce(self):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename, weight from ice natural inner join resources natural inner join purchase_type natural inner join resource_type  where aviable = true order by resourceid;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    # Returns information about specific ice with given resource id
    def getIceByResourceID(self, rid):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename, weight,googlemapurl from ice natural inner join resources natural inner join supplies natural inner join location  natural inner join purchase_type natural inner join resource_type  where aviable = true and resourceid = %s;"
        cursor.execute(query, [rid])
        result = cursor.fetchone()
        self.conn.commit()
        return result

    # Returns all ice tuples in the table that are being supplied by the user id given
    def getAllIceByUserID(self, uid):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename, weight from ice natural inner join resources natural inner join purchase_type natural inner join resource_type  where aviable = true and userid = %s order by resourceid;"
        cursor.execute(query, [uid])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    # Returns all ice tuples in the table with matching cost given
    def getIceByCost(self, cost):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename, weight from ice natural inner join resources natural inner join purchase_type natural inner join resource_type  where aviable = true and cost <= %s order by resourceid;"
        cursor.execute(query, [cost])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    # inserts an ice tuple with information given
    def insert(self, resourceid, weight):
        cursor = self.conn.cursor()
        query = "insert into ice (resourceid, weight) values(%s,%s) returning iceid"
        cursor.execute(query, (resourceid, weight))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

