from flask import jsonify
from dao.supplier import SupplierDAO


class SupplierHandler:
    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['sname'] = row[1]
        result['sphone'] = row[2]
        result['semail'] = row[3]
        result['scity'] = row[4]

        return result

    def build_resource_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        result['rmaterial'] = row[2]
        result['rcolor'] = row[3]
        result['rprice'] = row[4]
        result['quantity'] = row[5]
        return result

    def getAllSuppliers(self):

        dao = SupplierDAO()
        suppliers_list = dao.getAllSuppliers()
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getSupplierById(self, sid):

        dao = SupplierDAO()

        row = dao.getSupplierById(sid)
        if not row:
            return jsonify(Error="Supplier Not Found"), 404
        else:
            resource = self.build_supplier_dict(row)
        return jsonify(Resource=resource)

    def getResourcesBySupplierId(self, sid):
        dao = SupplierDAO()
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
                dao = SupplierDAO()
                supplier_list = dao.getSuppliersByCity(city)
                result_list = []
                for row in supplier_list:
                    result = self.build_supplier_dict(row)
                    result_list.append(row)
                return jsonify(Suppliers=result_list)
            else:
                return jsonify(Error="Malformed search string."), 400

    def insertSupplier(self, form):
        if form and len(form) == 3:
            sname = form['sname']
            scity = form['scity']
            sphone = form['sphone']
            if sname and scity and sphone:
                dao = SupplierDAO()
                sid = dao.insert(sname, scity, sphone)
                result = {}
                result["sid"] = sid
                result["sname"] = sname
                result["scity"] = scity
                result["sphone"] = sphone
                return jsonify(Supplier=result), 201
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
                dao = SupplierDAO()
                result = dao.update(sid,sname, scity, sphone)

                return jsonify(Supplier=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed args post request")

    def deleteSupplier(self, sid):
        dao=SupplierDAO()

        result=dao.deleteSupplier(sid)
        if result:
            return jsonify(Supplier=result), 201
        else:
            return jsonify(Error="Supplier not found"), 404
