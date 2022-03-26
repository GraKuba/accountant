import sys

# GLOBAL VARIABLES

balance = 0
history = []
warehouse = {}
command = []
names = []
amounts = []

# POBIERANIE HISTORII Z PLIKU CSV

while True:
    action = input()
    if action == "saldo":
        balance_change = int(input())
        comment = input()
        balance_tuple = "saldo", balance_change, comment
        history.append(balance_tuple)
        continue
    elif action == "sprzedaz" or action == "zakup":
        product_name = input()
        product_price = int(input())
        number_of_items = int(input())
        balance_tuple = action, product_name, product_price, number_of_items
        history.append(balance_tuple)
        continue
    else:
        if action == "stop" or False:
            break
