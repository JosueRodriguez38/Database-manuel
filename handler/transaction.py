from flask import jsonify
from dao.Transaction import TransactionDAO
from dao.Pays import PaysDAO
from dao.Request import RequestDAO
from dao.Selected import SelectedDAO

class TransactionHandler:
    def build_transaction_dict(self, row):
        result = {}
        result['transactionid'] = row[0]
        result['userid']=row[1]
        result['firstName'] = row[2]
        result['lastName'] = row[3]
        result['paymentMethodName'] = row[4]
        result['requestid'] = row[5]
        result['cost'] = row[6]
        result['date'] = row[7]
        return result

    def searchTransaction(self,args):
        dao= TransactionDAO()
        purchadetypenumber=args.get('type')
        userid=args.get('userid')
        transactionid=args.get('transactionid')

        if purchadetypenumber and userid and not transactionid:
            results = dao.getTransactionsByPurchaseTypeAndUserId(purchadetypenumber,userid)

            result_list = []
            for row in results:
                result_list.append(self.build_transaction_dict(row))
            return jsonify(Transaction=result_list)
        elif purchadetypenumber and not transactionid:
            results=dao.getTransactionsByPurchaseType(purchadetypenumber)
            result_list=[]
            for row in results:
                result_list.append(self.build_transaction_dict(row))
            return jsonify(Transaction=result_list)
        elif userid and not transactionid:
            results = dao.getAllTransactionsByUserID(userid)
            result_list = []
            for row in results:
                result_list.append(self.build_transaction_dict(row))
            return jsonify(Transaction=result_list)
        elif transactionid and not userid and not purchadetypenumber:
            results = dao.get_transaction_by_transactionid(transactionid)
            result_list = []
            for row in results:
                result_list.append(self.build_transaction_dict(row))
            return jsonify(Transaction = result_list)
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
        payment=form.get('paymentmethodnumber')
        date=form.get('date')
        requestid=form.get('requestid')

        if payment and date and requestid:
            tid=dao.inserttransaction(requestid,payment,date)
            if tid:
                return jsonify(PostStatus="new Transaction added with transactionid:" +str(tid))
            else:
                return jsonify(Error="new Transaction couldn't be inserted")
        else:
            return jsonify(Error="invalid Arguments")