from config.dbconfig import pg_config
from config.tuple_config import user_cons
import psycopg2

# The purpose of the consumer DAO is to extract the information regarding a consumer that has been requested

class PowerGeneratorDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllPowerGenerators(self):
        cursor = self.conn.cursor()
        query = "select name,ammount,cost,generatorfuel,capacity,size from power_generator natural inner join resources ;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getPowerGeneratorByResourceID(self,resourceID):
        cursor = self.conn.cursor()
        query = "select name,ammount,cost,generatorfuel,capacity,size from power_generator natural inner join resources where resourceid=%i;"
        cursor.execute(query,[resourceID])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getPowerGeneratorByGeneratorFuel(self,generatorfuel):
        cursor = self.conn.cursor()
        query = "select name,ammount,cost,generatorfuel,capacity,size from power_generator natural inner join resources where generatorfuel=%s order by generatorfuel;"
        cursor.execute(query,(generatorfuel))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def insertPowerGenerators(self, rid, generatorFuel, capacity, size):
        cursor = self.conn.cursor()
        query = "insert into cards(resourceid,generatorfuel,capacity,size) values(%i,%s,%s,%s) returning powergeneratorid;"
        cursor.execute(query, ([rid], generatorFuel, capacity, size))
        powerGenid = cursor.fetchone()[0]
        self.conn.commit()
        return powerGenid