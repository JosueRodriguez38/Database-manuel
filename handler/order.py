from flask import jsonify
from dao.order import OrderDAO

# Builds and inserts orders via the use or the order DAO

class OrderHandler:

    # builds a skeleton order tuple
    def build_order_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['firstName'] = row[1]
        result['lastName'] = row[2]
        result['oid'] = row[3]
        result['amount'] = row[4]
        result['dateOrdered'] = row[5]
        result['resourceTypeName'] = row[6]
        result['PurchaseTypeName'] = row[7]
        return result

    # defines each of the order's attributes
    def build_order_attributes(self, uid, firstName, lastName, oid, amount, dateOrdered, resourceTypeName, PurchaseTypeName):
        result = {}
        result['uid'] = uid
        result['firstName'] = firstName
        result['lastName'] = lastName
        result['oid'] = oid
        result['amount'] = amount
        result['dateOrdered'] = dateOrdered
        result['resourceTypeName'] = resourceTypeName
        result['PurchaseTypeName'] = PurchaseTypeName
        return result

    # obtains a list of all the orders, compiles them in a list, which is then jsonified
    def getAllOrders(self):
        dao = OrderDAO()
        orders_list = dao.getAllOrders()
        result_list = []
        for row in orders_list:
            result = self.build_order_dict(row)
            result_list.append(result)
        return jsonify(Orders=result_list)

    # Uses DAO method to find the order, uses json messages to denote success or failure
    def getOrderById(self, oid):
        dao = OrderDAO()
        row = dao.getOrderById(oid)
        if not row:
            return jsonify(Error= "Order Not Found"), 404
        else:
            order = self.build_order_dict(row)
            return jsonify(Order = order)

    def searchOrders(selfself, args):
        uid = args.get("uid")
        resourceTypeNumber = args.get("resourceTypeNumber")
        tid = args.get("tid")
        purchaseTypeNumber = args.get("purchaseTypeNumber")
        dateOrdered = args.get("dateOrdered")
        orders_list = []
        dao=OrderDAO()
        Name =  args.get('name')
        if Name:
            orders_list =  dao.getAllOrdersByResourceName(Name)
            return jsonify(Orders=orders_list)
        else:
            return jsonify(Error="Invalid Arguments")
        """
        if (len(args) == 2) and uid and resourceTypeNumber:
            orders_list = dao.getAllOrdersByResourceNameAndUserID(resourceTypeNumber, uid)
        elif (len(args) == 2) and purchaseTypeNumber and resourceTypeNumber:
            orders_list = dao.getAllOrdersByPurchaseTypeAndResourceName(purchaseTypeNumber, resourceTypeNumber)
        elif (len(args) == 2) and purchaseTypeNumber and uid:
            orders_list = dao.getAllOrdersByPurchaseTypeAndUserID(purchaseTypeNumber, uid)
        elif (len(args) == 1) and resourceTypeNumber:
            orders_list = dao.getAllOrdersByResourceName(resourceTypeNumber)
        elif (len(args) == 1) and uid:
            orders_list = dao.getALLOrdersByUserID(uid)
        elif (len(args) == 1) and tid:
            orders_list = dao.getAllOrdersByTransactionID
        elif (len(args) == 1) and purchaseTypeNumber:
            orders_list = dao.getAllOrdersByPurchaseType
        elif (len(args) == 1) and dateOrdered:
            orders_list = dao.getAllOrdersByDate(dateOrdered)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in orders_list:
            order = self.build_order_dict(row)
            result_list.append(order)
        return jsonify(Order=result_list)"""

    # Uses resource name to find order, json used as return message
    def getOrdersByResourceName(self, resourceTypeNumber):
        dao = OrderDAO()
        orders_list = dao.getAllOrdersByResourceName(resourceTypeNumber)
        result_list = []
        for row in orders_list:
            order = self.build_order_dict(row)
            result_list.append(order)
        return jsonify(Order=result_list)

    def getOrdersByUserID(self, uid):
        dao = OrderDAO()
        orders_list = dao.getALLOrdersByUserID(uid)
        result_list = []
        for row in orders_list:
            order = self.build_order_dict(row)
            result_list.append(order)
        return jsonify(Order=result_list)

    def getOrdersByTransactionID(self, tid):
        dao = OrderDAO()
        orders_list = dao.getAllOrdersByTransactionID(tid)
        result_list = []
        for row in orders_list:
            order = self.build_order_dict(row)
            result_list.append(order)
        return jsonify(Order=result_list)

    def getOrdersByPurchaseType(self, purchaseTypeNumber):
        dao = OrderDAO()
        orders_list = dao.getAllOrdersByPurchaseType(purchaseTypeNumber)
        result_list = []
        for row in orders_list:
            order = self.build_order_dict(row)
            result_list.append(order)
        return jsonify(Order=result_list)

    def getOrdersByDate(self, dateOrdered):
        dao = OrderDAO()
        orders_list = dao.getAllOrdersByDate(dateOrdered)
        result_list = []
        for row in orders_list:
            order = self.build_order_dict(row)
            result_list.append(order)
        return jsonify(Order=result_list)

    def getOrdersByResourceNameAndUserid(self, resourceTypeNumber, uid):
        dao = OrderDAO()
        orders_list = dao.getAllOrdersByResourceNameAndUserID(resourceTypeNumber, uid)
        result_list = []
        for row in orders_list:
            order = self.build_order_dict(row)
            result_list.append(order)
        return jsonify(Order=result_list)

    def getOrdersByResourceNameAndPurchaseType(self, resourceTypeNumber, purchaseTypeNumber):
        dao = OrderDAO()
        orders_list = dao.getAllOrdersByPurchaseTypeAndResourceName(resourceTypeNumber, purchaseTypeNumber)
        result_list = []
        for row in orders_list:
            order = self.build_order_dict(row)
            result_list.append(order)
        return jsonify(Order=result_list)

    def getOrdersByResourceNameAndPurchaseType(self, uid, purchaseTypeNumber):
        dao = OrderDAO()
        orders_list = dao.getAllOrdersByPurchaseTypeAndUserID(uid, purchaseTypeNumber)
        result_list = []
        for row in orders_list:
            order = self.build_order_dict(row)
            result_list.append(order)
        return jsonify(Order=result_list)

    # the order is inserted with the required parameters using the DAO method,
    # if not, a json error message will appear
    def insertOrder(self, form):

        if len(form) != 4:
            return jsonify(Error="Malformed post request"), 400
        else:
            userId =form['userId']
            resourceId = form['resourceId']
            ammountOrdered = form['ammountOrdered']
            date = form['date']
            if userId and resourceId and ammountOrdered and date:
                dao = OrderDAO()
                oid=dao.insertOrder(userId,resourceId,ammountOrdered,date)
                if oid:

                    #result = self.build_order_attributes(oid,cid, rname, ammountReserved, ammountBought, date)
                    return jsonify(PostStatus="New Order Added"), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400


    # Updates an existing order with new information
    def updateOrder(self, oid, form):
        dao = OrderDAO()
        if not dao.getOrderById(oid):
            return jsonify(Error = "Order not found."), 404
        else:
            print(len(form))
            if len(form) != 5:
                return jsonify(Error="Malformed update request"), 400
            else:
                rname = form['rname']
                cid = form['cid']
                ammountReserved = form['ammountReserved']
                ammountBought = form['ammountBought']
                date = form['date']
                if rname and cid and ammountReserved and ammountBought and date:
                    r=dao.update(oid, cid, rname, ammountReserved, ammountBought, date)
                    if not r:
                        return jsonify(Error="Invalid costumer"), 404
                    else:
                        result = self.build_order_attributes(oid, cid, rname, ammountReserved, ammountBought, date)
                        return jsonify(PutStatus="Updated order"), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    # deletes an order from the database if it exists, json message appears denoting success or if the
    # order was not found
    def deleteOrder(self, oid):
        dao = OrderDAO()

        if dao.delete(oid):
            return jsonify(DeleteStatus = "Order deleted"), 200
        else:
            return jsonify(Error = "Order not found."), 404

