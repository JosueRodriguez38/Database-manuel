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



# Uses resource DAO to build results for displaying in localhost
#this class involves supplier,

class ResourceHandler:

    # builds resource tuple with the space required to insert the information required
    def build_resource_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['sid'] = row[1]
        result['rname'] = row[2]
        result['cost'] = row[3]
        result['resAmount'] = row[4]
        result['buyable'] = row[5]
        result['location'] = row[6]

        return result

    #builds supplier tuple with the space required to insert the information required
    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['sname'] = row[1]
        result['sphone'] = row[2]
        result['semail'] = row[3]
        result['scity'] = row[4]
        return result

    # builds tuple for resource with specified field values
    def build_resource_attributes(self, rid, sid, rname, cost, resv_amount):
        result = {}
        result['rid'] = rid
        result['sid'] = sid
        result['cost'] = rname
        result['rname'] = cost
        result['resv_amount'] = resv_amount
        return result





    def build_water_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['watertypenumber'] = row[1]
        result['ounces'] = row[2]
        return result


    def build_water_attributes(self, rid, watertypenunmber,ounces):
        result = {}
        result['rid'] = rid
        result['watertypenumber'] = watertypenunmber
        result['ounces'] = ounces
        return result

    def build_tool_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['size'] = row[1]
        return result

    def build_tool_attributes(self, rid, size):
        result = {}
        result['rid'] = rid
        result['size'] = size
        return result

    def build_generator_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['generatorfuel'] = row[1]
        result['capacity'] = row[2]
        result['size'] = row[3]
        return result

    def build_generator_attributes(self, rid, generatorfuel, capacity, size):
        result = {}
        result['rid'] = rid
        result['generatorfuel'] = generatorfuel
        result['capacity'] = capacity
        result['size'] = size
        return result

    def build_medication_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['active ingridient'] = row[1]
        result['description'] = row[2]
        result['concentration'] = row[3]
        result['quantity'] = row[4]
        result['expiration date'] = row[5]
        return result

    def build_medication_attributes(self, rid,activeingridient, description, concentration, quatity, expirationdate):
        result = {}
        result['rid'] = rid
        result['active ingridient'] = activeingridient
        result['description'] = description
        result['concentration'] = concentration
        result['quantity'] = quatity
        result['expiration date'] = expirationdate
        return result

    def build_medicalDevice_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['specs'] = row[1]
        return result

    def build_medicalDevice_attributes(self, rid, specs):
        result = {}
        result['rid'] = rid
        result['specs'] = specs
        return result

    def build_ice_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['weight'] = row[1]
        return result

    def build_ice_attributes(self, rid, weight):
        result = {}
        result['rid'] = rid
        result['weight'] = weight
        return result

    def build_heavyequip_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['fuel type'] = row[1]
        return result

    def build_heavyequip_attributes(self, rid, fueltype ):
        result = {}
        result['rid'] = rid
        result['fueltype'] = fueltype
        return result

    def build_babyfood_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['flavor'] = row[1]
        result['expiration date'] = row[2]
        return result

    def build_babyfood_attributes(self, rid, flavor, expirationdate):
        result = {}
        result['rid'] = rid
        result['flavor'] = flavor
        result['expiration date'] = expirationdate
        return result

    def build_batteries_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['batterytype'] = row[1]
        result['quantity per pack'] = row[2]
        return result

    def build_batteries_attributes(self, rid,batterytype, quantityperpack):
        result = {}
        result['rid'] = rid
        result['batterytype'] = batterytype
        result['quantity per pack'] = quantityperpack
        return result

    def build_clothing_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['agecategory'] = row[1]
        result['size'] = row[2]
        return result

    def build_clothing_attributes(self, rid, agecategory, size):
        result = {}
        result['rid'] = rid
        result['agecategory'] = agecategory
        result['size'] = size
        return result

    # uses DAO method to access all resource tuples and adds them to a list, where jsonify is used
    def getAllResources(self):
        dao = ResourcesDAO()
        resources_list = dao.getAllResources()
        result_list = []
        #for row in resources_list:
           # result = self.build_resource_dict(row)
            #result_list.append(result)
        return jsonify(Resources=resources_list)

    # uses DAO method to find a specific resource tuple
    def getResourceById(self, rid):
        dao = ResourcesDAO()
        type = dao.getResourceTypeByResourceId(rid)[1]
        row=[]
        if type==1:
            dao = WaterDAO()
            row = dao.getWaterbyResourceId(rid)

        elif type == 2:
            dao = MedicationDAO()
            row = dao.getMedicationByResourceID(rid)

        elif type == 3:
            dao = BabyFoodDAO()
            row = dao.getBabyFoodByResourceID(rid)

        elif type == 4:
            dao = CannedFoodDAO()
            row = dao.getCannedFoodByResourceID(rid)
        elif type == 5:
            dao = DryFoodDAO()
            row = dao.getDryFoodByResourceId(rid)
        elif type == 6:
            dao = IceDAO()
            row = dao.getIceByResourceID(rid)
        elif type == 7:
            dao =  FuelDAO()
            row = dao.getFuelByResourceId(rid)
        elif type == 8:
            dao = MedicalDeviceDAO()
            row = dao.getMedicalDeviceById(rid)
        elif type == 9:
            dao = HeavyEquipmentDAO()
            row = dao.getHeavyEquipmentById(rid)
        elif type == 10:
            dao = ToolsDAO()
            row = dao.getToolByResourceId(rid)
        elif type == 11:
            dao = ClothingDAO()
            row = dao.getClothingByresourceID(rid)
        elif type == 12:
            dao = PowerGeneratorDAO()
            row = dao.getPowerGeneratorByResourceID(rid)
        elif type == 13:
            dao = BatteriesDAO()
            row = dao.getBatteryByResourceId(rid)

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
        resources_list = []
        if len(args) == 2 and name :
            resources_list = dao.getResourcesByNameAndCost(name, cost)
        elif len(args) == 1 and name:
            resources_list = dao.getResourcesByName(name)
        elif len(args) == 1 :
            resources_list = dao.getResourcesByCost(cost)
        else:
            return jsonify(Error="Malformed query string"), 400
        #result_list = []
        #for row in resources_list:
            #result = self.build_resource_dict(row)
            #result_list.append(result)
        return jsonify(Resources=resources_list)

    # Uses DAO method of the same name to find the resource with a specific id
    def getSuppliersByResourceId(self, rid):
        dao = ResourcesDAO()
        if not dao.getResourceById(rid):
            return jsonify(Error="Resource Not Found"), 404
        suppliers_list = dao.getSuppliersByResourceId(rid)
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

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
        # print(self.build_resource_counts(result))
        return jsonify(ResourceCounts=self.build_resource_counts(result)), 200
