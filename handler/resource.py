from flask import jsonify

from dao.resource import ResourcesDAO
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
from dao.Supplies import SuppliesDAO



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
        type = dao.getResourceTypeByResourceId(rid)[0]
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
            row = dao.getDryFoodById(rid)
        elif type == 6:
            dao = IceDAO()
            row = dao.getIceByID(rid)
        elif type == 7:
            dao =  FuelDAO()
            row = dao.getFuelById(rid)
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
    # name and cost are the 2 parameters this method accepts
    def searchResources(self, args):                                                     #Fixed
        name = args.get("name")
        cost = args.get("cost")
        dao = ResourcesDAO()
        resources_list = []
        if len(args) == 2 and name and cost:
            resources_list = dao.getResourcesByNameAndCost(name, cost)
        elif len(args) == 1 and name:
            resources_list = dao.getResourcesByName(name)
        elif len(args) == 1 and cost:
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
        resourceType = form['resourceTypeNumber']
        if not resourceType:
            return jsonify(Error="Malformed post request"), 400
        else:
            ammount = form['ammount']
            cost = form['cost']
            aviable = form['aviable']
            name = form['name']
            purchaseType = form['purchaseTypeNumber']
            uid = form['userid']
            if ammount and cost and aviable and name and purchaseType and uid:
                dao = ResourcesDAO()
                rid = dao.insert(resourceType, ammount, cost, name, name, purchaseType)
                suppliesdao = SuppliesDAO()
                suppliesdao.insertSuppies(rid, uid)
            else:
                return jsonify(Error="Malformed post request"), 400

        if resourceType == 1:
            waterTypeNumber = form['waterTypeNumber']
            ounces = form['ounces']
            if waterTypeNumber and ounces:
                waterdao = WaterDAO()
                waterdao.insertWater(rid, watertypenumber, ounces)
                return jsonify(PostStatus="New resource added"), 201
            else:
                return jsonify(Error="Malformed post request"), 400

        elif resourceType == 2:
            activeIngredient = form['activeIngredient']
            description = form['description']
            concentration = form['concentration']
            quantity = form['quantity']
            expirationdate = form['expirationdate']
            if activeIngredient and description and concentration and quantity and expirationdate:
                medicationdao = MedicationDAO()
                medicationdao.insertMedications(rid, activeIngredient, description, concentration, quantity, expirationdate)
                return jsonify(PostStatus="New resource added"), 201
            else:
                return jsonify(Error="Malformed post request"), 400

        elif resourceType == 3:
            flavor = form['flavor']
            expirationdate = form['expirationdate']
            if flavor and expirationdate:
                babydao = BabyFoodDAO()
                babydao.insertBabyFood(rid, flavor, expirationdate)
                return jsonify(PostStatus="New resource added"), 201
            else:
                return jsonify(Error="Malformed post request"), 400

        elif resourceType == 4:
            primaryIngredient = form['primaryIngredient']
            ounces = form['ounces']
            expirationdate = form['expirationdate']
            if primaryIngredient and ounces and expirationdate:
                canneddao = CannedFoodDAO()
                canneddao.insertCannedFood(rid, primaryIngredient, ounces, expirationdate)
                return jsonify(PostStatus="New resource added"), 201
            else:
                return jsonify(Error="Malformed post request"), 400

        elif resourceType == 5:
            ounces = form['ounces']
            expirationdate = form['expirationdate']
            if ounces and expirationdate:
                dryfooddao = DryFoodDAO()
                dryfooddao.insertDryFood(rid, ounces, expirationdate)
                return jsonify(PostStatus="New resource added"), 201
            else:
                return jsonify(Error="Malformed post request"), 400

        elif resourceType == 6:
            weight = form['weight']
            if weight:
                icedao = IceDAO()
                icedao.insertIce(rid, weight)
                return jsonify(PostStatus="New resource added"), 201
            else:
                return jsonify(Error="Malformed post request"), 400

        elif resourceType == 7:
            fuelTypeNumber = form['fuelTypeNumber']
            litro = form['litro']
            if fuelTypeNumber and litro:
                fueldao = FuelDAO()
                fueldao.insertFuel(rid, litro)
                return jsonify(PostStatus="New resource added"), 201
            else:
                return jsonify(Error="Malformed post request"), 400

        elif resourceType == 8:
            specs = form['specs']
            if specs:
                medicalDevicedao = MedicalDeviceDAO()
                medicalDevicedao.insertMedicalDevices(rid, specs)
                return jsonify(PostStatus="New resource added"), 201
            else:
                return jsonify(Error="Malformed post request"), 400

        elif resourceType == 9:
            fuelType = form['fuelType']
            if fuelType:
                heavyEquipmentdao = HeavyEquipmentDAO()
                heavyEquipmentdao.insertHeavyEquipment(rid, fuelType)
                return jsonify(PostStatus="New resource added"), 201
            else:
                return jsonify(Error="Malformed post request"), 400

        elif resourceType == 10:
            size = form['size']
            if size:
                tooldao = ToolsDAO()
                tooldao.insertTools(rid, size)
                return jsonify(PostStatus="New resource added"), 201
            else:
                return jsonify(Error="Malformed post request"), 400

        elif resourceType == 11:
            generatorFuel = form['generatorFuel']
            capacity = form['capacity']
            size = form['size']
            if generatorFuel and capacity and size:
                powerGendao = PowerGeneratorDAO()
                powerGendao.insertPowerGenerators(rid, generatorFuel, capacity, size)
                return jsonify(PostStatus="New resource added"), 201
            else:
                return jsonify(Error="Malformed post request"), 400

        elif resourceType == 12:
            ageCategory = form['ageCategory']
            size = form['size']
            if ageCategory and size:
                clothingdao = ClothingDAO()
                clothingdao.insertClothing(rid, ageCategory, size)
                return jsonify(PostStatus="New resource added"), 201
            else:
                return jsonify(Error="Malformed post request"), 400

        elif resourceType == 13:
            batteryType = form['batteryType']
            quantityPerPack = form['quantityPerPack']
            if batteryType and quantityPerPack:
                batterydao = BatteriesDAO()
                batterydao.insertBatteries(rid, batteryType, quantityPerPack)
                return jsonify(PostStatus="New resource added"), 201
            else:
                return jsonify(Error="Malformed post request"), 400

        else:
            return jsonify(Error="Unexpected attributes in post request"), 400



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
                if rname and resv_amount and cost and sid:
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
