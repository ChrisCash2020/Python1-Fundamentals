from donations_pkg import homepage, user
database = {'admin': 'password123'}
donations = {"text" : [], "total" : 0 }
authorized_user = ""
homepage.show_homepage()

while True:
    if authorized_user == None or len(authorized_user) == 0:
        print('You must be logged in to donate')
    else:
        print('Logged in as:',authorized_user)
    user_option = int(input('Choose an option: '))
    if user_option == 1:
        user_name = input('\nEnter username: ').lower()
        pass_word = input('Enter password: ')
        authorized_user = user.login(database, user_name, pass_word)
        homepage.show_homepage()
        continue
    elif user_option == 2:
        user_name = input('\nEnter username: ')
        pass_word = input('Enter password: ')
        authorized_user = user.register(database, user_name, pass_word)
        if len(authorized_user) > 0:
            database[user_name] = pass_word
        homepage.show_homepage()
        continue
    elif user_option == 3:
        if len(authorized_user) == 0:
            print('You are not logged in')
        else:
            donations = user.donate(authorized_user, donations)
        homepage.show_homepage()
        continue
    elif user_option == 4:
        homepage.show_donations(donations)
        homepage.show_homepage()
        continue
    elif user_option == 5:
        print('\nLeaving DonateMe...')
        break
