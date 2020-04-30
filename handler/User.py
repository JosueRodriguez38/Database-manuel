

import json
import io
from flask import jsonify
from dao.user import UserDAO


class UserHandler:
    def build_user_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['sname'] = row[1]
        result['sphone'] = row[5]
        result['scity'] = row[6]

        return result
    def insertSupplierJson(self, form):


        if form and len(form) == 3:
            sname = form['sname']
            scity = form['scity']
            sphone = form['sphone']
            if sname and scity and sphone:
                dao = UserDAO()
                sid = dao.insertSupplier(sname, scity, sphone)
                result = {}
                result["sid"] = sid
                result["sname"] = sname
                result["scity"] = scity
                result["sphone"] = sphone
                return jsonify(PostStatus="New Supplier added"), 200
            else:
                return jsonify(Error="Malformed post request"), 400
        else:
            return jsonify(Error="Malformed post request"), 400

    def insertConsumerJson(self, form):

        if form and len(form) == 3:
            sname = form["sname"]
            scity = form["scity"]
            sphone =form["sphone"]
            #print(sname +" "+scity+" "+" "+sphone)
            value = sname and scity and sphone
            print(value)
            if value:
                dao = UserDAO()
                sid = dao.insertConsumer(sname, scity, sphone)
                result = {}
                result["sid"] = sid
                result["sname"] = sname
                result["scity"] = scity
                result["sphone"] = sphone
                return jsonify(PostStatus="New Consumer added"), 200
            else:
                return jsonify(Error="Malformed post request"), 400
        else:
            return jsonify(Error="Malformed args post request"), 400

    def insertAdminJson(self, form):

        if form and len(form) == 3:
            sname = form['sname']
            scity = form['scity']
            sphone = form['sphone']
            if sname and scity and sphone:
                dao = UserDAO()
                sid = dao.insertAdmin(sname, scity, sphone)
                result = {}
                result["sid"] = sid
                result["sname"] = sname
                result["scity"] = scity
                result["sphone"] = sphone
                return jsonify(PostStatus="New Admin added"), 200
            else:
                return jsonify(Error="Malformed post request"), 400
        else:
            return jsonify(Error="Malformed post request"), 400

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
                    result["sname"] = name
                    result["scity"] = city
                    result["sphone"] = phone
                    return jsonify(PuStatus="Updated Admin"), 200
                else:
                    return jsonify(Error="Admin not found"), 404
            else:
                return jsonify(Error="Malformed post request"), 400
        else:
            return jsonify(Error="Malformed post request"), 400

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

        if dao.deleteAdmin(aid):
            return jsonify(DeleteStatus="Admin deleted"), 200
        else:
            return jsonify(Error="Supplier not found"), 404
