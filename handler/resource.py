from flask import jsonify

from config import tuple_config
from config.tuple_config import resource

from dao.resouce import ResourcesDAO


class ResourceHandler:
    # def build_resource_dict(self, row):
    #     result = {}
    #     result['rid'] = row[0]
    #     result['sid'] = row[1]
    #     result['rname'] = row[2]
    #     result['cost'] = row[3]
    #     result['ramount'] = row[4]
    #     result['bamount'] = row[5]
    #     result['location'] = row[6]
    #
    #     return result

    def build_supplier_dict(self, row):
        result = {'sid': row[0], 'sname': row[1], 'scity': row[2], 'sphone': row[3]}
        return result

    # def build_resource_attributes(self, rid, sid, rname, cost, ramount, bamount, location):
    #     result = {}
    #     result['rid'] = rid
    #     result['sid'] = sid
    #     result['rname'] = rname
    #     result['cost'] = cost
    #     result['ramount'] = ramount
    #     result['bamount'] = bamount
    #     result['location'] = ramount
    #     return result

    def getAllResources(self):

        return jsonify(Resources=resource)

    def getResourceById(self, rid):
        dao = ResourcesDAO()
        row = dao.getResourceById(rid)
        if not row:
            return jsonify(Error="Resource Not Found"), 404
        else:
            resource = self.build_resource_dict(row)
            return jsonify(Resource=resource)

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

    def insertResource(self, form):
        print("form: ", form)
        if len(form) != 4:
            return jsonify(Error="Malformed post request"), 400
        else:
            sid = form['sid']
            ramount = form['ramount']
            cost = form['cost']
            rname = form['rname']
            if rname and ramount and cost and sid:
                dao = ResourcesDAO()
                rid = dao.insert(sid, rname, cost, ramount)
                result = self.build_resource_attributes(rid, sid, rname, cost, ramount)
                return jsonify(Resource=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertResourceJson(self, json):
        sid = json['sid']
        ramount = json['ramount']
        cost = json['cost']
        rname = json['rname']
        if rname and ramount and cost and sid:
            dao = ResourcesDAO()
            rid = dao.insert(sid, rname, cost, ramount)
            result = self.build_resource_attributes(rid, sid, rname, cost, ramount)
            return jsonify(Resource=result), 201
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
                ramount = form['ramount']
                cost = form['cost']
                rname = form['rname']
                if rname and ramount and cost and sid:
                    dao.update(rid, sid, rname, cost, ramount)
                    result = self.build_resource_attributes(rid, sid, rname, cost, ramount)
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
