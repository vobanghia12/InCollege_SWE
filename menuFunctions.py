# import accounts
import accountFunctions


from accountFunctions import ALL_STUDENT_ACCOUNTS
# initialize dictionary for posted jobs
POSTED_JOBS = {}

# Allow for a max of 10 student accounts
MAX_STUDENT_ACCOUNTS = 10

# Ensure ALL_STUDENT_ACCOUNTS can handle the friends list for each student
for student in ALL_STUDENT_ACCOUNTS:
    ALL_STUDENT_ACCOUNTS[student]["friends"] = []
    ALL_STUDENT_ACCOUNTS[student]["friendRequests"] = []

    
    
# Main menu function
def main_menu(firstName, lastName):
    global fName, lName, current_logged_in_username
    fName, lName = firstName, lastName

    print("\nMain Menu:")
    print("1. Search for a job")
    print("2. Find someone you know")
    print("3. Learn a new skill")
    print("4. Useful Links")
    print("5. InCollege Important Links")
    print("6. Manage Friend Requests")
    print("7. Show My Network")
    print("8. Sign out")
    
    matched_users = [key for key, value in ALL_STUDENT_ACCOUNTS.items() if value['firstName'] == fName and value['lastName'] == lName]
    current_logged_in_username = matched_users[0] if matched_users else None


    optionChoice = input("Select a option: ")

    if optionChoice == '1':
        job_search()
    elif optionChoice == '2':
        find()
    elif optionChoice == '3':
        learning_sew_skill()
    elif optionChoice == '4':
        useful_links_menu()
    elif optionChoice == '5':
        important_links_menu()
    elif optionChoice == '6':
        manage_friend_requests()
    elif optionChoice == '7':
        show_my_network()
    elif optionChoice == '8':
        return 'toMain'
    else:
        print("Invalid input")
        main_menu(fName, lName)

def useful_links_menu():
    print("\nUseful Links:")
    print("1. General")
    print("2. Browse InCollege")
    print("3. Business Solutions")
    print("4. Directories")
    print("5. Return to Main Menu")

    choice = input("Select an option: ")
    
    if choice == "1":
        general_menu()
    elif choice in ["2", "3", "4"]:
        print("Under construction")
        useful_links_menu()
    elif choice == "5":
        main_menu(fName, lName)
    else:
        print("Invalid choice.")
        useful_links_menu()


def general_menu():
    print("\nGeneral:")
    print("1. Help Center")
    print("2. About")
    print("3. Press")
    print("4. Blog")
    print("5. Careers")
    print("6. Developers")
    print("7. Return to Useful Links Menu")

    choice = input("Select an option: ")

    if choice == "1":
        print("We're here to help")
        general_menu()
    elif choice == "2":
        print("In College: Welcome to In College, the world's largest college student network...")
        general_menu()
    elif choice == "3":
        print("In College Pressroom: Stay on top of the latest news, updates, and reports")
        general_menu()
    elif choice in ["4", "5", "6"]:
        print("Under construction")
        general_menu()
    elif choice == "7":
        useful_links_menu()
    else:
        print("Invalid choice.")
        general_menu()


def important_links_menu():
    print("\nInCollege Important Links:")
    print("1. Copyright Notice")
    print("2. About")
    print("3. Accessibility")
    print("4. User Agreement")
    print("5. Privacy Policy")
    print("6. Cookie Policy")
    print("7. Copyright Policy")
    print("8. Brand Policy")
    print("9. Return to Main Menu")

    choice = input("Select an option: ")

    if choice == "1":
        print("InCollege© copyright-2023")
        important_links_menu()
    elif choice == "2":
        print("InCollege aims to help students connect with each other and find jobs")
        important_links_menu()
    elif choice == "3":
        print("InCollege works to ensure easy access to all users")
        important_links_menu()
    elif choice == "4":
        print("By creating an account with InCollege, you automatically agree to our terms and services")
        important_links_menu()
    elif choice == "5":
        guest_controls()
    elif choice == "6":
        print("We use cookies to enhance our overall user experience")
        important_links_menu()
    elif choice == "7":
        print("We Reserve the right to use the InCollege© name and logo")
    elif choice == "8":
        print("Our brand policy is to ensure easy access to work opportunities to all students")
    elif choice == "9":
        main_menu(fName, lName)
    else:
        print("Invalid choice.")
        important_links_menu()


def guest_controls():
    print("\nGuest Controls:")
    print("1. Change inCollege Email setting")
    print("2. Change inCollege SMS setting")
    print("3. Change inCollege Targeted Advertising setting")
    print("4. Return to important links")

    choice = input("Enter 1-4 to choose and option: ")

    if choice == '1':
        subchoice = input("Enter 1 to turn on Email, or 2 to turn off Email: ")
        if subchoice == '1':
            for account, info in ALL_STUDENT_ACCOUNTS.items():
                if info['firstName'] == fName and info['lastName'] == lName:
                    info['Email'] = True
        elif subchoice == '2':
            for account, info in ALL_STUDENT_ACCOUNTS.items():
                if info['firstName'] == fName and info['lastName'] == lName:
                    info['Email'] = False
        else:
            print("invalid choice")
            guest_controls()
    elif choice == '2':
        subchoice = input("Enter 1 to turn on SMS, or 2 to turn off SMS: ")
        if subchoice == '1':
            for account, info in ALL_STUDENT_ACCOUNTS.items():
                if info['firstName'] == fName and info['lastName'] == lName:
                    info['SMS'] = True
        elif subchoice == '2':
            for account, info in ALL_STUDENT_ACCOUNTS.items():
                if info['firstName'] == fName and info['lastName'] == lName:
                    info['SMS'] = False
        else:
            print("invalid choice")
            guest_controls()
    elif choice == '3':
        subchoice = input("Enter 1 to turn on Targeted Advertising, or 2 to turn off Targeted Advertising: ")
        if subchoice == '1':
            for account, info in ALL_STUDENT_ACCOUNTS.items():
                if info['firstName'] == fName and info['lastName'] == lName:
                    info['Advertising'] = True
        elif subchoice == '2':
            for account, info in ALL_STUDENT_ACCOUNTS.items():
                if info['firstName'] == fName and info['lastName'] == lName:
                    info['Advertising'] = False
        else:
            print("invalid choice")
            guest_controls()
    else:
        print("Invalid Choice")
        guest_controls()


# Job search/Internship Option
def job_search():
    # options for user
    print("1. Post a job")
    print("2. Return to main menu")
    jobChoice = input("Select an option with: '1', or '2': ")

    # option to post a job
    if jobChoice == '1':
        if len(POSTED_JOBS) >= 5:
            print("Sorry, the limit of posted jobs has been reached")
            main_menu(fName, lName)
        else:
            title = input("Enter the title of the job: ")
            description = input("Enter the description of the job: ")
            employer = input("Enter the name of the employer: ")
            location = input("Enter the location of the job: ")
            salary = input("Enter the salary of the job: ")

            # key is first and last name of signed in user
            POSTED_JOBS[fName, lName] = {
                'title': title,
                'description': description,
                'employer': employer,
                'location': location,
                'salary': salary
            }
            print("Job has been posted!")
            main_menu(fName, lName)
    elif jobChoice == '2':
        main_menu(fName, lName)
        return
    else:
        print("Invalid input")
        job_search()


# Find someone you know option
def find():
    print("1. Search by last name")
    print("2. Search by university")
    print("3. Search by major")
    print("4. Return to main menu")

    choice = input("Select an option: ")

    if choice == "1":
        search("lastName")
    elif choice == "2":
        search("university")
    elif choice == "3":
        search("major")
    elif choice == "4":
        main_menu(fName, lName)
    else:
        print("Invalid choice.")
        find()
        
def search(key):
    value = input(f"Enter {key}: ")
    found = False
    for student, info in ALL_STUDENT_ACCOUNTS.items():
        if info[key] == value:
            found = True
            print(f"Found: {info['firstName']} {info['lastName']}")
           
            send_request = input("Send request to connect? (yes/no): ")
            if send_request.lower() == "yes":
                print(f"Connection request sent to {info['firstName']} {info['lastName']}")
                ALL_STUDENT_ACCOUNTS[student]["friendRequests"].append(current_logged_in_username)
    if not found:
        print("No student found.")
    find()


# Learn a new skill option
def learning_sew_skill():
    print("1. Python")
    print("2. Java")
    print("3. C++")
    print("4. C#")
    print("5. SQL")
    print("6. Return to main menu")

    # User choose an option
    userChoice = input("Select an option with '1', '2', '3', '4', '5', or '6': ")

    # Option menu:
    if userChoice == '1':
        print("Under construction")
        learning_sew_skill()
    elif userChoice == '2':
        print("Under construction")
        learning_sew_skill()
    elif userChoice == '3':
        print("Under construction")
        learning_sew_skill()
    elif userChoice == '4':
        print("Under construction")
        learning_sew_skill()
    elif userChoice == '5':
        print("Under construction")
        learning_sew_skill()
    elif userChoice == '6':
        main_menu(fName, lName)
        return
    else:
        print("Invalid input")
        learning_sew_skill()
        
def manage_friend_requests():
    global current_logged_in_username
    if current_logged_in_username not in ALL_STUDENT_ACCOUNTS:
        print("Error retrieving friend requests.")
        return
    
    requests = ALL_STUDENT_ACCOUNTS[current_logged_in_username].get('friendRequests', [])

    
    if not requests:
        print("You have no pending friend requests.")
        return
    
    print("Pending Friend Requests:")
    for idx, req in enumerate(requests, 1):
        print(f"{idx}. {req}")
    
    choice = input("Enter the number of the request you'd like to manage or 0 to go back: ")
    if choice == "0":
        return

    if 0 < int(choice) <= len(requests):
        selected_request = requests[int(choice) - 1]
        decision = input(f"Do you want to accept {selected_request}'s friend request? (yes/no): ")
        if decision.lower() == "yes":
            ALL_STUDENT_ACCOUNTS[current_logged_in_username]["friends"].append(selected_request)
            ALL_STUDENT_ACCOUNTS[selected_request]["friends"].append(username)
        ALL_STUDENT_ACCOUNTS[username]["friendRequests"].remove(selected_request)
        if decision.lower() == "yes":
            print(f"You are now connected with {selected_request}.")
        else:
            print(f"You have declined {selected_request}'s friend request.")
    else:
        print("Invalid selection.")
        manage_friend_requests()


def show_my_network():
    if current_logged_in_username not in ALL_STUDENT_ACCOUNTS:
        print("Error retrieving your network.")
        return

    friends = ALL_STUDENT_ACCOUNTS[current_logged_in_username].get('friends', [])

    if not friends:
        print("You have no connections in your network.")
        return

    print("\nYour Network:")
    for idx, friend in enumerate(friends, 1):
        friend_info = ALL_STUDENT_ACCOUNTS[friend]
        print(f"{idx}. {friend_info['firstName']} {friend_info['lastName']} ({friend})")

    while True:
        choice = input("\nEnter the number of the friend you'd like to disconnect from or 0 to go back: ")

        try:
            choice = int(choice)
            if choice == 0:
                return

            if 0 < choice <= len(friends):
                selected_friend = friends[choice - 1]
                decision = input(f"Do you really want to disconnect from {ALL_STUDENT_ACCOUNTS[selected_friend]['firstName']} {ALL_STUDENT_ACCOUNTS[selected_friend]['lastName']} ({selected_friend})? (yes/no): ")

                if decision.lower() == "yes":
                    ALL_STUDENT_ACCOUNTS[current_logged_in_username]["friends"].remove(selected_friend)
                    ALL_STUDENT_ACCOUNTS[selected_friend]["friends"].remove(current_logged_in_username)
                    print(f"You are now disconnected from {ALL_STUDENT_ACCOUNTS[selected_friend]['firstName']} {ALL_STUDENT_ACCOUNTS[selected_friend]['lastName']}.")
                    # Refresh the list after disconnection
                    show_my_network()
                    break
                else:
                    print("No changes were made.")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Please enter a valid number.")
