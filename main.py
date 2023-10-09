import accountFunctions
import menuFunctions
import sys

from accountFunctions import acceptFriendRequest, rejectFriendRequest, disconnectFromFriend


# Starting boolean assuming when you first use it nobody is logged in
isLoggedIn = False
global fName, lName, connections
connections = []


def login_function():
    global isLoggedIn
    username = input("Enter username: ")
    password = input("Enter password: ")
    if accountFunctions.checkUser(username, password):
        fName = accountFunctions.ALL_STUDENT_ACCOUNTS[username]['firstName']
        lName = accountFunctions.ALL_STUDENT_ACCOUNTS[username]['lastName']
        isLoggedIn = True
        print("You have successfully logged in.\n")
        return menuFunctions.main_menu(fName, lName)
    else:
        x = input("Incorrect username/password. Input 1 to try again, or input 2 to return to menu.\n")
        if x == '1':
            login_function()
        elif x == '2':
            main()


def create_account():
    if len(accountFunctions.ALL_STUDENT_ACCOUNTS) >= 10:
        print("Sorry, all permitted accounts have been created. Please come back later.")
    else:
        fName, lName = accountFunctions.createAccount()
        return menuFunctions.main_menu(fName, lName)


def search_for_user():
    print("Searching For InCollege User")
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    if accountFunctions.checkForName(firstName, lastName) == True:
        print("They are a part of the InCollege system.")
    else:
        print("They are not yet a part of the InCollege system yet.")
        
def search_for_user_by_criteria():
    print("Search For InCollege User By Criteria")
    criteria = input("Search by (lastName/university/major): ")

    results = []

    if criteria == "lastName":
        lastName = input("Enter last name: ")
        results = accountFunctions.searchByCriteria('lastName', lastName)
    elif criteria == "university":
        university = input("Enter university: ")
        results = accountFunctions.searchByCriteria('university', university)
    elif criteria == "major":
        major = input("Enter major: ")
        results = accountFunctions.searchByCriteria('major', major)
    else:
        print("Invalid criteria selected.")
        return

    if not results:
        print("No matches found.")
        return

    for idx, user in enumerate(results, 1):
        print(f"{idx}. {user['firstName']} {user['lastName']}")
    
    # Send a connection request
    connect_idx = int(input("Enter the number of the student you'd like to connect with or 0 to return: "))
    if connect_idx == 0:
        return
    if 0 < connect_idx <= len(results):
        selected_user = results[connect_idx - 1]
        accountFunctions.sendConnectionRequest(fName, selected_user['username'])
    else:
        print("Invalid selection.")
        return

        
def return_to_useful_links():
    choice = input("Do you want to go back to the useful links page?: y/n")
    if choice == "y":
        return True
    else:
        return False
    
def return_to_important_links():
    choice = input("Do you want to go back to the important links page?: y/n")
    if choice == "y":
        return True
    else:
        return False
    
def quit():
    sys.exit("Goodbye !")



def display_useful_links():
    print("\nUseful Links:")
    print("1. General")
    print("2. Browse InCollege")
    print("3. Business Solutions")
    print("4. Directories")
    print("5. Return to Main Menu")

    choice = input("Select an option: ")

    if choice == "1":
        print("\nGeneral:")
        print("1. Help Center")
        print("2. About")
        print("3. Press")
        print("4. Blog")
        print("5. Careers")
        print("6. Developers")
        print("7. Return to Useful Links Menu")

        choice = input("Select a option: ")

        if choice == "1":
            print("We're here to help")
            choice = return_to_useful_links()
            if choice == True:
                display_useful_links()
            else:
                quit()
        elif choice == "2":
            print("In College: Welcome to In College, the world's largest college student network...")
            choice = return_to_useful_links()
            if choice == True:
                display_useful_links()
            else:
                quit()
        elif choice == "3":
            print("In College Pressroom: Stay on top of the latest news, updates, and reports")
            choice = return_to_useful_links()
            if choice == True:
                display_useful_links()
            else:
                quit()
        elif choice in ["4", "5", "6"]:
            print("Under construction")
            choice = return_to_useful_links()
            if choice == True:
                display_useful_links()
            else:
                quit()
        elif choice == "7":
            choice = return_to_useful_links()
            if choice == True:
                display_useful_links()
            else:
                quit()
        else:
            print("Invalid choice.")
            display_useful_links()
    elif choice in ["2", "3", "4"]:
        print("Under construction")
        display_useful_links()
    elif choice == "5":
        main()
    else:
        print("Invalid choice.")
        main()


def display_important_links():
    print("\nInCollege Important Links:")
    print("1. Copyright Notice")
    print("2. About")
    print("3. Accessibility")
    print("4. User Agreement")
    print("5. Cookie Policy")
    print("6. Copyright Policy")
    print("7. Brand Policy")
    print("8. Return to login screen")

    choice = input("Select an option: ")

    if choice == "1":
        print("InCollege© copyright-2023")
        choice == return_to_important_links()
        if choice == True:
            display_important_links()
        else:
            quit()
    elif choice == "2":
        print("InCollege aims to help students connect with each other and find jobs")
        if choice == True:
            display_important_links()
        else:
            quit()
    elif choice == "3":
        print("InCollege works to ensure easy access to all users")
        if choice == True:
            display_important_links()
        else:
            quit()
    elif choice == "4":
        print("By creating an account with InCollege, you automatically agree to our terms and services")
        if choice == True:
            display_important_links()
        else:
            quit()
    elif choice == "5":
        print("We use cookies to enhance our overall user experience")
        if choice == True:
            display_important_links()
        else:
            quit()
    elif choice == "6":
        print("We Reserve the right to use the InCollege© name and logo")
        if choice == True:
            display_important_links()
        else:
            quit()
    elif choice == "7":
        print("Our brand policy is to ensure easy access to work opportunities to all students")
        if choice == True:
            display_important_links()
        else:
            quit()
    elif choice == "8":
        main()
    else:
        print("Invalid choice.")
        display_important_links()

def main():
    global isLoggedIn
    #global fName, lName

    while True:
        # Initial screen
        print("\nWelcome to InCollege!\n")

        # User not logged in
        if not isLoggedIn:
            print("InCollege Student Success Story:")
            print("Billy used InCollege to network and obtain opportunities that resulted with him landing a job as a "
                  "software engineer!")
            print("\n=================================")
            print("1. Useful Links")
            print("2. InCollege Important Links")
            print("3. Login")
            print("4. Create a new account")
            print("5. Watch a video about InCollege")
            print("6. Search for an InCollege User")

            userChoice = input("Select an option with numbers 1-6: ")

            if userChoice == '1':
                display_useful_links()
            elif userChoice == '2':
                display_important_links()
            elif userChoice == '3':
                login_function()
            elif userChoice == '4':
                create_account()
            elif userChoice == '5':
                print("\nVideo is now playing")
            elif userChoice == '6':
                search_for_user_by_criteria()
                main()
            else:
                print("Invalid choice. Please choose a number between 1-6.")
                main()
        # User is logged in
        else:
            return menuFunctions.main_menu(fName, lName)
        
if __name__ == '__main__':
    # Call main and check if returned to
    main()
    if main() == 'toMain':
        main()
        
