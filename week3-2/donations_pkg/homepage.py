def show_homepage():
    print('         === DonateMe Homepage ===           \n-----------------------------------------\n| 1.   Login     | 2.    Register        |\n-----------------------------------------\n| 3.   Donate    | 4.    Show Donations  |\n-----------------------------------------\n|             5. Exit                    |\n-----------------------------------------\n')

def show_donations(donations):
    print("\n---All Donations---\n")
    if len(donations) == 0:
        print("Currently, there are no donations.")
    else:
        for i in donations["text"]:
            print(i)
    print("Total = $" + str(donations["total"]))
    print()
