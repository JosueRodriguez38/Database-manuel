from flask import jsonify
from dao.Transaction import TransactionDAO

class TransactionHandler:
    def build_transaction_dict(self, row):
        result = {}
        result['tid'] = row[0]
        result['uid'] = row[1]
        result['paymentMethod'] = row[2]
        result['cost'] = row[3]
        result['date'] = row[4]
        return result
