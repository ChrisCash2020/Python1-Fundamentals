class User: 
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password
    def change_name(self, name):
        self.name = name
    def change_pin(self, pin):
        self.pin = pin
    def change_password(self, password):
        self.password = password
bank_user_database = {}
class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0
        bank_user_database[name] = [pin, password, self.balance]
    def amt_validation(self, amt_val):
        if type(amt_val) == str or amt_val <= 0:
            print('Only positive numbers can be deposited, withdrawn, transferred, and requested')
            return True
        else:
            return False

    def show_balance(self):
        print(self.name, "has an account balance of:", float(self.balance) if self.balance > 0 else int(self.balance))

    def witdraw(self, amt):
        
        self.balance -= amt 
        return self.balance
    
    def deposit(self, amt):
        self.balance += amt
        return self.balance

    def transfer_money(self, reciever, amt):
        def show_all_balances():
            print(self.name, "has an account balance of:", float(self.balance) if self.balance > 0 else int(self.balance))
            print(reciever, "has an account balance of:", int(receiver_balance) if receiver_balance == 0 else float(receiver_balance))
        if reciever in bank_user_database:
            receiver_balance = bank_user_database[reciever][2]
            show_all_balances()
            print("You are transfering $" + str(amt) + " to " + reciever)
            print("Authentication required")
            pin = float(input("Enter your PIN: "))
            if self.pin == pin:
                self.balance -= amt
                bank_user_database[self.name][2] = self.balance 
                receiver_balance += amt
                bank_user_database[reciever][2] = receiver_balance
                print("Transfer Authorized\nTransfering $" + str(amt) + " to " + reciever)
                show_all_balances()
                return bank_user_database
            else:
                print('Invalid PIN. Transaction canceled.')
                show_all_balances()
                return False
        else:
            print('Bank recipient not found')
    
    def request_money(self, recipient, amt):
        def show_all_balances():
            print(self.name, "has an account balance of:", float(self.balance) if self.balance > 0 else int(self.balance))
            print(recipient, "has an account balance of:", float(recipient_balance) if recipient_balance > 0 else int(recipient_balance))
        if recipient in bank_user_database:
            recipient_balance = bank_user_database[recipient][2]
            recipient_pin = bank_user_database[recipient][0]
            show_all_balances()
            print("You are requesting $" + str(amt) + " from " + recipient)
            print("User authentication required")
            pin = float(input("Enter "  + recipient + "'s PIN: "))
            if recipient_pin == pin:
                password = input("Enter your password: ")
                if self.password == password:
                    self.balance += amt
                    recipient_balance -= amt
                    print('Request authorized\n' + recipient + ' sent $' + str(amt))
                    show_all_balances()
                    return True
                else:
                    print('Invalid Password. Transaction canceled')
                    show_all_balances()
                    return False
            else: 
                print('Invalid PIN. Transaction canceled.')
                show_all_balances()
                return False
        else:
            print('Bank recipient not found')

""" Driver Code for Task 1 """
# user1 = User("Bob", 1234, "password")
# print(user1.name, user1.pin, user1.password)

""" Driver Code for Task 2 """
# user1.change_name("Bobby"), user1.change_pin(4321), user1.change_password('newpassword')
# print(user1.name, user1.pin, user1.password)

""" Driver Code for Task 3 """
bankuser = BankUser("Bob", 1234, "password")
bankuser2 = BankUser("Alice", 5678, "alicepassword")
bankuser2.deposit(5000)
print(bank_user_database)
""" Driver Code for Task 4 """
# bankuser.show_balance()
# bankuser.deposit(1000)
# bankuser.show_balance()
# bankuser.witdraw(500)
# bankuser.show_balance()
""" Driver Code for Task 4 """
bankuser2.transfer_money(bankuser.name, 500)
print()
bankuser2.request_money(bankuser.name, 250)
print(bank_user_database)