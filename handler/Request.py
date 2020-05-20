from flask import jsonify

from dao.Request import RequestDAO
from dao.Selected import SelectedDAO
class RequestHandler:

    def insertRequest(self, form):
        userid=form['userId']
        resourceid=form['resourceId']
        ammount=form['ammountOrdered']
        date=form['date']
        if userid and resourceid and ammount and date:
            dao =RequestDAO()
            requestid = dao.insertRequest(userid)
            dao = SelectedDAO()
            selectedid = dao.insertSelected(requestid,resourceid,ammount,date)

            return jsonify(ResquestID=[requestid,selectedid])

    def getAllRequest(self):
        dao = RequestDAO()
        results = dao.getallrequest()
        return jsonify(requests=results)

    def getRequestByRequestID(self,requestid):
        dao = RequestDAO()
        results = dao.get_request_by_requestid(requestid)
        return jsonify(Request=results)



    def searchRequest(self, args):
        userid = args.get("userid")
        name = args.get("name")
        if userid and not name:
            dao = RequestDAO()
            results = dao.getUserRequest()
            return jsonify(Requests=results)
        elif name and not userid:
            dao = RequestDAO()
            results = dao.getAllResourcesbyResourceName(name)
            return jsonify(Requests=results)
        return

    def getAllResourcesByRequestId(self, requestid):

        dao = RequestDAO()
        results = dao.getAllResourcesbyRequestID(requestid)
        return jsonify(Requests=results)

