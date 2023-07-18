from models.transaction import Transaction
from datetime import date

transaction1 = Transaction("Pepparoni Pizza", date(2023, 4, 30), 11.00)
transaction2 = Transaction("Margarita Pizza", date(2030, 6, 23), 9.00)
transaction3 = Transaction("Funghi", date(2023, 6, 26), 10.00)
transaction4 = Transaction("Pineapple Pizza", date(2023, 7, 4), 12.00)

transactions = [transaction1, transaction2, transaction3, transaction4]
