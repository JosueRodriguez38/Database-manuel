

import json
import io
from flask import jsonify
from dao.user import UserDAO


class UserHandler:
    def build_user_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['uname'] = row[1]
        result['uphone'] = row[2]
        result['uemail'] = row[3]
        result['ucity'] = row[4]

        return result

    def insertSupplierJson(self, form):


        if form and len(form) == 3:
            uname = form['uname']
            ucity = form['ucity']
            uphone = form['uphone']
            if uname and ucity and uphone:
                dao = UserDAO()
                uid = dao.insertSupplier(uname, ucity, uphone)
                result = {}
                result["uid"] = uid
                result["uname"] = uname
                result["ucity"] = ucity
                result["uphone"] = uphone
                return jsonify(Supplier=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")

    def insertConsumerJson(self, form):

        if form and len(form) == 3:
            uname = form["uname"]
            ucity = form["ucity"]
            uphone =form["uphone"]
            #print(uname +" "+ucity+" "+" "+uphone)
            value = uname and ucity and uphone
            print(value)
            if value:
                dao = UserDAO()
                uid = dao.insertConsumer(uname, ucity, uphone)
                result = {}
                result["uid"] = uid
                result["uname"] = uname
                result["ucity"] = ucity
                result["uphone"] = uphone
                return jsonify(Consumer=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed args post request")

    def insertAdminJson(self, form):

        if form and len(form) == 3:
            uname = form['uname']
            ucity = form['ucity']
            uphone = form['uphone']
            if uname and ucity and uphone:
                dao = UserDAO()
                uid = dao.insertAdmin(uname, ucity, uphone)
                result = {}
                result["uid"] = uid
                result["uname"] = uname
                result["ucity"] = ucity
                result["uphone"] = uphone
                return jsonify(Admin=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")

    def insertAdmin(self,aid,form):

        if form and len(form) == 3:
            name = form['name']
            city = form['city']
            phone = form['phone']
            if name and city and phone:
                dao = UserDAO()
                aid = dao.insertAdminById(aid,name, city, phone)
                if aid:
                    result = {}
                    result["aid"] = aid
                    result["uname"] = name
                    result["ucity"] = city
                    result["uphone"] = phone
                    return jsonify(Admin=result), 201
                else:
                    return jsonify(Error="Admin not found"),404
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")

    def getAdmin(self, aid):
        dao = UserDAO()

        row = dao.getAdminById(aid)
        if not row:
            return jsonify(Error="Admin Not Found"), 404
        else:
            admin = self.build_user_dict(row)
            admin['aid']=aid
        return jsonify(Admin=admin)

    def deleteAdmin(self, aid):
        dao = UserDAO()

        result = dao.deleteAdmin(aid)
        if result:
            return jsonify(Admin=result), 201
        else:
            return jsonify(Error="Supplier not found"), 404
