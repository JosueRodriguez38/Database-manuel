from flask import jsonify

from dao.resource import ResourcesDAO


class ResourceHandler:
    def build_resource_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['sid'] = row[1]
        result['rname'] = row[2]
        result['cost'] = row[3]
        result['resAmount'] = row[4]
        result['buyable'] = row[5]
        result['location'] = row[6]



        return result

    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['sname'] = row[1]
        result['sphone'] = row[2]
        result['semail'] = row[3]
        result['scity'] = row[4]
        return result

    def build_resource_attributes(self, rid, sid, rname, cost, resv_amount):
        result = {}
        result['rid'] = rid
        result['sid'] = sid
        result['cost'] = rname
        result['rname'] = cost
        result['resv_amount'] = resv_amount
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
        cost = args.get("cost")
        dao = ResourcesDAO()
        resources_list = []
        if (len(args) == 2) and name and cost:
            resources_list = dao.getResourcesByNameAndCost(name, cost)
        elif (len(args) == 1) and name:
            resources_list = dao.getResourcesByName(name)
        elif (len(args) == 1) and cost:
            resources_list = dao.getResourcesByCost(cost)
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
            resv_amount = form['resv_amount']
            cost = form['cost']
            rname = form['rname']
            if rname and resv_amount and cost and sid:
                dao = ResourcesDAO()
                rid = dao.insert(sid, rname, cost, resv_amount)
                result = self.build_resource_attributes(rid, sid, rname, cost, resv_amount)
                return jsonify(Resource=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertResourceBySupplierIdJson(self,rid, json):
        sid = json['sid']
        resv_amount = json['resv_amount']
        cost = json['cost']
        rname = json['rname']
        if rname and resv_amount and cost and sid:
            dao = ResourcesDAO()
            r = dao.insert(sid, rname, cost, resv_amount)
            if r:
                return jsonify(PostStatus="Resource added"), 200
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
            return jsonify(DeleteStatus="Resource deleted"), 200

    def updateResource(self, rid, form):
        dao = ResourcesDAO()
        if not dao.getResourceById(rid):
            return jsonify(Error="Resource not found."), 404
        else:
            if len(form) != 4:
                return jsonify(Error="Malformed update request"), 400
            else:
                sid = form['sid']
                resv_amount = form['resv_amount']
                cost = form['cost']
                rname = form['rname']
                if rname and resv_amount and cost and sid:
                    dao.update(rid, sid, rname, cost, resv_amount)
                    result = self.build_resource_attributes(rid, sid, rname, cost, resv_amount)
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
