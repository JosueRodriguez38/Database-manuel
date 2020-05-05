from flask import jsonify
from dao.user import UserDAO


class SupplierHandler:
    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['sname'] = row[1]
        result['sphone'] = row[5]
        result['scity'] = row[6]

        return result

    def build_resource_attributes(self, sid, usrname, phone, city):
        result = {}
        result['sid'] = sid
        result['user name'] = usrname
        result['phone'] = phone
        result['city'] = city
        return result

    def getAllSuppliers(self):

        dao = UserDAO()
        suppliers_list = dao.getAllSuppliers()
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getSupplierById(self, sid):

        dao = UserDAO()

        row = dao.getSupplierById(sid)
        if not row:
            return jsonify(Error="Supplier Not Found"), 404
        else:
            supplier = self.build_supplier_dict(row)
        return jsonify(Supplier=supplier)

    def getResourcesBySupplierId(self, sid):
        dao = UserDAO()
        if not dao.getSupplierById(sid):
            return jsonify(Error="Supplier Not Found"), 404
        resources_list = dao.getResourcesBySupplierId(sid)
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(ResourcesResources=result_list)

    def searchSuppliers(self, args):
        if len(args) > 1:
            return jsonify(Error = "Malformed search string."), 400
        else:
            city = args.get("city")
            if city:
                dao = UserDAO()
                supplier_list = dao.getSuppliersByCity(city)
                result_list = []
                for row in supplier_list:
                    result = self.build_supplier_dict(row)
                    result_list.append(result)
                return jsonify(Suppliers=result_list)
            else:
                return jsonify(Error="Malformed search string."), 400

    def insertSupplier(self, form):
        if form and len(form) == 3:
            sname = form['sname']
            scity = form['scity']
            sphone = form['sphone']
            if sname and scity and sphone:
                dao = UserDAO()
                sid = dao.insert(sname, scity, sphone)
                result = {}
                result["sid"] = sid
                result["sname"] = sname
                result["scity"] = scity
                result["sphone"] = sphone
                return jsonify(InsertStatus=result), 200
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")

    def updateSupplier(self,sid,form):
        print(form)
        if form and len(form)==3:
            sname = form['sname']
            scity = form['scity']
            sphone = form['sphone']
            if sname and scity and sphone:
                dao = UserDAO()
                if dao.update(sid,sname, scity, sphone):

                    return jsonify(PutStatus="Updated information"), 200
                else:
                    return jsonify(Error="Invalid Sid")
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed args post request")

    def deleteSupplier(self, sid):
        dao=UserDAO()

        if dao.delete(sid):
            return jsonify(DeleteStatus="Supplier deleted"), 200
        else:
            return jsonify(Error="Supplier not found"), 404
