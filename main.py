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

# POBIERZ DANE Z TERMINALA O DANEJ AKCJI
new_tuple = ()
action = sys.argv[1]
if len(sys.argv) > 2:
    if action == "saldo":
        name = action
        balance_change = int(sys.argv[2])
        comment = sys.argv[3]
        new_tuple = action, balance_change, comment
        history.append(new_tuple)
    elif action == "zakup" or action == "sprzedaz":
        name = action
        product_name = sys.argv[2]
        product_price = int(sys.argv[3])
        product_amount = int(sys.argv[4])
        new_tuple = action, product_name, product_price, product_amount
        history.append(new_tuple)
    elif action == "przeglad":
        number_of_commands = len(sys.argv)
        command_number = sys.argv[2:number_of_commands]
        for number in command_number:
            print(history[int(number)])
