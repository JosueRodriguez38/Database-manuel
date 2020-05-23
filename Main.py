from flask import Flask, jsonify, request
from handler.resource import ResourceHandler
from handler.Request import RequestHandler
from handler.User import UserHandler
from handler.transaction import TransactionHandler

# Import Cross-Origin Resource Sharing to enable
# services on other ports on this machine or on other
# machines to access this app
from flask_cors import CORS

# Activate
app = Flask(__name__)
# Apply CORS to this app
CORS(app)


@app.route('/')
def greeting():
    return 'Hello, this is the Disaster supplies DB App!'


@app.route('/user', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return UserHandler().insertUserJson(request.json)
    else:
        if not request.args:

            return UserHandler().getAllUsers()
        else:
            return UserHandler().serachUser(request.args)


@app.route('/user/<int:userid>', methods=['GET', 'PUT', 'DELETE'])
def get_supplier_by_id(userid):
    if request.method == 'GET':
        return UserHandler().getUserById(userid)
    elif request.method == 'PUT':
        return UserHandler().updateUser(userid, request.json)
    elif request.method == 'DELETE':
        return UserHandler().deleteUser(userid)
    else:
        return jsonify(Error="Method not allowed"), 405


@app.route('/resources', methods=['GET', 'POST'])
def get_all_resources():
    if request.method == 'POST':
        return ResourceHandler().insertResourcesJson(request.json)
    else:
        if not request.args:
            return ResourceHandler().getAllResources()
        else:
            return ResourceHandler().searchResources(request.args)


@app.route('/resources/<int:rid>', methods=['GET', 'PUT', 'DELETE'])
def get_resource_by_id(rid):
    if request.method == 'GET':
        return ResourceHandler().getResourceById(rid)

    elif request.method == 'PUT':
        return ResourceHandler().insertResourceBySupplierIdJson(rid, request.json)

    elif request.method == 'DELETE':
        return ResourceHandler().deleteResource(rid)

    else:
        return jsonify(Error="Method not allowed"), 405


@app.route('/request', methods=['POST', 'GET'])
def getRequest():
    if request.method == 'POST':
        return RequestHandler().insertRequest(request.json)
    elif request.method == 'GET':
        if not request.args:
            return RequestHandler().getAllRequest()
        else:
            return RequestHandler().searchRequest(request.args)
    else:
        return  jsonify(Error="Method not allowed"), 405


@app.route('/request/<int:rid>', methods=[ 'GET', 'PUT', 'DELETE'])
def get_requests(rid):
    if request.method == 'GET':
        return RequestHandler().getAllResourcesByRequestId(rid)
    elif request.method == 'PUT':
        return RequestHandler().update_request(rid)
    elif request.method == 'DELETE':
        return RequestHandler().getRequestByRequestID(rid)
    else:
        return jsonify(Error="Method not allowed"), 405


@app.route('/transaction', methods=['GET', 'POST'])
def getAllTransactions():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return TransactionHandler().inserttransaction(request.json)
    else:
        if not request.args:
            return TransactionHandler().getAllTransactions()
        else:
            return TransactionHandler().searchTransaction(request.args)


@app.route('/transaction/<int:tid>', methods=['GET', 'PUT', 'DELETE'])
def getTransactionById(tid):
    if request.method == 'GET':
        return TransactionHandler().getAllResourcesByTransactionId(tid)
    elif request.method == 'PUT':
        return TransactionHandler().updateTransaction(tid, request.json)
    elif request.method == 'DELETE':
        return TransactionHandler().deleteTransaction(tid)
    else:
        return jsonify(Error="Method not allowed"), 405


if __name__ == '__main__':
    app.run()
