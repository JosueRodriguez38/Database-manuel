from flask import jsonify
from dao.Need import NeededDAO
from dao.resource import ResourcesDAO
from dao.Request import  RequestDAO
from dao.Selected import SelectedDAO

class NeedHandler:

    # Builds tuple with proper information and order
    def build_needed_dicc(self, row):
        results={}
        results['neededid']= row[0]
        results['userid'] = row[1]
        results['firstname'] = row[2]
        results['lastname'] = row[3]
        results['nameneeded'] = row[4]
        results['resourcetypename'] = row[5]
        results['ammountneeded'] = row[6]
        results['purchasetypename'] = row[7]
        results['dateneeded'] = row[8]
        results['pueblo'] = row[9]
        results['location'] = row[10]
        return results

    # inserts a needed resource with help of NeededDAO methods

    def insert_needed(self, form):
        resourcetypenumber  = form['resourcetypenumber']
        userid = form['userid']
        purchasetypenumber = form['purchasetypenumber']
        ammountneeded = form['ammountneeded']
        dateneeded = form['dateneeded']
        nameneeded = form['nameneeded']

        if resourcetypenumber and userid and purchasetypenumber and ammountneeded and dateneeded and nameneeded:
            dao = NeededDAO()
            neededid = dao.insert_needed(resourcetypenumber,userid,purchasetypenumber,ammountneeded,dateneeded,nameneeded)
            rdao = ResourcesDAO()
            resourceid = rdao.get_min_resourceid_by_needed_atribute(resourcetypenumber, purchasetypenumber, ammountneeded,nameneeded)[0]
            if resourceid:
                reqdao = RequestDAO()
                requestid=reqdao.insertrequest(userid)[0]
                sdao = SelectedDAO()
                sdao.insertSelected(requestid,resourceid,ammountneeded,dateneeded)
                dao.update_status(neededid,False)
                dao.insert_atendido(neededid,requestid)
                return jsonify("New needed has been added neededid: "+str(neededid)+" Resource found  new request has been added: "+str(requestid))
            return jsonify("New Needed has been added neededid: "+str(neededid))
        else:
            return jsonify(Error="Invalid arguments")

    # gets all needed resources

    def get_all_needed(self):
        dao = NeededDAO()
        data = dao.get_all_needed()
        results=[]
        if data:
            for row in data:
                results.append(self.build_needed_dicc(row))
        return jsonify(Needed= results)

    def search_needed(self, args):
        dao = NeededDAO()
        pass

    # gets specific needed resource

    def get_needed_by_neededid(self, neededid):
        dao = NeededDAO()
        data = dao.get_needed_by_neededid(neededid)
        result = self.build_needed_dicc(data)
        return result

    def update_needed_by_neededid(self, tid):
        dao = NeededDAO()
        return jsonify("Incomplete implementation")

    def delete_needed_by_neededid(self, tid):
        dao = NeededDAO()
        return jsonify("Incomplete implementation")

    def get_statistic_by_senate_region(self):

        pass

    # gets needed resource via the specified date
    def get_statistic_by_date(self, args):
        dao = NeededDAO()
        date = args.get('date')
        print (date)
        if date:
            if date=='1':
                data = dao.get_needed_by_date_since1(date)
                results = {}
                results['Resources Needed'] = data[0]
                results['Resources Aviable'] = data[1]
                results['Resources Matched'] = data[2]
                return jsonify(Needed=results)
            elif date=='7':
                data = dao.get_needed_by_date_since7(date)
                results={}
                results['Resources Needed']=data[0]
                results['Resources Aviable'] = data[1]
                results['Resources Matched'] = data[2]
                return jsonify(Needed=results)
            else:
                return jsonify(Error="Invalid interval for date")
        else:
            return jsonify(Error="invalid arguments")


