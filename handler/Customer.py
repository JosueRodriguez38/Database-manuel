from flask import jsonify
from dao.Customer import CustomerDAO

# The consumer handler takes the information extracted from the consumerDAO
# and jsonify the results for the localhost

class CustomerHandler:

    # Builds the consumer dictionary, adding to an array the values of consumer id, name, phone, and city
    def build_consumer_dict(self, row):
        result = {}
        result['cid'] = row[0]
        result['cname'] = row[1]
        result['cphone'] = row[5]
        result['ccity'] = row[6]

        return result

    # this method calls the DAO method in order to add all the consumers to a list, and jsonifies it
    def getAllConsumer(self):
        dao = CustomerDAO()
        consumer_list = dao.getAllConsumer()
        result_list = []
        for row in consumer_list:
            result = self.build_consumer_dict(row)
            result_list.append(result)
        return jsonify(Consumers=result_list)

    # Uses DAO method to compare the input id
    def searchConsumerById(self, cid):
        dao = CustomerDAO()
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
            cname = form['cname']
            ccity = form['ccity']
            cphone = form['cphone']
            if cname and ccity and cphone:
                dao = CustomerDAO()
                result = dao.update(cid, cname, ccity, cphone)
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
        dao = CustomerDAO()

        if dao.delete(cid):
            return jsonify(DeleteStatus="Consumer deleted"), 200
        else:
            return jsonify(Error="Consumer not found"), 404
