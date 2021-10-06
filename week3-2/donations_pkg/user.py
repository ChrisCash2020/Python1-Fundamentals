import re
def login(database, username, password):
    if username in database:
        if database[username] == password:
            print('\nWelcome back ' + username + '\n')
            return username
        else:
            print('\nIncorrect password for ' + username + '\n')
    else:
        print('\nUser not found. Please register\n')

def register(database, username, password):
    empty_string = ""
    if username in database:
        print('\nUsername already registerd\n')
        return empty_string
    else:
        if len(username) > 10 and len(password) < 5:
            print("\nUsername and password fails validation")
            return empty_string
        elif len(username) > 10:
            print("\nUsername too long")
            return empty_string
        elif bool(re.search(r'\d', username)) == True:
            print("\nUsername contains numbers")
            return empty_string
        elif len(password) < 5:
            print("\nPassword too short")
            return empty_string
        else:
            print('\nUsername ' + username + ' registerd!\n')
            return username

def donate(username, donation_dict):
    while True:
        try:
            donation_amt = float(input('Enter amount to donate: '))
        except:
            print("incorrect value")
            continue
        else:
            if donation_amt <= 0:
                print("incorrect value")
                continue
            else:
                break

    donation = username + ' donated $' + str(donation_amt)
    donation_dict["text"].append(donation)
    donation_dict["total"] += donation_amt
    print('Thank you for your donation!\n')
    return donation_dict
   

   
