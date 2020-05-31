from config.dbconfig import pg_config
from config.tuple_config import user_cons
import psycopg2

# Need = Reserved Goods

class NeededDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def insert_needed(self,resourcetypenumber,userid,purchasetypenumber,ammountneeded,dateneeded,nameneeded):
        cursor = self.conn.cursor()
        query = "insert into needed(resourcetypenumber,userid,purchasetypenumber,ammountneeded,dateneeded,nameneeded,status) values (%s, %s, %s,%s,%s,%s,true) returning neededid;"
        cursor.execute(query, (resourcetypenumber,userid,purchasetypenumber,ammountneeded,dateneeded,nameneeded))
        neededid = cursor.fetchone()
        self.conn.commit()
        return neededid

    def get_needed_by_userid(self,userid):
        cursor = self.conn.cursor()
        query = "select neededid,userid,firstname,lastname, nameneeded, resourcetypename, ammountneeded, purchasetypename, dateneeded,pueblo, googlemapurl from needed natural inner join users natural inner join location natural inner join purchase_type natural inner join resource_type where userid=%s and needed.status=true"
        cursor.execute(query, (userid))
        results = cursor.fetchone()
        self.conn.commit()
        return results

    def get_needed_by_neededid(self,neededid):
        cursor = self.conn.cursor()
        query = "select neededid,userid,firstname,lastname, nameneeded, resourcetypename, ammountneeded, purchasetypename, dateneeded,pueblo, googlemapurl from needed natural inner join users natural inner join location natural inner join purchase_type natural inner join resource_type where neededid=%s and needed.status=true"
        cursor.execute(query, ([neededid]))
        results = cursor.fetchone()
        self.conn.commit()
        return results

    def get_needed_by_nameneeded(self,name):
        cursor = self.conn.cursor()
        query = "select neededid,userid,firstname,lastname, nameneeded, resourcetypename, ammountneeded, purchasetypename, dateneeded,pueblo, googlemapurl from needed natural inner join users natural inner join location natural inner join purchase_type natural inner join resource_type where nameneeded ~* %s and needed.status=true"
        cursor.execute(query, (name))
        results = cursor.fetchone()
        self.conn.commit()
        return results

    def get_needed_by_resourcetypenumber(self, resourcetypenumber):
        cursor = self.conn.cursor()
        query = "select neededid,userid,firstname,lastname, nameneeded, resourcetypename, ammountneeded, purchasetypename, dateneeded,pueblo, googlemapurl from needed natural inner join users natural inner join location natural inner join purchase_type natural inner join resource_type where resourcetypenumber=%s and needed.status=true"
        cursor.execute(query, (resourcetypenumber))
        results = cursor.fetchone()
        self.conn.commit()
        return results

    def get_all_needed(self):
        cursor = self.conn.cursor()
        query = "select neededid,userid,firstname,lastname, nameneeded, resourcetypename, ammountneeded, purchasetypename, dateneeded,pueblo, googlemapurl from needed natural inner join users natural inner join location natural inner join purchase_type natural inner join resource_type where needed.status=true"
        cursor.execute(query)
        results = cursor.fetchall()
        self.conn.commit()

        return results

    def get_needed_by_date_since1(self,date):
        cursor = self.conn.cursor()
        query = "select * from (select count(*) as \"In need\" from needed where status = true and dateneeded>= current_date - interval \'1 days\') as T1, (select count(*) as \"Aviable\" from resources where aviable=true and dateaviable >= current_date - interval \'1 days\') as t2, (select count(*) as \"Matched\"  from atendido natural inner join request natural inner join selected where dateselected >=  current_date - interval \'1 days\' )as t3"
        cursor.execute(query)
        results = cursor.fetchone()
        self.conn.commit()
        return results
    def get_needed_by_date_since7(self,date):
        cursor = self.conn.cursor()
        query = "select * from (select count(*) as \"In need\" from needed where status = true and dateneeded>= current_date - interval \'7 days\') as T1, (select count(*) as \"Aviable\" from resources where aviable=true and dateaviable >= current_date - interval \'7 days\') as t2, (select count(*) as \"Matched\"  from atendido natural inner join request natural inner join selected where dateselected >=  current_date - interval \'7 days\' )as t3"
        cursor.execute(query)
        results = cursor.fetchone()
        self.conn.commit()
        return results

    def update_status(self,neededid, param):
        cursor = self.conn.cursor()
        query = "update needed set status = %s where neededid=%s returning neededid"
        cursor.execute(query,(param,neededid))
        results = cursor.fetchone()
        self.conn.commit()
        return results

    def insert_atendido(self, neededid, requestid):
        cursor = self.conn.cursor()
        query = "insert into atendido(neededid,requestid) values(%s,%s) returning atendidoid"
        cursor.execute(query, ( neededid,requestid))
        results = cursor.fetchone()
        self.conn.commit()
        return results