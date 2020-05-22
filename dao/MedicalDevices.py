from config.dbconfig import pg_config
from config.tuple_config import user_cons
import psycopg2

# The purpose of the consumer DAO is to extract the information regarding a consumer that has been requested

class MedicalDeviceDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllMedicalDevices(self):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, name, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join medical_devices where aviable = true order by name;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getMedicalDeviceById(self, rid):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, name, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join medical_devices where aviable = true and resourceid = %s;"
        cursor.execute(query, [rid])
        result = cursor.fetchone()
        self.conn.commit()
        return result

    def getAllMedicalDevicesByUserID(self, uid):
        cursor = self.conn.cursor()
        query = "select resourceid, userid resourceTypeName, name, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join medical_devices natural inner join supplies where aviable = true and userid = %s order by name;"
        cursor.execute(query, [uid])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllMedicalDevicesByName(self, name):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, name, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join medical_devices where aviable = true and name like %s;"
        cursor.execute(query, (name,))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllMedicalDevicesBySpecs(self, specs):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, name, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join medical_devices where aviable = true and specs like %s;"
        cursor.execute(query, (specs,))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def insertMedicalDevices(self, resourceid, specs):
        cursor = self.conn.cursor()
        query = "insert into medical_devices(resourceid,specs) values(%i,%s) returning medicaldeviceid;"
        cursor.execute(query, ([resourceid], specs))
        medicalDevicesid = cursor.fetchone()[0]
        self.conn.commit()
        return medicalDevicesid