# import csv
#
#
# class Client:
#     def __init__(self, name, balance):
#         self.name = name
#         self._balance = balance
#
#     def __str__(self):
#         return f"name: {self.name}, Balance:{self._balance}"
#
#
# class Bank(Client):
#     def __init__(self, clients):
#         self.clients = []
#
#     def add(self):
#         new_client = ""
#         self.clients.append(new_client)
#
#     def show(self, new_client, clients):
#         for index, new_client in enumerate(self.clients, start=1):
#             print(index, self.clients)
#
#     def search(self, client):
#         if client in self.clients:
#             print(client)
#         else:
#             print("This client does not exist")
#
#     def save(self, filename):
#         try:
#             with open(filename, "w", newline='') as f:
#                 writer = csv.reader()
#                 for self.client in self.clients:
#                     writer.writerow(self.clients)
#                     print("File save correctly")
#         except:
#             print("Cannot open file!")
#
#     def download(self, filename):
#         try:
#             with open(filename, "r", newline='') as f:
#                 reader = csv.reader()
#                 for row in reader:
#                     self.clients = row
#         except:
#             print("File cannot open!")
#
#     def menu(self):
#         while True:
#             print("""
#             1 - Add
#             2 - Show
#             3 - Search
#             4 - Save
#             5 - Download
#             6 - Quit
#             """)
#             choice = input("Enter your choice")
#             if choice == "1":
#                 new_client = input("Enter new client")
#                 self.add()
#             if choice == "2":
#                 for index, new_client in enumerate(self.clients, start=1):
#                     print(index, self.clients)
#             if choice == "3":
#                 client = input("Enter your client")
#                 self.search(client)
#             if choice == "4":
#                 filename = input("Enter filename")
#                 self.save(filename)
#             if choice == "5":
#                 filename = input("Enter filename")
#                 self.download(filename)
#             if choice == "6":
#                 print("Goodbye")
#                 break

# Task 2
# class price_dol:
#     def __get__(self, instance, owner):
#         dol = 36
#         coin = instance.coin
#         cot = instance.cot
#         p_dol = sum(coin[name] * cot[name] for name in coin)
#         return p_dol
#
#
# class Bag:
#     dol_p = price_dol()
#
#     def __init__(self, name_inv):
#         self.name_inv = name_inv
#         self.coin = {}
#         self.cot = {}
#
#     def add(self, name, count):
#         if name in self.coin:
#             self.coin[name] += count
#         else:
#             self.coin[name] = count
#
#     def delete(self, name):
#         if name == self.coin:
#             del self.coin[name]
#         else:
#             print("Error, print correct coin")
#
#     def show(self):
#         for name, self.count in self.coin.items():
#             coin_p = self.cot.get(name, 0)
#             print(f"{name}: {self.count} coins, Price: ${coin_p}")
#
#     def sort(self):
#         sort_p = sorted(self.coin.items())
#         return dict(sort_p)
#
#     def menu(self):
#         while True:
#             print("""
#             1 - Add
#             2 - Delete
#             3 - Show
#             4 - Sort
#             5 - Quit
#             """)
#             choice = input("Enter your choice")
#             if choice == "1":
#                 name = input("Enter name")
#                 self.add(name)
#             if choice == "2":
#                 name = input("Enter name")
#                 self.delete(name)
#             if choice == "3":
#                 self.show()
#             if choice == "4":
#                 self.sort()
#             if choice == "5":
#                 print("Goodbye")
#                 break


# Task 3
# class ATM:
#     def __init__(self, balance):
#         self.balance = balance
#         self.users = {}
#
#
# class User:
#     def __init__(self, name, pin, balance):
#         self.name = name
#         self.pin = pin
#         self.balance = balance
#
#
#     def create_new_account(self, name, pin, n_balance):
#         new_user = User(name, pin, n_balance)
#         self.new_user = new_user
#
#     def open_account(self, p_pin):
#         if self.pin == int(p_pin):
#             print("Welcome!")
#             print(self.balance)
#         else:
#             raise ValueError("This PIN wrong. Please, Try again.")
#
#     def withdraw_money(self, p_balance):
#         p_balance = int(p_balance)
#         if self.balance < p_balance:
#             print("There is not enough money in the account!")
#         else:
#             self.balance -= p_balance
#             print(f"You have withdrawn from your account{p_balance}")
#             print(self.balance)
#
#     def menu(self):
#         while True:
#             print("""
#             1 - Create new account
#             2 - Open account
#             3 - Withdraw money
#             4 - Quit
#             """)
#             choice = input("Enter your choice")
#             if choice == "1":
#                 name = input("Enter name")
#                 pin = int(input("Enter new pin."))
#                 n_balance = int(input("Enter new balance"))
#                 self.create_new_account(name, pin, n_balance)
#             if choice == "2":
#                 name = input("Enter name")
#                 pin = input("Enter pin")
#                 self.open_account(pin)
#             if choice == "3":
#                 balance = input("Enter the amount you want to withdraw")
#                 self.withdraw_money(balance)
#             if choice == "4":
#                 print("Goodbye")
#                 break


