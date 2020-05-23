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
        query = "SELECT transactionid, userid, orderid, resourcetypename, amountordered, paymentmethodname, transaction.cost, transaction.date FROM transaction natural inner join payment_methods natural inner join transaction_orders natural inner join orders natural inner join resources natural inner join resource_type order by resourcetypename;"
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
        query = "select * from transaction natural inner join request where userid = %s"
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

    def getTransactionsByPurchaseType(self,PurchaseTypeNumber):
        cursor = self.conn.cursor()
        query = "SELECT transactionid, firstname,resources.name, ammountordered, paymentmethodname, resources.cost*ammountordered as cost, transaction.date,PurchaseTypeName FROM transaction natural inner join payment_methods natural inner join pays left join orders on pays.orderid=orders.orderid left join resources on orders.resourceid=resources.resourceid natural inner join Purchase_type lef join users on transaction.userid=users.userid where PurchaseTypeNumber = %s ;"
        cursor.execute(query, [PurchaseTypeNumber])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getResourcesFromTransactionByTransactionId(self,transactionid):
        cursor = self.conn.cursor()
        query = "SELECT name, ammount, resourcetypename ,resources.cost, purchasetypename from transaction natural inner join pays left join orders on orders.orderid=pays.orderid left join resources on resources.resourceid=orders.resourceid natural inner join purchase_type natural inner join resource_type where transactionid=%s;"
        cursor.execute(query, [transactionid])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result
    def inserttransaction(self, requestid,paymentmethodnumber,datebought ):
        cursor = self.conn.cursor()
        query = "insert into transaction (paymentmethodnumber, cost, date, requestid) values (%s,(Select sum(ammountselected*cost) from selected natural inner join resources where requestid = %s), %s,%s) returning transactionid;"
        cursor.execute(query, (paymentmethodnumber, requestid,datebought,requestid))
        tid = cursor.fetchall()
        self.conn.commit()
        return tid

    def getTransactionsByPurchaseTypeAndUserId(self, purchadetypenumber, userid):
        cursor = self.conn.cursor()
        query = "Select transactionid, userid , requestid, paymentmethodname , resources.cost,date from transaction natural inner join payment_methods natural inner join request natural inner join selected left join resources on selected.resourceid = resources.resourceid where PurchaseTypeNumber = %s and userid=%s;"
        cursor.execute(query, (purchadetypenumber, userid))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def get_transaction_by_transactionid(self,transactionid):
        cursor = self.conn.cursor()
        query = "Select transactionid, userid , requestid, paymentmethodname , cost,date from transaction natural inner join payment_methods natural inner join request where transactionid = %s"
        cursor.execute(query, (transactionid))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result
