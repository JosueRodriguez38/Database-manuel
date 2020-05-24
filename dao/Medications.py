from config.dbconfig import pg_config
from config.tuple_config import user_cons
import psycopg2

# The purpose of the consumer DAO is to extract the information regarding a consumer that has been requested

class MedicationDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def insert(self, resourceid,activeingredient,description,concentration,quantity, expirationdate):
        cursor = self.conn.cursor()
        query = "INSERT INTO medication (resourceid,activeingredient,description,concentration,quantity, expirationdate) values(%s,%s,%s,%s,%s,%s) returning medicationid"
        cursor.execute(query,(resourceid,activeingredient,description,concentration,quantity, expirationdate))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllMedication(self):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename , ammount, cost, purchasetypename ,activeingredient,description,concentration,quantity,expirationdate from resources natural inner join purchase_type natural inner join resource_type natural inner join medication order by resourceid;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getMedicationByResourceID(self,resourceid):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename , ammount, cost, purchasetypename ,activeingredient,description,concentration,quantity,expirationdate,googlemapurl  from resources  natural inner join supplies natural inner join location natural inner join purchase_type natural inner join resource_type natural inner join medication where resourceid=%s;"
        cursor.execute(query,[resourceid])
        result = cursor.fetchone()
        self.conn.commit()
        return result

    def getMedicationByActiveIngredient(self,active):
        cursor = self.conn.cursor()
        query = "select name,ammount,cost,activeingredient,description,concentration,quantity,expirationdate from medication natural inner join resources where activeingredient=%s;"
        cursor.execute(query,(active))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllMedicationsOrderedByActiveingredientsAsc(self):
        cursor = self.conn.cursor()
        query = "select name,ammount,cost,activeingredient,description,concentration,quantity,expirationdate from medication natural inner join resources order by activeingrediente Asc;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllMedicationsOrderedByActiveingredientsDesc(self):
        cursor = self.conn.cursor()
        query = "select name,ammount,cost,activeingredient,description,concentration,quantity,expirationdate from medication natural inner join resources order by activeingrediente desc;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result
