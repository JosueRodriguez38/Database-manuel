from config.dbconfig import pg_config
from config.tuple_config import user_cons
import psycopg2

# The purpose of the consumer DAO is to extract the information regarding a consumer that has been requested

class TransactionDAO:   #transaction atributes (tid, uid, paymentmethodnumber,totalcost,datebought)
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getalltransactionsbydate(self, date):
        return


    def getalltransactionsbycard(self, paymentmethod):
        cursor = self.conn.cursor()
        query = "SELECT * FROM transaction where paymentmthodnumber=1"
        cursor.execute(query, paymentmethod)
        users = cursor.fetchone()[0]
        self.conn.commit()
        return users

    def getalltransactionsby_athmovil(self, paymentmethod):
        cursor = self.conn.cursor()
        query = "SELECT * FROM transaction where paymentmthodnumber=2"
        cursor.execute(query, paymentmethod)
        users = cursor.fetchone()[0]
        self.conn.commit()
        return users

    def getalltransactions(self):
         cursor = self.conn.cursor()
         query = "SELECT * FROM transaction"
         cursor.execute(query)
         result = []
         for row in cursor:
             result.append(row)
         return result

    def gettransactionbyuid(self, uid):
        return

    def inserttransaction(self,tid, uid, paymentmethodnumber,totalcost,datebought ):
        cursor = self.conn.cursor()
        query = "insert into transaction(uid, paymentmethodnumber,totalcost,datebought) values (%i, %i, %i,%s) returning uid;"
        cursor.execute(query, (uid, paymentmethodnumber,totalcost,datebought))
        tid = cursor.fetchone()[0]
        self.conn.commit()
        return tid