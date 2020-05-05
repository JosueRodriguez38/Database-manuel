from flask import Flask, jsonify, request
# from handler. import ResourcesHandler
from handler.supplier import SupplierHandler
from handler.resource import ResourceHandler
from handler.order import OrderHandler
from handler.User import UserHandler
from handler.Customer import CustomerHandler
# Import Cross-Origin Resource Sharing to enable
# services on other ports on this machine or on other
# machines to access this app
from flask_cors import CORS, cross_origin

# Activate
app = Flask(__name__)
# Apply CORS to this app
CORS(app)


@app.route('/')
def greeting():
    UserHandler().insertUser()
    return 'Hello, this is the Disaster supplies DB App!'


@app.route('/supplier', methods=['GET', 'POST'])  # args(city) #finished
def getAllSuppliers():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return UserHandler().insertSupplierJson(request.json)
    else:
        if not request.args:

            return SupplierHandler().getAllSuppliers()
        else:
            return SupplierHandler().searchSuppliers(request.args)


@app.route('/supplier/<int:sid>', methods=['GET', 'PUT', 'DELETE'])  # finished?
def getSupplierById(sid):
    if request.method == 'GET':
        return SupplierHandler().getSupplierById(sid)
    elif request.method == 'PUT':
        return SupplierHandler().updateSupplier(sid, request.json)
    elif request.method == 'DELETE':
        return SupplierHandler().deleteSupplier(sid)
    else:
        return jsonify(Error="Method not allowed"), 405


@app.route('/resources', methods=['GET', 'POST'])  # args (cost y name)      #terminado?
def getAllresources():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ResourceHandler().insertResourcesJson(request.json)
    else:
        if not request.args:
            return ResourceHandler().getAllResources()
        else:
            return ResourceHandler().searchResources(request.args)


@app.route('/resources/<int:rid>', methods=['GET', 'PUT', 'DELETE'])  # finished?
def getResourceById(rid):
    if request.method == 'GET':
        return ResourceHandler().getResourceById(rid)

    elif request.method == 'PUT':
        return ResourceHandler().insertResourceBySupplierIdJson(rid, request.json)  # by resource id and supplier id

    elif request.method == 'DELETE':
        return ResourceHandler().deleteResource(rid)

    else:
        return jsonify(Error="Method not allowed"), 405


@app.route('/consumer', methods=['POST', 'GET'])  # falta anadir buscar custumers por lugar
def getAllconsumer():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return UserHandler().insertConsumerJson(request.json)
    if request.method == 'GET':
        return CustomerHandler().getAllConsumer()


# fusionar

@app.route('/consumer/<int:cid>', methods=['GET', 'PUT', 'DELETE'])  # finished?
def getConsumerById(cid):
    if request.method == 'GET':

        return CustomerHandler().searchConsumerById(cid)
    elif request.method == 'PUT':

        return CustomerHandler().updateConsumer(cid, request.json)
    elif request.method == 'DELETE':

        return CustomerHandler().deleteConsumer(cid)
    else:
        return jsonify(Error="Method not allowed"), 405


@app.route('/admin', methods=['POST'])  # comentar
def insertAdmin():
    print("REQUEST: ", request.json)
    return UserHandler().insertAdminJson(request.json)


@app.route('/admin/<int:aid>', methods=['GET', 'PUT', 'DELETE'])  # finished?
def getAdminById(aid):
    if request.method == 'GET':

        return UserHandler().getAdmin(aid)
    elif request.method == 'PUT':
        print("REQUEST: ", request.json)
        return UserHandler().insertAdmin(aid, request.json)
    elif request.method == 'DELETE':
        return UserHandler().deleteAdmin(aid)
    else:
        return jsonify(Error="Method not allowed"), 405


@app.route('/orders', methods=['GET', 'POST'])  # finished?
def getAllOrders():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return OrderHandler().insertOrder(request.json)
    else:
        if not request.args:
            return OrderHandler().getAllOrders()
        else:
            return OrderHandler().getOrdersByResourceName(request.args)


@app.route('/orders/<int:oid>', methods=['GET', 'PUT', 'DELETE'])  #
def getOrderById(oid):
    if request.method == 'GET':
        return OrderHandler().getOrderById(oid)
    elif request.method == 'PUT':
        return OrderHandler().updateOrder(oid, request.json)
    elif request.method == 'DELETE':
        return OrderHandler().deleteOrder(oid)
    else:
        return jsonify(Error="Method not allowed"), 405


if __name__ == '__main__':
    app.run()
