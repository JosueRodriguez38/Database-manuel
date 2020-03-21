from flask import jsonify

from dao.resouce import ResourcesDAO


class ResourceHandler:
    def build_resource_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        result['price'] = row[2]
        result['reserved'] = row[3]
        result['buyable'] = row[4]
        result['location'] = row[5]



        result['resvAmount'] = row[4]
        return result

    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['sname'] = row[1]
        result['scity'] = row[2]
        result['sphone'] = row[3]
        return result

    def build_resource_attributes(self, rid, sid, rname, price, resvAmount):
        result = {}
        result['rid'] = rid
        result['sid'] = sid
        result['price'] = rname
        result['rname'] = price
        result['resvAmount'] = resvAmount
        return result

    def getAllResources(self):
        dao = ResourcesDAO()
        resources_list = dao.getAllResources()
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getResourceById(self, rid):
        dao = ResourcesDAO()
        row = dao.getResourceById(rid)
        if not row:
            return jsonify(Error="Resource Not Found"), 404
        else:
            resource = self.build_resource_dict(row)
            return jsonify(Resource=resource)

    def searchResources(self, args):                                                     #Fixed
        name = args.get("name")
        price = args.get("price")
        dao = ResourcesDAO()
        resources_list = []
        if (len(args) == 2) and name and price:
            resources_list = dao.getResourcesByNameAndPrice(name, price)
        elif (len(args) == 1) and name:
            resources_list = dao.getResourcesByName(name)
        elif (len(args) == 1) and price:
            resources_list = dao.getResourcesByPrice(price)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getSuppliersByResourceId(self, rid):
        dao = ResourcesDAO()
        if not dao.getResourceById(rid):
            return jsonify(Error="Resource Not Found"), 404
        suppliers_list = dao.getSuppliersByResourceId(rid)
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def insertResourcesJson(self, form):
        print("form: ", form)
        if len(form) != 4:
            return jsonify(Error="Malformed post request"), 400
        else:
            sid = form['sid']
            resvAmount = form['resvAmount']
            price = form['price']
            rname = form['rname']
            if rname and resvAmount and price and sid:
                dao = ResourcesDAO()
                rid = dao.insert(sid, rname, price, resvAmount)
                result = self.build_resource_attributes(rid, sid, rname, price, resvAmount)
                return jsonify(Resource=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertResourceBySupplierIdJson(self,rid, json):
        sid = json['sid']
        resvAmount = json['resvAmount']
        price = json['price']
        rname = json['rname']
        if rname and resvAmount and price and sid:
            dao = ResourcesDAO()
            r = dao.insert(rid,sid, rname, price, resvAmount)
            if r:
                result = self.build_resource_attributes(rid, sid, rname, price, resvAmount)
                return jsonify(Resource=result), 201
            else:
                return jsonify(Error="Resource not found or invalid supplier id."), 404
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteResource(self, rid):
        dao = ResourcesDAO()
        if not dao.getResourceById(rid):
            return jsonify(Error="Resource not found."), 404
        else:
            dao.delete(rid)
            return jsonify(DeleteStatus="OK"), 200

    def updateResource(self, rid, form):
        dao = ResourcesDAO()
        if not dao.getResourceById(rid):
            return jsonify(Error="Resource not found."), 404
        else:
            if len(form) != 4:
                return jsonify(Error="Malformed update request"), 400
            else:
                sid = form['sid']
                resvAmount = form['resvAmount']
                price = form['price']
                rname = form['rname']
                if rname and resvAmount and price and sid:
                    dao.update(rid, sid, rname, price, resvAmount)
                    result = self.build_resource_attributes(rid, sid, rname, price, resvAmount)
                    return jsonify(Resource=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def build_resource_counts(self, resource_counts):
        result = []
        # print(resource_counts)
        for P in resource_counts:
            D = {}
            D['id'] = P[0]
            D['name'] = P[1]
            D['count'] = P[2]
            result.append(D)
        return result

    def getCountByResourceId(self):
        dao = ResourcesDAO()
        result = dao.getCountByResourceId()
        # print(self.build_resource_counts(result))
        return jsonify(ResourceCounts=self.build_resource_counts(result)), 200
