from flask import jsonify

from dao.user import UserDAO

from dao.esenciales import esencialesDAO

# Uses resource DAO to build results for displaying in localhost
#this class involves supplier,

class EsencialesHandler:

    # all builds methods prepare tuple with proper order and info type
    def build_user_dict(self, row):
        result = {}
        result['userid'] = row[0]
        result['accounttype'] = row[1]
        result['firstname'] = row[2]
        result['lastname'] = row[3]
        result['phone'] = row[4]
        result['email'] = row[5]
        result['status'] = row[6]
        return result

    def build_user_attributes(self,userid, accounttype, firstname,lastname,phone,email,status):
        result = {}
        result['userid'] = userid
        result['accounttype'] = accounttype
        result['firstname'] = firstname
        result['lastname'] = lastname
        result['phone'] = phone
        result['email'] = email
        result['status'] = status
        return result

    def build_order_dict(self, row):
        result = {}
        result['orderid'] = row[0]
        result['userid'] = row[1]
        result['ammountordered'] = row[2]
        result['date'] = row[3]
        result['resourceid'] = row[4]
        return result

    def build_order_attributes(self,orderid,userid,ammountordered,date,resourceid):
        result = {}
        result['orderid'] = orderid
        result['userid'] = userid
        result['ammountordered'] = ammountordered
        result['date'] = date
        result['resourceid'] = resourceid
        return result

    # espesificacion 4
    def insertOrder(self, form):
        print("form: ", form)
        if len(form) != 4:
            return jsonify(Error="Malformed post request"), 400
        else:
            userid = form['userid']
            ammountordered = form['ammountordered']
            date = form['date']
            resourceid = form['resourceid']
            if userid and ammountordered and date and resourceid:
                dao = esencialesDAO()
                orderid = dao.insert(userid,ammountordered,date,resourceid)
                result = self.build_user_attributes(orderid,userid,ammountordered,date,resourceid)
                return jsonify(Part=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    #borrar
    def insertUserConsumer(self,form):
        print("form: ", form)
        if len(form) != 6:
            return jsonify(Error="Malformed post request"), 400
        else:
            accounttype = form['accounttype']
            firstname = form['firstname']
            lastname = form['lastname']
            phone = form['phone']
            email = form['email']
            status = form['status']
            if email and status and phone and lastname and firstname and accounttype:
                dao = esencialesDAO()
                userid = dao.insert(accounttype, firstname,lastname,phone,email,status)
                result = self.build_user_attributes(userid,accounttype, firstname,lastname,phone,email,status)
                return jsonify(Part=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    #especificacion 6
    def getOrdersbyUser(self,userid):
        udao = UserDAO()
        dao = esencialesDAO
        if not udao.getUserById(userid):
            return jsonify(Error="User has no orders"), 404
        orders_list = dao.getOrdersbyUser()
        result_list = []
        for row in orders_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(OrdersofUser=result_list)

    #especificacion 4
    def getOrderbyId(self, orderid):
        dao = esencialesDAO()
        row = dao.getOrderbyId()
        if not row:
            return jsonify(Error="Order Not Found"), 404
        else:
            order = self.build_order_dict(row)
            return jsonify(Order=order)

    def build_allresources_dict(self, row):
        result = {}
        result['resourceid'] = row[0]
        result['resourceTypeName'] = row[1]
        result['ammount'] = row[2]
        result['cost'] = row[3]
        result['purchaseTypeName'] = row[4]
        result['name'] = row[5]
        return result

    def build_allresources_attributes(self, resourceid, resourceTypeName , ammount, cost, purchaseTypeName, name):
        result = {}
        result['resourceid'] = resourceid
        result['resourceTypeName'] = resourceTypeName
        result['ammount'] = ammount
        result['cost'] = cost
        result['purchaseTypeName'] = purchaseTypeName
        result['name'] = name
        return result

    def getAllResources(self):
        dao = esencialesDAO()
        allresources_list = dao.getAllResources()
        result_list = []
        for row in allresources_list:
            result = self.build_allresources_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

