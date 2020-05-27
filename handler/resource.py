from flask import jsonify

from dao.resource import ResourcesDAO
from dao.Supplies import SuppliesDAO
from dao.Water import WaterDAO
from dao.Medications import MedicationDAO
from dao.BabyFood import BabyFoodDAO
from dao.CannedFood import CannedFoodDAO
from dao.DryFood import DryFoodDAO
from dao.Ice import IceDAO
from dao.Fuel import FuelDAO
from dao.MedicalDevices import MedicalDeviceDAO
from dao.HeavyEquipment import HeavyEquipmentDAO
from dao.Tools import ToolsDAO
from dao.Clothing import ClothingDAO
from dao.PowerGenerators import PowerGeneratorDAO
from dao.Batteries import BatteriesDAO
from dao.Request import RequestDAO
from dao.Selected import SelectedDAO
from dao.Need import NeededDAO


# Uses resource DAO to build results for displaying in localhost
#this class involves supplier,

class ResourceHandler:

    # builds resource tuple with the space required to insert the information required
    def build_resource_dict(self, row):
        result = {}
        result['resourceid'] = row[0]
        result['name'] = row[1]
        result['resourcetypename'] = row[2]
        result['Amount'] = row[3]
        result['cost'] = row[4]
        result['purchasetypename']=row[5]
        result['location'] = row[6]

        return result


    # builds tuple for resource with specified field values
    def build_resource_attributes(self, rid, sid, rname, cost, resv_amount):
        result = {}
        result['resourceid'] = rid
        result['userid'] = sid
        result['cost'] = rname
        result['name'] = cost
        result['ammount'] = resv_amount
        return result


    # uses DAO method to access all resource tuples and adds them to a list, where jsonify is used

    def build_waterbyresourceid_dict(self,row):
        result = {}
        result['resourceid'] = row[0]
        result['name'] = row[1]
        result['resourcetypename'] = row[2]
        result['ammount'] = row[3]
        result['cost'] = row[4]
        result['purchasetypename'] = row[5]
        result['watertypename'] = row[6]
        result['ounces'] = row[7]
        result['location'] = row[8]
        return result

    def build_toolbyresourceid_dict(self, row):
        result = {}
        result['resourceid'] = row[0]
        result['name'] = row[1]
        result['resourcetypename'] = row[2]
        result['ammount'] = row[3]
        result['cost'] = row[4]
        result['purchasetypename'] = row[5]
        result['size'] = row[6]
        result['location'] = row[7]
        return result

    def build_powergeneratorbyresourceid_dict(self, row):
        result = {}
        result['resourceid'] = row[0]
        result['name'] = row[1]
        result['resourcetypename'] = row[2]
        result['ammount'] = row[3]
        result['cost'] = row[4]
        result['purchasetypename'] = row[5]
        result['generatorfuel'] = row[6]
        result['capacity'] = row[7]
        result['size'] = row[8]
        result['location'] = row[9]
        return result

    def build_medicationbyresourceid_dict(self, row):
        result = {}
        result['resourceid'] = row[0]
        result['name'] = row[1]
        result['resourcetypename'] = row[2]
        result['ammount'] = row[3]
        result['cost'] = row[4]
        result['purchasetypename'] = row[5]
        result['activeingridient'] = row[6]
        result['description'] = row[7]
        result['concentration'] = row[8]
        result['quantity'] = row[9]
        result['expirationdate'] = row[10]
        result['location'] = row[11]
        return result

    def build_medicaldevicebyresourceid_dict(self, row):
        result = {}
        result['resourceid'] = row[0]
        result['name'] = row[1]
        result['resourcetypename'] = row[2]
        result['ammount'] = row[3]
        result['cost'] = row[4]
        result['purchasetypename'] = row[5]
        result['specs'] = row[6]
        result['location'] = row[7]
        return result

    def build_icebyresourceid_dict(self, row):
        result = {}
        result['resourceid'] = row[0]
        result['name'] = row[1]
        result['resourcetypename'] = row[2]
        result['ammount'] = row[3]
        result['cost'] = row[4]
        result['purchasetypename'] = row[5]
        result['weight'] = row[6]
        result['location'] = row[7]
        return result

    def build_heavyequipmentbyresourceid_dict(self, row):
        result = {}
        result['resourceid'] = row[0]
        result['name'] = row[1]
        result['resourcetypename'] = row[2]
        result['ammount'] = row[3]
        result['cost'] = row[4]
        result['purchasetypename'] = row[5]
        result['fueltype'] = row[6]
        result['location'] = row[7]
        return result

    def build_fuelbyresourceid_dict(self, row):
        result = {}
        result['resourceid'] = row[0]
        result['name'] = row[1]
        result['resourcetypename'] = row[2]
        result['ammount'] = row[3]
        result['cost'] = row[4]
        result['purchasetypename'] = row[5]
        result['fueltypename'] = row[6]
        result['litro'] = row[7]
        result['location'] = row[8]
        return result

    def build_dryfoodbyresourceid_dict(self, row):
        result = {}
        result['resourceid'] = row[0]
        result['name'] = row[1]
        result['resourcetypename'] = row[2]
        result['ammount'] = row[3]
        result['cost'] = row[4]
        result['purchasetypename'] = row[5]
        result['ounces'] = row[6]
        result['expirationdate'] = row[7]
        result['location'] = row[8]
        return result

    def build_clothingbyresourceid_dict(self, row):
        result = {}
        result['resourceid'] = row[0]
        result['name'] = row[1]
        result['resourcetypename'] = row[2]
        result['ammount'] = row[3]
        result['cost'] = row[4]
        result['purchasetypename'] = row[5]
        result['agecategory'] = row[6]
        result['size'] = row[7]
        result['location'] = row[8]
        return result

    def build_cannedfoodbyresourceid_dict(self, row):
        result = {}
        result['resourceid'] = row[0]
        result['name'] = row[1]
        result['resourcetypename'] = row[2]
        result['ammount'] = row[3]
        result['cost'] = row[4]
        result['purchasetypename'] = row[5]
        result['primaryingredient'] = row[6]
        result['ounces'] = row[7]
        result['expirationdate'] = row[8]
        result['location'] = row[9]
        return result

    def build_batterybyresourceid_dict(self, row):
        result = {}
        result['resourceid'] = row[0]
        result['name'] = row[1]
        result['resourcetypename'] = row[2]
        result['ammount'] = row[3]
        result['cost'] = row[4]
        result['purchasetypename'] = row[5]
        result['baterytype'] = row[6]
        result['quantityperpack'] = row[7]
        result['location']= row[8]
        return result

    def build_babyfoodbyresourceid_dict(self, row):
        result = {}
        result['resourceid'] = row[0]
        result['name'] = row[1]
        result['resourcetypename'] = row[2]
        result['ammount'] = row[3]
        result['cost'] = row[4]
        result['purchasetypename'] = row[5]
        result['flavor'] = row[6]
        result['expirationdate'] = row[7]
        result['location'] = row[8]
        return result

    def getAllResources(self):
        dao = ResourcesDAO()
        data = dao.getAllResources()
        result_list = []
        for row in data:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    # uses DAO method to find a specific resource tuple
    def getResourceById(self, rid):
        dao = ResourcesDAO()
        type = dao.getResourceTypeByResourceId(rid)[1]
        row=[]
        if type==1:
            dao = WaterDAO()
            row = dao.getWaterbyResourceId(rid)
            return jsonify(self.build_waterbyresourceid_dict(row))
        elif type == 2:
            dao = MedicationDAO()
            row = dao.getMedicationByResourceID(rid)
            return jsonify(self.build_medicationbyresourceid_dict(row))
        elif type == 3:
            dao = BabyFoodDAO()
            row = dao.getBabyFoodByResourceID(rid)
            return jsonify(self.build_babyfoodbyresourceid_dict(row))
        elif type == 4:
            dao = CannedFoodDAO()
            row = dao.getCannedFoodByResourceID(rid)
            return jsonify(self.build_cannedfoodbyresourceid_dict(row))
        elif type == 5:
            dao = DryFoodDAO()
            row = dao.getDryFoodByResourceId(rid)
            return jsonify(self.build_dryfoodbyresourceid_dict(row))
        elif type == 6:
            dao = IceDAO()
            row = dao.getIceByResourceID(rid)
            return jsonify(self.build_icebyresourceid_dict(row))
        elif type == 7:
            dao = FuelDAO()
            row = dao.getFuelByResourceId(rid)
            return jsonify(self.build_fuelbyresourceid_dict(row))

        elif type == 8:
            dao = MedicalDeviceDAO()
            row = dao.getMedicalDeviceById(rid)
            return jsonify(self.build_medicaldevicebyresourceid_dict(row))
        elif type == 9:
            dao = HeavyEquipmentDAO()
            row = dao.getHeavyEquipmentById(rid)
            return jsonify(self.build_heavyequipmentbyresourceid_dict(row))
        elif type == 10:
            dao = ToolsDAO()
            row = dao.getToolByResourceId(rid)
            return jsonify(self.build_toolbyresourceid_dict(row))
        elif type == 11:
            dao = ClothingDAO()
            row = dao.getClothingByresourceID(rid)
            return jsonify(self.build_clothingbyresourceid_dict(row))
        elif type == 12:
            dao = PowerGeneratorDAO()
            row = dao.getPowerGeneratorByResourceID(rid)
            return jsonify(self.build_powergeneratorbyresourceid_dict(row))
        elif type == 13:
            dao = BatteriesDAO()
            row = dao.getBatteryByResourceId(rid)
            return jsonify(self.build_batterybyresourceid_dict(row))

        if not row:
            return jsonify(Error="Resource Not Found"), 404
        else:
            return jsonify(Resource=row)





    # Searches for a resource, the way it is done depends on the input and its length,
    # name  are the 2 parameters this method accepts
    def searchResources(self, args):                                                     #Fixed
        name = args.get("name")
        cost = args.get("cost")
        dao = ResourcesDAO()
        if len(args) == 2 and name :
            resources_list = dao.getResourcesByNameAndCost(name, cost)
        elif len(args) == 1 and name:
            data = dao.getResourcesByName(name)
            resources_list=[]
            for row in data:
                resources_list.append(self.build_resource_dict(row))
        elif len(args) == 1 :
            resources_list = dao.getAllResourcesOrderedByCost(cost)
        else:
            return jsonify(Error="Malformed query string"), 400
        #result_list = []
        #for row in resources_list:
            #result = self.build_resource_dict(row)
            #result_list.append(result)
        return jsonify(Resources=resources_list)


    # inserts a resource into the database,
    # Restrictions: must be proper length to fill all attributes, which need to be properly matched
    #(no numbers in name field)
    def insertResourcesJson(self, form):
        userid=form['userid']
        resourcetypenumber = form['resourcetypenumber']
        ammount = form['ammount']
        cost = form['cost']
        name = form['name']
        purchasetypenumber = form['purchasetypenumber']

        if resourcetypenumber ==1:
            if len(form) == 8:
                watertype = form['watertypenumber']
                ounces = form['ounces']
                if userid and resourcetypenumber and ammount  and name and purchasetypenumber and watertype and ounces:
                    rdao = ResourcesDAO()
                    resourceid = rdao.insert(resourcetypenumber,ammount,cost,name,purchasetypenumber)[0]
                    sdao = SuppliesDAO()
                    sdao.insertSupplies(resourceid,userid)
                    wdao = WaterDAO()
                    wdao.insertWater(resourceid,watertype,ounces)
                    self.check_needed(resourceid,resourcetypenumber,ammount,purchasetypenumber,name)
                    return jsonify("New Resource has been added resourceid: " +str(resourceid))

            else:
                return jsonify(ERROR="Invalid Argumments")
        elif resourcetypenumber ==2:
            if len(form) == 11:
                active = form['activeingredient']
                descrp =form['description']
                concentration = form['concentration']
                quantity = form['quantity']
                date = form['expirationdate']
                if userid and resourcetypenumber and ammount  and name and purchasetypenumber and active and descrp and concentration and quantity and date :
                    rdao = ResourcesDAO()
                    resourceid = rdao.insert(resourcetypenumber, ammount, cost, name, purchasetypenumber)[0]
                    sdao = SuppliesDAO()
                    sdao.insertSupplies(resourceid, userid)
                    mdao = MedicationDAO()
                    mdao.insert(resourceid,active,descrp,concentration,quantity, date)
                    self.check_needed(resourceid, resourcetypenumber, ammount, purchasetypenumber, name)
                    return jsonify("New Resource has been added resourceid: " +str(resourceid))
            else:
                return jsonify(ERROR="Invalid Argumments")
        elif resourcetypenumber ==3:
            if len(form) == 8:
                flavor = form['flavor']
                expirationdate =form['expirationdate']
                if userid and resourcetypenumber and ammount  and name and purchasetypenumber and flavor and expirationdate:
                    rdao = ResourcesDAO()
                    resourceid = rdao.insert(resourcetypenumber, ammount, cost, name, purchasetypenumber)[0]
                    sdao = SuppliesDAO()
                    sdao.insertSupplies(resourceid, userid)
                    Bdao =BabyFoodDAO()
                    Bdao.insertBabyFood(resourceid,flavor,expirationdate)
                    self.check_needed(resourceid, resourcetypenumber, ammount, purchasetypenumber, name)
                    return jsonify("New Resource has been added resourceid: " +str(resourceid))
            else:
                return jsonify(ERROR="Invalid Argumments")
        elif resourcetypenumber ==4:
            if len(form) == 9:
                ingredient = form['primaryingredient']
                ounces = form['ounces']
                expirationdate = form['expirationdate']
                if userid and resourcetypenumber and ammount  and name and purchasetypenumber and ingredient and ounces and expirationdate :
                    rdao = ResourcesDAO()
                    resourceid = rdao.insert(resourcetypenumber, ammount, cost, name, purchasetypenumber)[0]
                    sdao = SuppliesDAO()
                    sdao.insertSupplies(resourceid, userid)
                    cdao = CannedFoodDAO()
                    cdao.insert(resourceid, ingredient, ounces, expirationdate)
                    self.check_needed(resourceid, resourcetypenumber, ammount, purchasetypenumber, name)
                    return jsonify("New Resource has been added resourceid: " +str(resourceid))
            else:
                return jsonify(ERROR="Invalid Argumments")
        elif resourcetypenumber ==5:
            if len(form) == 8:
                ounces = form['ounces']
                expirationdate = form['expirationdate']
                if userid and resourcetypenumber and ammount  and name and purchasetypenumber and ounces and expirationdate:
                    rdao = ResourcesDAO()
                    resourceid = rdao.insert(resourcetypenumber, ammount, cost, name, purchasetypenumber)[0]
                    sdao = SuppliesDAO()
                    sdao.insertSupplies(resourceid, userid)
                    ddao=DryFoodDAO()
                    ddao.insert(resourceid,ounces,expirationdate)
                    self.check_needed(resourceid, resourcetypenumber, ammount, purchasetypenumber, name)
                    return jsonify("New Resource has been added resourceid: " +str(resourceid))
            else:
                return jsonify(ERROR="Invalid Argumments")
        elif resourcetypenumber ==6:
            if len(form) == 7:
                weight = form['weight']
                if userid and resourcetypenumber and ammount  and name and purchasetypenumber and weight:
                    rdao = ResourcesDAO()
                    resourceid = rdao.insert(resourcetypenumber, ammount, cost, name, purchasetypenumber)[0]
                    sdao = SuppliesDAO()
                    sdao.insertSupplies(resourceid, userid)
                    idao=IceDAO()
                    idao.insert(resourceid,weight)
                    self.check_needed(resourceid, resourcetypenumber, ammount, purchasetypenumber, name)
                    return jsonify("New Resource has been added resourceid: " +str(resourceid))
            else:
                return jsonify(ERROR="Invalid Argumments")
        elif resourcetypenumber ==7:
            if len(form) == 8:
                fueltypenumber=form['fueltypenumber']
                litro =form['litro']
                if userid and resourcetypenumber and ammount  and name and purchasetypenumber and fueltypenumber and litro:
                    rdao = ResourcesDAO()
                    resourceid = rdao.insert(resourcetypenumber, ammount, cost, name, purchasetypenumber)[0]
                    sdao = SuppliesDAO()
                    sdao.insertSupplies(resourceid, userid)
                    fdao = FuelDAO()
                    fdao.insert(resourceid, fueltypenumber,litro)
                    self.check_needed(resourceid, resourcetypenumber, ammount, purchasetypenumber, name)
                    return jsonify("New Resource has been added resourceid: " +str(resourceid))
            else:
                return jsonify(ERROR="Invalid Argumments")
        elif resourcetypenumber ==8:
            if len(form) == 7:
                specs = form['specs']
                if userid and resourcetypenumber and ammount  and name and purchasetypenumber and specs:
                    rdao = ResourcesDAO()
                    resourceid = rdao.insert(resourcetypenumber, ammount, cost, name, purchasetypenumber)[0]
                    sdao = SuppliesDAO()
                    sdao.insertSupplies(resourceid, userid)
                    mdao= MedicalDeviceDAO()
                    mdao.insert(resourceid,specs)
                    self.check_needed(resourceid, resourcetypenumber, ammount, purchasetypenumber, name)
                    return jsonify("New Resource has been added resourceid: " +str(resourceid))
            else:
                return jsonify(ERROR="Invalid Argumments")
        elif resourcetypenumber ==9:
            if len(form) == 7:
                fueltype = form['fueltype']
                if userid and resourcetypenumber and ammount  and name and purchasetypenumber and fueltype:
                    rdao = ResourcesDAO()
                    resourceid = rdao.insert(resourcetypenumber, ammount, cost, name, purchasetypenumber)[0]
                    sdao = SuppliesDAO()
                    sdao.insertSupplies(resourceid, userid)
                    fdao = HeavyEquipmentDAO()
                    fdao.insert(resourceid, fueltype)
                    self.check_needed(resourceid, resourcetypenumber, ammount, purchasetypenumber, name)
                    return jsonify("New Resource has been added resourceid: " +str(resourceid))
            else:
                return jsonify(ERROR="Invalid Argumments")
        elif resourcetypenumber ==10:
            if len(form) == 7:
                size = form['size']

                if userid and resourcetypenumber and ammount  and name and purchasetypenumber and size:
                    rdao = ResourcesDAO()
                    resourceid = rdao.insert(resourcetypenumber, ammount, cost, name, purchasetypenumber)[0]
                    sdao = SuppliesDAO()
                    sdao.insertSupplies(resourceid, userid)
                    tdao = ToolsDAO()
                    tdao.insertTools(resourceid, size)
                    self.check_needed(resourceid, resourcetypenumber, ammount, purchasetypenumber, name)
                    return jsonify("New Resource has been added resourceid: " +str(resourceid))
            else:
                return jsonify(ERROR="Invalid Argumments")
        elif resourcetypenumber ==11:
            if len(form) == 8:
                agecategory = form['agecategory']
                size = form['size']

                if userid and resourcetypenumber and ammount and name and purchasetypenumber and agecategory and size:
                    rdao = ResourcesDAO()
                    resourceid = rdao.insert(resourcetypenumber, ammount, cost, name, purchasetypenumber)[0]
                    sdao = SuppliesDAO()
                    sdao.insertSupplies(resourceid, userid)
                    cdao=ClothingDAO()
                    cdao.insert(resourceid, agecategory, size)
                    self.check_needed(resourceid, resourcetypenumber, ammount, purchasetypenumber, name)
                    return jsonify("New Resource has been added resourceid: " +str(resourceid))
            else:
                return jsonify(ERROR="Invalid Argumments")
        elif resourcetypenumber ==12:
            if len(form) == 9:
                generatorfuel = form['generatorfuel']
                capacity =form['capacity']
                size = form['size']

                if userid and resourcetypenumber and ammount  and name and purchasetypenumber and generatorfuel and capacity and size:
                    rdao = ResourcesDAO()
                    resourceid = rdao.insert(resourcetypenumber, ammount, cost, name, purchasetypenumber)[0]
                    sdao = SuppliesDAO()
                    sdao.insertSupplies(resourceid, userid)
                    pdao = PowerGeneratorDAO()
                    pdao.insert(resourceid, generatorfuel, capacity, size)
                    self.check_needed(resourceid, resourcetypenumber, ammount, purchasetypenumber, name)
                    return jsonify("New Resource has been added resourceid: " +str(resourceid))
            else:
                return jsonify(ERROR="Invalid Argumments")
        elif resourcetypenumber ==13:
            if len(form) == 8:
                baterytype = form['baterytype']
                quantityperpack = form['quantityperpack']
                if userid and resourcetypenumber and ammount  and name and purchasetypenumber and baterytype and quantityperpack:
                    rdao = ResourcesDAO()
                    resourceid = rdao.insert(resourcetypenumber, ammount, cost, name, purchasetypenumber)[0]
                    sdao = SuppliesDAO()
                    sdao.insertSupplies(resourceid, userid)
                    bdao = BatteriesDAO()
                    bdao.insert(resourceid, baterytype, quantityperpack)
                    self.check_needed(resourceid, resourcetypenumber, ammount, purchasetypenumber, name)
                    return jsonify("New Resource has been added resourceid: " +str(resourceid))
            else:
                return jsonify(ERROR="Invalid Argumments")
        else:
            return jsonify(Error= "invalid type argument")


    # allocates a specified resource and the amount(by id) to a specific supplier


    # Uses DAO to delete a resource by id
    def deleteResource(self, rid):
        dao = ResourcesDAO()
        if not dao.getResourceById(rid):
            return jsonify(Error="Resource not found."), 404
        else:
            dao.delete(rid)
            return jsonify(DeleteStatus="Resource deleted"), 200

    # updates a resource's attributes if it exists
    # input must have the right length and proper arguments
    def updateResource(self, rid, form):
        dao = ResourcesDAO()
        if not dao.getResourceById(rid):
            return jsonify(Error="Resource not found."), 404
        else:
            if len(form) != 4:
                return jsonify(Error="Malformed update request"), 400
            else:
                sid = form['sid']
                resv_amount = form['resv_amount']
                cost = form['cost']
                rname = form['rname']
                if rname and resv_amount  and sid:
                    dao.update(rid, sid, rname, cost, resv_amount)
                    result = self.build_resource_attributes(rid, sid, rname, cost, resv_amount)
                    return jsonify(Resource=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    # Used to establish the amount of resources
    def build_resource_counts(self, resource_counts):
        result = []
        # print(resource_counts)
        for P in resource_counts:
            D = {}
            D['id'] = P[0]
            D['name'] = P[1]
            D['count'] = P[2]
            result.append(D)
        return result

    # returns the amount of the specified resource (using id)
    def getCountByResourceId(self):
        dao = ResourcesDAO()
        result = dao.getCountByResourceId()
        return jsonify(ResourceCounts=self.build_resource_counts(result)), 200

    def check_needed(self, resourceid, resourcetypenumber, ammount,purchasetypenumber,name):
        rdao = ResourcesDAO()
        necesitados = rdao.get_necesitados(resourcetypenumber,ammount,purchasetypenumber)

        for row in necesitados:
            resourceammount = rdao.get_resource_ammount(resourceid)[0]
            if row[1]<= resourceammount:
                reqdao = RequestDAO()
                seldao = SelectedDAO()
                requestid = reqdao.insertrequest(row[2])[0]
                seldao.insertSelected(requestid,resourceid,row[1])
                ndao =NeededDAO()
                ndao.update_status(row[0],False)
                print("Request added")
            else:
                pass
        pass


