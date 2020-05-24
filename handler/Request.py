from flask import jsonify

from dao.Request import RequestDAO
from dao.Selected import SelectedDAO
class RequestHandler:
    def build_request_dict(self, row):
        result={}
        result['requestid'] = row[0]
        result['userid'] = row[1]
        result['firstname'] = row[2]
        result['lastname'] = row[3]
        result['status'] =row[4]
        return result

    def build_resource_dict(self, row):
        result = {}
        result['requestid'] = row[0]
        result['resourceid'] = row[1]
        result['name'] = row[2]
        result['resourcetypename'] = row[3]
        result['Amount'] = row[4]
        result['cost'] = row[5]
        result['purchasetypename']=row[6]
        result['location'] = row[7]

        return result

    def insertRequest(self, form):
        userid=form['userId']
        resourceid=form['resourceId']
        ammount=form['ammountOrdered']
        date=form['date']
        if userid and resourceid and ammount and date:
            dao =RequestDAO()
            requestid = dao.insertrequest(userid)[0]
            dao = SelectedDAO()
            selectedid = dao.insertSelected(requestid,resourceid,ammount,date)[0]

            return jsonify(ResquestID="New request has been added with resourceid = "+resourceid)
        else:
            return jsonify(Error="Invalid Json Arguments")

    def getAllRequest(self):
        dao = RequestDAO()
        data = dao.getallrequest()
        result = []
        for row in data:
            result.append(self.build_request_dict(row))
        return jsonify(requests=result)

    def getRequestByRequestID(self,requestid):
        dao = RequestDAO()
        data = dao.get_request_by_requestid(requestid)
        results= self.build_request_dict(data)

        return jsonify(Request=results)



    def searchRequest(self, args):
        userid = args.get("userid")
        name = args.get("name")
        requestid = args.get("requestid")
        if userid and not name and not requestid:
            dao = RequestDAO()
            data = dao.getUserRequest(userid)
            result=[]
            for row in data:
                result.append(self.build_request_dict(row))
            return jsonify(Requests=result)

        elif name and not userid and not requestid:
            dao = RequestDAO()
            data = dao.getAllResourcesbyResourceName(name)
            results=[]
            for row in data:
                results.append(self.build_resource_dict(row))
            return jsonify(Requests=results)

        elif requestid and not name and not userid:
            return self.getRequestByRequestID(requestid)
        return jsonify(Error="invalid arguments")

    def getAllResourcesByRequestId(self, requestid):

        dao = RequestDAO()
        data = dao.getAllResourcesbyRequestID(requestid)
        results=[]
        for row in data:
            results.append(self.build_resource_dict(row))

        return jsonify(Requests=results)

