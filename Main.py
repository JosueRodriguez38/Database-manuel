from flask import Flask, jsonify, request
# from handler. import ResourcesHandler
from handler.supplier import SupplierHandler
from handler.resource import ResourceHandler
from handler.order import OrderHandler
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
    return 'Hello, this is the supplies DB App!'


@app.route('/supplier', methods=['GET', 'POST'])
def getAllSuppliers():
    if request.method == 'Post':
        print("REQUEST: ", request.json)
        return SupplierHandler().insertResourcesJson(request.json)
    else:
        if not request.args:
            return SupplierHandler().getAllSuppliers()
        else:
            return SupplierHandler().searchSuppliers(request.agrs)


@app.route('/supplier/<int:sid>', methods=['GET', 'PUT', 'DELETE'])
def getSupplierById(sid):
    if request.method == 'GET':
        return
    elif request.method == 'PUT':
        return
    elif request.method == 'DELETE':
        return
    else:
        return jsonify(Error = "Method not allowed"), 405


@app.route('/resources', methods=['GET', 'POST'])
def getAllresources():
    if request.method == 'Post':
        print("REQUEST: ", request.json)
        return ResourceHandler().insertResourcesJson(request.json)
    else:
        if not request.args:
            return ResourceHandler().getAllResources()
        else:
            return ResourceHandler().searchResources(request.agrs)


@app.route('/Resource/<int:rid>', methods=['GET', 'PUT', 'DELETE'])
def getResourceById(rid):
    if request.method == 'GET':
        return
    elif request.method == 'PUT':
        return
    elif request.method == 'DELETE':
        return
    else:
        return jsonify(Error = "Method not allowed"), 405


@app.route('/consumer', methods=['POST'])
def insertConsumer():
    print("REQUEST: ", request.json)
    return SupplierHandler().insertResourcesJson(request.json)


@app.route('/consumer/<int:cid>', methods=['GET', 'PUT', 'DELETE'])
def getConsumerById(cid):
    if request.method == 'GET':
        return
    elif request.method == 'PUT':
        return
    elif request.method == 'DELETE':
        return
    else:
        return jsonify(Error = "Method not allowed"), 405


@app.route('/admin', methods=['POST'])
def insertAdmin():
    print("REQUEST: ", request.json)
    return SupplierHandler().insertResourcesJson(request.json)


@app.route('/admin/<int:aid>', methods=['GET', 'PUT', 'DELETE'])
def getAdminById(aid):
    if request.method == 'GET':
        return
    elif request.method == 'PUT':
        return
    elif request.method == 'DELETE':
        return
    else:
        return jsonify(Error = "Method not allowed"), 405


@app.route('/orders', methods=['GET', 'POST'])
def getAllOrders():
    if request.method == 'Post':
        print("REQUEST: ", request.json)
        return OrderHandler().insertOrderJson(request.json)
    else:
        if not request.args:
            return OrderHandler().getAllOrders()
        else:
            return OrderHandler().getOrdersByResourceName()


@app.route('/orders/<int:oid>', methods=['GET', 'PUT', 'DELETE'])
def getOrderById(oid):
    if request.method == 'GET':
        return OrderHandler().getOrderById(oid)
    elif request.method == 'PUT':
        return OrderHandler().updateOrder(oid, request.form)
    elif request.method == 'DELETE':
        return OrderHandler().deleteOrder(oid)
    else:
        return jsonify(Error = "Method not allowed"), 405



if __name__ == '__main__':
    app.run()
