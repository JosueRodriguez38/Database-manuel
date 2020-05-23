

import json
import io
from flask import jsonify
from dao.user import UserDAO
from dao.Location import LocationDAO
from dao.UserCredentials import UserCredentialDAO


class UserHandler:
    def build_user_dict(self, row):
        result = {}
        result['userid'] = row[0]
        result['accounttypename'] = row[1]
        result['firstname'] = row[2]
        result['lastname'] = row[3]
        result['phone'] = row[4]
        result['email'] = row[5]
        result['adressline1'] = row[6]
        result['adressline2'] = row[7]
        result['pueblo'] = row[8]
        result['pais'] = row[9]
        result['codigopostal'] = row[10]
        result['googlemapurl'] = row[11]
        result['status'] = row[12]

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

                return jsonify(PostStatus="New User added with userid = "+userid ), 200
            else:
                return jsonify(Error="Malformed post request"), 400



    def getUserById(self, userid):
        dao = UserDAO()

        if userid:
            data = dao.getUserById(userid)

            result = []
            for row in data:
                result.append(self.build_user_dict(row))
            return jsonify(User=result)
        else:
            return jsonify(Error="Not arguments")

    def serachUser(self,arg):
        type = arg.get('type')
        if type:
            dao = UserDAO()
            data = dao.getAllUserByAccountType(type)
            result = []
            for row in data:
                result.append(self.build_user_dict(row))
            return jsonify(AllUsers=result)

        else:
            return jsonify(Error="Illegal arguments")


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