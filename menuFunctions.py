# import accounts

from accountFunctions import ALL_STUDENT_ACCOUNTS, acceptFriendRequest, rejectFriendRequest, disconnectFromFriend

# initialize dictionary for posted jobs
POSTED_JOBS = {}

# Allow for a max of 10 student accounts
MAX_STUDENT_ACCOUNTS = 10

# Ensure ALL_STUDENT_ACCOUNTS can handle the friends list for each student
for student in ALL_STUDENT_ACCOUNTS:
    ALL_STUDENT_ACCOUNTS[student]["friends"] = []
    
    
# Main menu function
def main_menu(firstName, lastName):
    global fName, lName
    fName, lName = firstName, lastName

    print("\nMain Menu:")
    print("1. Search for a job")
    print("2. Find someone you know")
    print("3. Learn a new skill")
    print("4. Useful Links")
    print("5. InCollege Important Links")
    print("6. Manage Friend Requests")
    print("7. Manage Network")
    print("8. Sign out")

    optionChoice = input("Select an option: ")

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
        manage_network()
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

# Function to manage friend requests
def manage_friend_requests():
    print("\nManage Friend Requests:")
    print("1. Display Pending Friend Requests")
    print("2. Accept a Friend Request")
    print("3. Reject a Friend Request")
    print("4. Return to Main Menu")

    choice = input("Select an option: ")

    if choice == "1":
        displayPendingRequests(fName)  # Display pending friend requests for the logged-in user
    elif choice == "2":
        acceptFriendRequest()
    elif choice == "3":
        rejectFriendRequest()
    elif choice == "4":
        main_menu(fName, lName)
    else:
        print("Invalid choice.")
        manage_friend_requests()

# Function to manage the user's network
def manage_network():
    print("\nManage Network:")
    print("1. Display Your Network")
    print("2. Disconnect from a Friend")
    print("3. Return to Main Menu")

    choice = input("Select an option: ")

    if choice == "1":
        displayNetwork(fName)  # Display the user's network
    elif choice == "2":
        disconnectFromFriend()
    elif choice == "3":
        main_menu(fName, lName)
    else:
        print("Invalid choice.")
        manage_network()


# Function to display pending friend requests
def displayPendingRequests(username):
    if username in accountFunctions.PENDING_REQUESTS:
        print("\nPending Friend Requests:")
        for requester in accountFunctions.PENDING_REQUESTS[username]:
            print(f"- {ALL_STUDENT_ACCOUNTS[requester]['firstName']} {ALL_STUDENT_ACCOUNTS[requester]['lastName']}")
    else:
        print("\nNo pending friend requests.")

# Function to display the user's network
def displayNetwork(username):
    friends = ALL_STUDENT_ACCOUNTS[username]['friends']
    if friends:
        print("\nYour Network:")
        for friend_username in friends:
            print(f"- {ALL_STUDENT_ACCOUNTS[friend_username]['firstName']} {ALL_STUDENT_ACCOUNTS[friend_username]['lastName']}")
    else:
        print("\nYour network is empty.")