from banking_pkg import account
import re
def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")
print("          === Automated Teller Machine ===          ")
name = input('Enter name to register: ')
while True:
    if len(name) >= 1 or len(name) >= 10:
        break
    else:
        print('The maximum name length is 10 character.')
        name = input('Enter name to register: ')
        continue
pin = input('Enter PIN: ')
while True:
    if bool(re.match('[0-9]{4}$', pin)) == False:
        print('PIN must contain 4 numbers.')
        pin = input('Enter PIN: ')
        continue
    else:
        break
balance = 0
print(name + ' has been registered with a starting balance of $' + str(balance))
while True:
    print("          === Automated Teller Machine ===          ")
    print('LOGIN')
    name_to_validate = input('Enter name: ')
    pin_to_validate = input('Enter PIN:  ')
    if name_to_validate == name and pin_to_validate == pin:
        print('Login successful!')
        break
    else:
        print('Invalid Credentials!')
        continue
while True:
    atm_menu(name)
    option = int(input('Choose an option: '))
    if option == 1:
        print('Current Balance: $' + str(account.show_balance(balance)))
        continue
    elif option == 2:
        balance = account.deposit(balance)
        print('Current Balance: $' + str(account.show_balance(balance)))
        continue
    elif option == 3:
        balance = account.withdraw(balance)
        print('Current Balance: $' + str(account.show_balance(balance)))
        continue
    elif option == 4:
        account.logout(name)
        break
    else:
        print('Invalide Option!')
        continue
