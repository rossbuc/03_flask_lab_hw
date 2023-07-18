from ast import Or
from models.order import Order
from datetime import date

order1 = Order("Dennis", date(2023, 4, 30), 1, "Pepparoni")
order2 = Order("Charlie", date(2030, 6, 23), 1, "Margarita")
order3 = Order("Dee", date(2023, 6, 26), 1, "Funghi")
order4 = Order("Frank", date(2023, 7, 4), 1, "Pineapple")

orders = [order1, order2, order3, order4]