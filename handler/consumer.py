from flask import jsonify
from dao.consumer import ConsumerDAO

class ConsumerHandler:

    def build_consumer_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['sname'] = row[1]
        result['sphone'] = row[5]
        result['scity'] = row[6]

        return result

        return result

    def getAllConsumer(self):
        dao = ConsumerDAO()
        consumer_list = dao.getAllConsumer()
        result_list = []
        for row in consumer_list:
            result = self.build_consumer_dict(row)
            result_list.append(result)
        return jsonify(Consumers=result_list)


    def searchConsumerById(self,cid):
        dao = ConsumerDAO()
        row = dao.getConsumerById(cid)
        if not row:
            return jsonify(Error="Consumer Not Found"), 404
        else:
            resource = self.build_consumer_dict(row)
        return jsonify(Consumer=resource)

    def updateConsumer(self,cid,form):
        print(form)
        if form and len(form) == 3:
            sname = form['sname']
            scity = form['scity']
            sphone = form['sphone']
            if sname and scity and sphone:
                dao = ConsumerDAO()
                result = dao.update(cid, sname, scity, sphone)
                if result:
                    return jsonify(Supplier=result), 201
                else:
                    return jsonify(Error="Consumer not found"), 404
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed args post request")

    def deleteConsumer(self,cid):
        dao = ConsumerDAO()

        result = dao.deleteConsumer(cid)
        if result:
            return jsonify(Consumer=result), 201
        else:
            return jsonify(Error="Consumer not found"), 404
