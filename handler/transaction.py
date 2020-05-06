from flask import jsonify
from dao.Transaction import TransactionDAO
from dao.Pays import PaysDAO
class TransactionHandler:
    def build_transaction_dict(self, row):
        result = {}
        result['transactionid'] = row[0]
        result['firstName'] = row[1]
        result['lastName'] = row[2]
        result['name'] = row[3]
        result['ammountOrdered'] = row[4]
        result['paymentMethodName'] = row[5]
        result['cost'] = row[6]
        result['date'] = row[7]
        result['purchaseTypeName'] = row[1]
        return result

    def searchTransaction(self,args):
        dao= TransactionDAO()
        purchadetypenumber=args.get('type')
        userid=args.get('userid')

        if purchadetypenumber and not userid:
            results=dao.getTransactionsByPurchaseType(purchadetypenumber)
            result_list=[]
            for row in results:
                result_list.append(self.build_transaction_dict(row))
            return jsonify(Transaction=result_list)
        elif userid and not purchadetypenumber:
            results = dao.getAllTransactionsByUserID(userid)
            result_list = []
            for row in results:
                result_list.append(self.build_transaction_dict(row))
            return jsonify(Transaction=result_list)

        else:
            return jsonify(ERROR="invalid arguments")

    def getAllResourcesByTransactionId(self,transactionid):
        dao=TransactionDAO()
        results =dao.getResourcesFromTransactionByTransactionId(transactionid)
        #for row in results:
            #result_list.append(self.build_transaction_dict(row))
        return jsonify(Transaction=results)


    def inserttransaction(self,form):
        dao = TransactionDAO( )
        userid=form.get('userid')
        cost=form.get('cost')
        payment=form.get('paymentmethodnumber')
        date=form.get('date')
        orderid=form.get('orderid')
        if userid and payment and date and orderid:
            tid=dao.inserttransaction(userid,payment,cost,date)
            dao = PaysDAO()
            dao.InsertPays(tid,orderid)
            return jsonify(PostStatus="new Transaction added")
        else:
            return jsonify(Error="invalid Arguments")