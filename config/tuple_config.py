order = []
order.append(1)  # order ID
order.append(2)  # consumer ID
order.append('water')  # resource name
order.append(212)  # amount reserved
order.append(200)  # amount bought
order.append('21/01/2020')  # date

user_cons = []
user_cons.append(2)  # user ID
user_cons.append('Elvis Presley')  # username
user_cons.append('bb')  # password
user_cons.append('Elvis')  # first name
user_cons.append('Presley')  # last name
user_cons.append('9396463533')  # phone
user_cons.append('calorina')

user_supp_admin = []  # a second user
user_supp_admin.append(1)
user_supp_admin.append('Antobici')
user_supp_admin.append('wordpass')
user_supp_admin.append('Antonio')
user_supp_admin.append('Bicicletas')
user_supp_admin.append('7875555555')
user_supp_admin.append('mayaguez')

resource = []
resource.append(1)  # resource ID
resource.append(user_supp_admin[0])  # user ID
resource.append('salchicha')  # resource name
resource.append(0.60)  # resource price
resource.append(100)  # amount that this supplier has that can be reserved
resource.append(230)  # amount that this supplier has that can be bought
resource.append('Mayaguez')  # location

transaction = []
transaction.append(1)  # transaction ID
transaction.append('visa')  # payment method
value = 'your total is' + str(order[3] * resource[3])
transaction.append(value)  # total amount to pay

supplier = []
supplier.append(1)  # supplier ID
supplier.append(user_supp_admin[0])  # user ID

admin = []
admin.append(1)  # admin ID
admin.append(user_supp_admin[0])  # user ID

consumer = []
consumer.append(1)  # consumer ID
consumer.append(user_cons[0])  # user ID


inserted = []
inserted.append(3)
inserted.append("Maytin")
inserted.append("comida")
inserted.append("Maya")
inserted.append("Valentin")
inserted.append("7871234567")
inserted.append("Link")
