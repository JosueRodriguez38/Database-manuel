from flask import Flask, jsonify, request
# from handler. import ResourcesHandler
from handler.supplier import SupplierHandler
from handler.resource import ResourceHandler
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


@app.route('/resources', methods=['GET'])
def getAllresources():
    return ResourceHandler().getAllResources()


if __name__ == '__main__':
    app.run()
