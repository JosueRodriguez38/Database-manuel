from flask import jsonify
#from dao.resources import ResourcesDAO


class ResourceHandler:
    def build_resource_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        result['pmaterial'] = row[2]
        result['pcolor'] = row[3]
        result['pprice'] = row[4]
        return result

    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['sname'] = row[1]
        result['scity'] = row[2]
        result['sphone'] = row[3]
        return result

    def build_resource_attributes(self, rid, rname, pcolor, pmaterial, pprice):
        result = {}
        result['rid'] = rid
        result['rname'] = rname
        result['pmaterial'] = pcolor
        result['pcolor'] = pmaterial
        result['pprice'] = pprice
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
            return jsonify(Error = "Resource Not Found"), 404
        else:
            resource = self.build_resource_dict(row)
            return jsonify(Resource = resource)

    def searchResources(self, args):
        color = args.get("color")
        material = args.get("material")
        dao = ResourcesDAO()
        resources_list = []
        if (len(args) == 2) and color and material:
            resources_list = dao.getResourcesByColorAndMaterial(color, material)
        elif (len(args) == 1) and color:
            resources_list = dao.getResourcesByColor(color)
        elif (len(args) == 1) and material:
            resources_list = dao.getResourcesByMaterial(material)
        else:
            return jsonify(Error = "Malformed query string"), 400
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

    def insertResource(self, form):
        print("form: ", form)
        if len(form) != 4:
            return jsonify(Error = "Malformed post request"), 400
        else:
            rname = form['rname']
            pprice = form['pprice']
            pmaterial = form['pmaterial']
            pcolor = form['pcolor']
            if pcolor and pprice and pmaterial and rname:
                dao = ResourcesDAO()
                rid = dao.insert(rname, pcolor, pmaterial, pprice)
                result = self.build_resource_attributes(rid, rname, pcolor, pmaterial, pprice)
                return jsonify(Resource=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertResourceJson(self, json):
        rname = json['rname']
        pprice = json['pprice']
        pmaterial = json['pmaterial']
        pcolor = json['pcolor']
        if pcolor and pprice and pmaterial and rname:
            dao = ResourcesDAO()
            rid = dao.insert(rname, pcolor, pmaterial, pprice)
            result = self.build_resource_attributes(rid, rname, pcolor, pmaterial, pprice)
            return jsonify(Resource=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteResource(self, rid):
        dao = ResourcesDAO()
        if not dao.getResourceById(rid):
            return jsonify(Error = "Resource not found."), 404
        else:
            dao.delete(rid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateResource(self, rid, form):
        dao = ResourcesDAO()
        if not dao.getResourceById(rid):
            return jsonify(Error = "Resource not found."), 404
        else:
            if len(form) != 4:
                return jsonify(Error="Malformed update request"), 400
            else:
                rname = form['rname']
                pprice = form['pprice']
                pmaterial = form['pmaterial']
                pcolor = form['pcolor']
                if pcolor and pprice and pmaterial and rname:
                    dao.update(rid, rname, pcolor, pmaterial, pprice)
                    result = self.build_resource_attributes(rid, rname, pcolor, pmaterial, pprice)
                    return jsonify(Resource=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def build_resource_counts(self, resource_counts):
        result = []
        #print(resource_counts)
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
        #print(self.build_resource_counts(result))
        return jsonify(ResourceCounts = self.build_resource_counts(result)), 200



