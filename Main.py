from flask import Flask, jsonify, request
#from handler. import PartHandler
from handler.supplier import SupplierHandler
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
    return 'Hello, this is the parts DB App!'

@app.route('/suppliers', methods=['GET', 'POST'])
def getAllSuppliers():
    if request.method == 'Post':
        print("REQUEST: ", request.json)
        return SupplierHandler().insertPartJson(request.json)
    else:
        if not request.args:
            return SupplierHandler().getAllSuppliers()
        else:
            return SupplierHandler().searchSuppliers(request.agrs)


if __name__ == '__main__':
    app.run()