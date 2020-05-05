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

    def getAllMedication(self):
        cursor = self.conn.cursor()
        query = "select name,ammount,cost,activeingredient,description,concentration,quantity,expirationdate from medication natural inner join resources order by name;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getMedicationByResourceID(self,resourceid):
        cursor = self.conn.cursor()
        query = "select name,ammount,cost,activeingredient,description,concentration,quantity,expirationdate from medication natural inner join resources where resourceid=%i;"
        cursor.execute(query,[resourceid])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
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
