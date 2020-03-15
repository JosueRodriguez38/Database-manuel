order = []
order.append(1)  # order ID
order.append('water')  # resource name
order.append(212)  # amount reserved
order.append(200)  # amount bought
order.append('21/01/2020')  # date

user_cons = []
user_cons.apend(1)  # user ID
user_cons.apend('Elvis Presley')  # username
user_cons.apend('bb')  # password
user_cons.apend('Elvis')  # first name
user_cons.apend('Presley')  # last name
user_cons.apend('9396463533')  # phone
user_cons.apend(
    'https://www.google.com/maps/place/UPRM/@18.2108946,-67.1430912,17z/data=!3m1!4b1!4m5!3m4!1s0x8c02b3ccfeb38ac3:0xd285b5144bc722b0!8m2!3d18.2108895!4d-67.1409025')  # location

user_supp_admin = []  # a second user
user_supp_admin.apend(1)
user_supp_admin.apend('Pablo_Escobar')
user_supp_admin.apend('wordpass')
user_supp_admin.apend('Antonio')
user_supp_admin.apend('Bicicletas')
user_supp_admin.apend('7875555555')
user_supp_admin.apend(
    'https://www.google.com/maps/place/UPRM/@18.2108946,-67.1430912,17z/data=!3m1!4b1!4m5!3m4!1s0x8c02b3ccfeb38ac3:0xd285b5144bc722b0!8m2!3d18.2108895!4d-67.1409025')

resource = []
resource.append(1)  # resource ID
resource.append(user_supp_admin[0])  # user ID
resource.append('salchicha')  # resource name
resource.append(0.60)  # resource price
resource.append(100)  # amount that this supplier has that can be reserved
resource.append(230)  # amount that this supplier has that can be bought
resource.append('nose q va aqui')  # location

transaction = []
transaction.append(1)  # transaction ID
transaction.append('visa')  # payment method
transaction.append('your total is' + (order[3] * resource[3]))  # total amount to pay

supplier = []
supplier.append(1)  # supplier ID
supplier.append(user_supp_admin[0])  # user ID

admin = []
admin.append(1)  # admin ID
admin.append(user_supp_admin[0])  # user ID

consumer = []
consumer.append(1)  # consumer ID
consumer.append(user_cons[0])  # user ID
