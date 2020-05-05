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

    def getAllTransactions(self):
        cursor = self.conn.cursor()
        query = "SELECT transactionid, userid, orderid, resourcetypename, amountordered, paymentmethodname, transaction.cost, datebought FROM transaction natural inner join payment_methods natural inner join transaction_orders natural inner join order natural inner join resources natural inner join resource_types order by resourcetypename;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllTransactionsByPaymentMethod(self, paymentmethodNumber):
        cursor = self.conn.cursor()
        query = "SELECT transactionid, userid, orderid, resourcetypename, amountordered, paymentmethodname, transaction.cost, datebought FROM transaction natural inner join payment_methods natural inner join transaction_orders natural inner join order natural inner join resources natural inner join resource_types where paymentmthodnumber = %s order by resourcetypename;"
        cursor.execute(query, [paymentmethodNumber,])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllTransactionsByUserID(self, uid):
        cursor = self.conn.cursor()
        query = "SELECT transactionid, userid, orderid, resourcetypename, amountordered, paymentmethodname, transaction.cost, datebought FROM transaction natural inner join payment_methods natural inner join transaction_orders natural inner join order natural inner join resources natural inner join resource_types where uid = %s order by resourcetypename;"
        cursor.execute(query, [uid])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getTransactionsByID(self, tid):
        cursor = self.conn.cursor()
        query = "SELECT transactionid, userid, orderid, resourcetypename, amountordered, paymentmethodname, transaction.cost, datebought FROM transaction natural inner join payment_methods natural inner join transaction_orders natural inner join order natural inner join resources natural inner join resource_types where tid = %s order by resourcetypename;"
        cursor.execute(query, [tid])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllTransactionsByResourceName(self, resourceTypeName):
        cursor = self.conn.cursor()
        query = "SELECT transactionid, userid, orderid, resourcetypename, amountordered, paymentmethodname, transaction.cost, datebought FROM transaction natural inner join payment_methods natural inner join transaction_orders natural inner join order natural inner join resources natural inner join resource_types where resourceTypeName = %s order by resourcetypename;"
        cursor.execute(query, (resourceTypeName,))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getTransactionsByOrderID(self, oid):
        cursor = self.conn.cursor()
        query = "SELECT transactionid, userid, orderid, resourcetypename, amountordered, paymentmethodname, transaction.cost, datebought FROM transaction natural inner join payment_methods natural inner join transaction_orders natural inner join order natural inner join resources natural inner join resource_types where oid = %s order by resourcetypename;"
        cursor.execute(query, [oid])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getTransactionsByDate(self, dateBought):
        cursor = self.conn.cursor()
        query = "SELECT transactionid, userid, orderid, resourcetypename, amountordered, paymentmethodname, transaction.cost, datebought FROM transaction natural inner join payment_methods natural inner join transaction_orders natural inner join order natural inner join resources natural inner join resource_types where dateBought = %s order by resourcetypename;"
        cursor.execute(query, (dateBought,))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllTransactionsByUserIDAndResourceName(self, uid, resourceTypeName):
        cursor = self.conn.cursor()
        query = "SELECT transactionid, userid, orderid, resourcetypename, amountordered, paymentmethodname, transaction.cost, datebought FROM transaction natural inner join payment_methods natural inner join transaction_orders natural inner join order natural inner join resources natural inner join resource_types where uid = %s and resourceTypeName = %s order by resourcetypename;"
        cursor.execute(query, ([uid], resourceTypeName))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result


    def inserttransaction(self,tid, uid, paymentmethodnumber,totalcost,datebought ):
        cursor = self.conn.cursor()
        query = "insert into transaction(uid, paymentmethodnumber,totalcost,datebought) values (%i, %i, %i,%s) returning uid;"
        cursor.execute(query, ([uid], [paymentmethodnumber],[totalcost],datebought))
        tid = cursor.fetchone()[0]
        self.conn.commit()
        return tid