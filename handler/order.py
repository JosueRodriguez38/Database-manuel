from flask import jsonify
from dao.order import OrderDAO

class OrderHandler:
    def build_order_dict(self, row):
        result = {}
        result['oid'] = row[0]
        result['cid'] = row[1]
        result['rname'] = row[2]
        result['ammountReserved'] = row[3]
        result['ammountBought'] = row[4]
        result['date'] = row[5]
        return result

    def build_order_attributes(self, oid, cid, rname, ammountBought, ammountReserved, date):
        result = {}
        result['oid'] = oid
        result['cid'] = cid
        result['rname'] = rname
        result['ammountReserved'] = ammountReserved
        result['ammountBought'] = ammountBought
        result['date'] = date
        return result

    def getAllOrders(self):
        dao = OrderDAO()
        orders_list = dao.getAllOrders()
        result_list = []
        for row in orders_list:
            result = self.build_order_dict(row)
            result_list.append(result)
        return jsonify(Orders=result_list)

    def getOrderById(self, oid):
        dao = OrderDAO()
        row = dao.getOrderById(oid)
        if not row:
            return jsonify(Error = "Part Not Found"), 404
        else:
            order = self.build_order_dict(row)
            return jsonify(Order = order)

    def getOrdersByResourceName(self, rname):
        dao = OrderDAO()
        row = dao.getOrderByResourceName(rname)
        if not row:
            return jsonify(Error="Part Not Found"), 404
        else:
            order = self.build_order_dict(row)
            return jsonify(Order=order)

    def insertOrder(self, form):
        print("form: ", form)
        if len(form) != 6:
            return jsonify(Error="Malformed post request"), 400
        else:
            rname = form['rname']
            firstName = form['firstName']
            lastName = form['lastName']
            ammountReserved = form['ammountReserved']
            ammountBought = form['ammountBought']
            date = form['date']
            if rname and firstName and lastName and ammountReserved and ammountBought and date:
             #   dao = OrderDAO()        *comentado porque el response va a estar hardcoded
              #  cdao = ConsumerDAO()
               # cid = cdao.getConsumerIdByName(firstName, lastName)
                #oid = dao.insert(rname, firstName, ammountReserved, ammountBought, date)
                cid = 1
                oid = 1
                result = self.build_order_attributes(oid, cid, rname, ammountReserved, ammountBought, date)
                return jsonify(Order=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertPartJson(self, json):
        rname = json['rname']
        firstName = json['firstName']
        lastName = json['lastName']
        ammountReserved = json['ammountReserved']
        ammountBought = json['ammountBought']
        date = json['date']
        if rname and firstName and lastName and ammountReserved and ammountBought and date:
          #  dao = OrderDAO()           *comentado porque el response va a estar hardcoded
          # cid = dao.getConsumerIdByName(firstName, lastName)
          # oid = dao.insert(rname, firstName, ammountReserved, ammountBought, date)
            cid = 1
            oid = 1
            result = self.build_order_attributes(oid, cid, rname, ammountReserved, ammountBought, date)
            return jsonify(Order=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updateOrder(self, oid, form):
        dao = OrderDAO()
        if not dao.getOrderById(oid):
            return jsonify(Error = "Order not found."), 404
        else:
            if len(form) != 4:
                return jsonify(Error="Malformed update request"), 400
            else:
                rname = form['rname']
                ammountReserved = form['ammountReserved']
                ammountBought = form['ammountBought']
                date = form['date']
                if rname and ammountReserved and ammountBought and date:
                    dao.update(oid, rname, ammountReserved, ammountBought, date)
                    #cid = dao.getConsumerIdByName(firstName, lastName)
                    cid = 1
                    result = self.build_order_attributes(oid, cid, rname, ammountReserved, ammountBought, date)
                    return jsonify(Order=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteOrder(self, oid):
        #dao = OrderDAO()
        #if not dao.getOrderById(oid):
        #    return jsonify(Error="Order not found."), 404
        #else:
        #    dao.delete(oid)
            return jsonify(DeleteStatus = "Order deleted"), 200

