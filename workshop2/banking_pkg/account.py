def show_balance(balance):
    if balance == 0:
        return int(balance)
    else:
        return float(balance)
def deposit(balance):
    amount = int(input('Enter an amount to deposit: '))
    balance += amount
    return balance
def withdraw(balance):
    withdraw = int(input('Enter amount to withdraw: '))
    if balance >= withdraw:
        balance -= withdraw
    else:
        print('Where are you going to get that kind of money?')
    return balance
def logout(name):
    print('Goodbye', name)
