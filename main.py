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

for command in history:
    if command[0] == "saldo":
        balance_change = command[1]
        if balance + balance_change < 0:
            print("Błąd. Za mało środków na koncie.")
            break
        balance += balance_change
    elif command[0] == "zakup":
        purchase_price = command[2] * command[3]
        if balance < purchase_price:
            print("Błąd, nie stać cię na zakup.")
            break
        balance -= purchase_price
        names.append(command[1])
        amounts.append(command[3])
        for idx in range(len(names)):
            warehouse[names[idx]] = amounts[idx]
    elif command[0] == "sprzedaz":
        sale_price = command[2] * command[3]
        balance += sale_price
        for idx in warehouse:
            if idx == command[1]:
                old_value = warehouse[idx]
                new_value = old_value - command[3]
                amounts.remove(command[3])
                amounts.append(new_value)
                for idx in range(len(names)):
                    warehouse[names[idx]] = amounts[idx]
            else:
                print("Nie posiadasz wystarczającej ilości.")
                break

if action == "saldo":
    print(balance)
elif action == "zakup":
    print(history)
elif action == "sprzedaz":
    print(history)
elif action == "magazyn":
    print(warehouse)
elif action == "konto":
    print(balance)

