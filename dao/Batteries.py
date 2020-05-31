from config.dbconfig import pg_config
from config.tuple_config import user_cons
import psycopg2

# Batteries Attributes: name, batteryType quantityPerPack
# The purpose of the batteries DAO is to extract the information of the tuple specified

# getAllBatteries: extracts the batteries attributes plus
# the resource id and typename of every tuple in the batteries table

# getBatteryByResourceId: brings out the tuple with the specified resource id

# getAllBatteriesByBatteryType/Cost: obtains the tuples with the specified battery type or cost

# getAllBatteriesByUserID: obtains the batteries tuple that the userID has bought/reserved

# getBatteryByUserIDAndBatteryType: obtains the tuple that has both the parameters specified.

# insert: adds a new batteries tuple with the specified resourceID, batteryType and quantityPerPack


class BatteriesDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def getAllBatteries(self):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename,baterytype,quantityperpack from  batteries natural inner join resources natural inner join purchase_type natural inner join resource_type  where aviable = true order by baterytype;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getBatteryByResourceId(self, rid):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename,baterytype,quantityperpack,googlemapurl  from  batteries natural inner join resources natural inner join supplies natural inner join location natural inner join purchase_type natural inner join resource_type  where aviable = true and resourceid = %s;"
        cursor.execute(query, [rid])
        result = cursor.fetchone()
        self.conn.commit()
        return result

    def getAllBatteriesByBatteryType(self, batteryType):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename,baterytype,quantityperpack from  batteries natural inner join resources natural inner join purchase_type natural inner join resource_type  where aviable = true and baterytype = %s;"
        cursor.execute(query, (batteryType))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllBatteriesByUserID(self, uid):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename,baterytype,quantityperpack from  batteries natural inner join resources natural inner join purchase_type natural inner join resource_type  where aviable = true and userid = %s order by baterytype;"
        cursor.execute(query, [uid])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllBatteriesByCost(self, cost):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename,baterytype,quantityperpack from  batteries natural inner join resources natural inner join purchase_type natural inner join resource_type  where aviable = true and cost <= %s order by baterytype;"
        cursor.execute(query, [cost])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllBatteriesByUserIDAndBatteryType(self, uid, batteryType):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename,baterytype,quantityperpack from  batteries natural inner join resources natural inner join purchase_type natural inner join resource_type  where aviable = true and userid = %s and baterytype= %s;"
        cursor.execute(query, ([uid], batteryType,))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def insert(self, resourceid, baterytype, quantityperpack):
        cursor = self.conn.cursor()
        query = "insert into batteries(resourceid, baterytype, quantityperpack) values(%s,%s,%s) returning batteriesid"
        cursor.execute(query, (resourceid, baterytype, quantityperpack))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result