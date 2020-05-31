from config.dbconfig import pg_config

import psycopg2

# Location Attributes: ADL1, ADL2, city, country, postal code, googleMapURL
#ADL = Address Line

class LocationDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                             pg_config['user'],
                                                             pg_config['passwd'])
        self.conn = psycopg2.connect(connection_url)

    def addlocation(self, ADL1,ADL2,city,country,code,googlemap,userid):
        cursor = self.conn.cursor()
        query = "insert into location(adressline1,adressline2,pueblo,pais,codigopostal,googlemapurl,userid) values (%s, %s, %s,%s,%s,%s,%s) returning locationid ;"
        cursor.execute(query, (ADL1,ADL2,city,country,code,googlemap,userid))
        val = cursor.fetchone()[0]
        self.conn.commit()
        return val