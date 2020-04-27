from config.dbconfig import pg_config
from config.tuple_config import order, user_cons
import psycopg2


class OrderDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

        # ALGUNOS DE ESTOS YA ESTAN EN LOS FILES ESTO ES SOLO PARA ESTAR SEGUROS Y FINALIZAR
        # A LA MAYPRIA LES CAMBIE ALGO, VERIFIQUEN Y ME AVISAN SI ESTA BIEN PARA ESCRIBIRLOS EN EL LUGAR CORRECTO

    # 1
    def getUserInfoFromorder(self, uid):
        cursor = self.conn.cursor()
        query = "select * from user where uid = (select uid from order where uid = %s)"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result

    # 2 Esta en el file order, creo que el query deberia seleccionar todo. cambie el return ahora devuleve todas las
    #  ordenes de ese resource
    def getOrdersByresourceName(self, resourceName):
        cursor = self.conn.cursor()
        query = "select resourceName, date from Order where resourceName = %s"
        cursor.execute(query, (resourceName,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # 3 Todos los resources DISPONIBLES
    def getAllAvailableResources(self):
        cursor = self.conn.cursor()
        query = "select resourceName, reservedAmmount, buyableAmmount from Resources where reservedAmmount > 0 or buyableAmmount > 0"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Chequea si 1 resource en especifico esta disponible
    def getResourceById(self, rid):
        cursor = self.conn.cursor()
        query = "select resourceName, reservedAmmount, buyableAmmount, location from Resources where rid = &s and (reservedAmmount > 0 or buyableAmmount > 0)"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    # 4 no entendi la diferenca entre esta y el 3

    #5
    def getUsersOrders(self, uid):
        cursor = self.conn.cursor()
        query = "select * from order where uid = %s"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    # asi o como en el siguiente ( verificar tablas y preguntar a Ismael
    def getUsersOrders(self, uid):
        cursor = self.conn.cursor()
        query = "select * from order where uid = %s"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result