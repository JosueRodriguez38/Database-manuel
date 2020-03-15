from flask import jsonify
from dao.transaction import TransactionDAO

class TransactionHandler:
    def build_transaction_dict(self, row):
        result = {}
        result['tid'] = row[0]
        result['cid'] = row[1]
        result['cost'] = row[2]
        result['paymentMethod'] = row[3]
        return result

