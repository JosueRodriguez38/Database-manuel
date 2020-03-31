from flask import jsonify
from dao.consumer import ConsumerDAO

# The consumer handler takes the information extracted from the consumerDAO
# and jsonify the results for the localhost

class ConsumerHandler:

    # Builds the consumer dictionary, adding to an array the values of consumer id, name, phone, and city
    def build_consumer_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['sname'] = row[1]
        result['sphone'] = row[5]
        result['scity'] = row[6]

        return result

        return result

    # this method calls the DAO method in order to add all the consumers to a list, and jsonifies it
    def getAllConsumer(self):
        dao = ConsumerDAO()
        consumer_list = dao.getAllConsumer()
        result_list = []
        for row in consumer_list:
            result = self.build_consumer_dict(row)
            result_list.append(result)
        return jsonify(Consumers=result_list)

    # Uses DAO method to compare the input id
    def searchConsumerById(self, cid):
        dao = ConsumerDAO()
        row = dao.getConsumerById(cid)
        if not row:
            return jsonify(Error="Consumer Not Found"), 404
        else:
            result = self.build_consumer_dict(row)
        return jsonify(Consumer=result)

    # This method finds the consumer and updates their information, with various json messages in case
    # of success or an error arising
    def updateConsumer(self, cid, form):
        print(form)
        if form and len(form) == 3:
            sname = form['sname']
            scity = form['scity']
            sphone = form['sphone']
            if sname and scity and sphone:
                dao = ConsumerDAO()
                result = dao.update(cid, sname, scity, sphone)
                if result:
                    return jsonify(PutStatus="Updated information"), 200
                else:
                    return jsonify(Error="Consumer not found"), 404
            else:
                return jsonify(Error="Malformed post request"), 400
        else:
            return jsonify(Error="Malformed args post request"), 400

    # Uses the DAO method to delete a consumer and returns a json indicating if successful or if the consumer
    # was not found
    def deleteConsumer(self, cid):
        dao = ConsumerDAO()

        if dao.delete(cid):
            return jsonify(DeleteStatus="Consumer deleted"), 200
        else:
            return jsonify(Error="Consumer not found"), 404
