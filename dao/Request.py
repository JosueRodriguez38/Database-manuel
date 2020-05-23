from config.dbconfig import pg_config
import psycopg2

# Atributos de Baby Food: (Name, Flavor, Size, Expiration Date, ResourceID)

class RequestDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def insertrequest(self, userid):
        cursor = self.conn.cursor()
        query = "insert into request(userid, status) values(%s,true) returning requestid "
        cursor.execute(query, (userid,))
        result = cursor.fetchall()
        self.conn.commit()
        return result

    def getallrequest(self):
        cursor = self.conn.cursor()
        query = "select requestid,userid,firstname,lastname,status from request natural inner join users order by status "
        cursor.execute(query)
        result = cursor.fetchall()
        self.conn.commit()
        return result

    def getUserRequest(self,userid):
        cursor = self.conn.cursor()
        query = "select requestid,userid,firstname,lastname,status from request natural inner join users where userid = %s order by status "
        cursor.execute(query,[userid])
        result = cursor.fetchall()
        self.conn.commit()
        return result

    def getAllResourcesbyRequestID(self, requestid):
        cursor = self.conn.cursor()
        query = "Select * from selected natural inner join resources where requestid = %s "
        cursor.execute(query, [requestid])
        result = cursor.fetchall()
        self.conn.commit()
        return result

    def getAllResourcesbyResourceName(self, name):
        cursor = self.conn.cursor()
        query = "Select * from selected natural inner join resources where name = %s "
        cursor.execute(query, [name])
        result = cursor.fetchall()
        self.conn.commit()
        return result

    def get_request_by_requestid(self, requestid):
        cursor = self.conn.cursor()
        query = "select * from request where requestid = %s "
        cursor.execute(query, [requestid])
        result = cursor.fetchall()
        self.conn.commit()
        return result