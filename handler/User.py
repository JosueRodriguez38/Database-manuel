

import json
import io
from flask import jsonify
from dao.user import UserDAO
from dao.Location import LocationDAO
from dao.UserCredentials import UserCredentialDAO


class UserHandler:
    def build_user_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['sname'] = row[1]
        result['sphone'] = row[5]
        result['scity'] = row[6]

        return result


    def insertUserJson(self, form):
        if form and len(form) == 13:
            #for user table
            firstname = form['firstName']
            lastName = form['lastName']
            accountType = form['accountType']
            phone = form['phone']
            email = form['email']

            #for location
            addressL1 = form['addressL1']
            addressL2 = form['addressL2']
            pueblo = form['pueblo']
            pais = form['pais']
            zipCode = form['zipCode']
            googleMap = form['googleMap']

            #for user credentials
            userName = form['userName']
            userPassword = form['userPassword']

            if accountType and firstname and lastName and phone and email and addressL1 and addressL2 and pueblo and pais and zipCode and googleMap and userName and userPassword:
                daou = UserDAO()
                daol = LocationDAO()
                daoC = UserCredentialDAO()
                userid = daou.insertUser(accountType,firstname,lastName,phone,email)
                daol.addlocation(addressL1,addressL2,pueblo,pais,zipCode,googleMap,userid)
                daoC.insertUserCredential(userName,userPassword,userid)

                return jsonify(PostStatus="New User added"), 200
            else:
                return jsonify(Error="Malformed post request"), 400



    def getUserById(self, userid):
        dao = UserDAO()

        row = dao.RemoveUserById(userid)
        if not row:
            return jsonify(Error="Admin Not Found"), 404
        else:
            admin = self.build_user_dict(row)
            admin['userid']=userid
        return jsonify(Admin=admin)

    def serachUser(self):
        return

    def getAllUsers(self):
        return

    def deleteUser(self, aid):
        dao = UserDAO()

        if dao.deleteUser(aid):
            return jsonify(DeleteStatus="Admin deleted"), 200
        else:
            return jsonify(Error="Supplier not found"), 404

    def getAllConsumer(self):
        return

    def updateUser(self, userid, json):
        pass