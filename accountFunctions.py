# Dictionary with key as username and value as a dictionary containing password, firstName, and lastName
ALL_STUDENT_ACCOUNTS = {}

# Constants
MAX_STUDENT_ACCOUNTS = 10

# Function for creating an account
def createAccount():
    if len(ALL_STUDENT_ACCOUNTS) >= MAX_STUDENT_ACCOUNTS:
        print("Sorry, the maximum number of accounts have been reached!")
        return

    username = input("Enter a unique username: ")
    if checkUniqueUsername(username):
        print("Username is already claimed. Please choose another one.\n")
        return

    password = input("Enter a secure password: ")
    if not checkValidPassword(password):
        print("Invalid password. Password must be 8-12 characters long, contain at least one capital letter, one digit, and one special character.\n")
        return

    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    university = input("Enter your university: ")
    major = input("Enter your major: ")

    ALL_STUDENT_ACCOUNTS[username] = {
        'password': password,
        'firstName': firstName,
        'lastName': lastName,
        'lastName': lastName,
        'university': university,
        'major': major,
        'friends': [],
        'Language': 'English',
        'SMS': True,
        'Email': True,
        'Advertising': True

    }
    print("Your Account has been created!\n")
    return firstName, lastName

# Function checks if user is in the dictionary and checks corresponding password, returns true if found
def checkUser(username, password):
    if username in ALL_STUDENT_ACCOUNTS and ALL_STUDENT_ACCOUNTS[username]['password'] == password:
        return True
    else:
        return False

# Function checks if username is unique in the dictionary
def checkUniqueUsername(username):
    if username in ALL_STUDENT_ACCOUNTS:
        return True
    else:
        return False

# Checks if inputted password during creation is within our requirements
def checkValidPassword(password):
    if 8 <= len(password) <= 12:
        checkDigit = False
        checkSpecialCharacter = False
        checkUpperCase = False

        # Check if it has the password requirements
        for x in password:
            if x.isdigit():
                checkDigit = True
            elif x in "!@#$%^&*()_+[]:;<>,.?~":
                checkSpecialCharacter = True
            elif x.isupper():
                checkUpperCase = True

        # If all correct then it should return as 'true', if one of them is wrong the and statements turn false
        return checkUpperCase and checkDigit and checkSpecialCharacter
    else:
        return False


# Function to check InCollege membership by first name and last name *epic 2
def checkForName(firstName, lastName):
    for account, info in ALL_STUDENT_ACCOUNTS.items():
        if info['firstName'] == firstName and info['lastName'] == lastName:
            return True
        else:
            return False


# New dictionary to store pending friend requests
PENDING_REQUESTS = {}

# Function to send a connection request
def sendConnectionRequest(username, friend_username):
    if friend_username in ALL_STUDENT_ACCOUNTS and friend_username not in ALL_STUDENT_ACCOUNTS[username]['friends']:
        # Check if a pending request already exists
        if username not in PENDING_REQUESTS:
            PENDING_REQUESTS[friend_username] = []

        # Send the request and add it to the recipient's pending requests
        PENDING_REQUESTS[friend_username].append(username)

        print(f"Friend request sent to {ALL_STUDENT_ACCOUNTS[friend_username]['firstName']} {ALL_STUDENT_ACCOUNTS[friend_username]['lastName']}!")
    else:
        print("User not found or already connected.")

# Function to accept a friend request
def acceptFriendRequest(username, friend_username):
    if username in PENDING_REQUESTS.get(friend_username, []):
        ALL_STUDENT_ACCOUNTS[username]['friends'].append(friend_username)
        ALL_STUDENT_ACCOUNTS[friend_username]['friends'].append(username)
        PENDING_REQUESTS[friend_username].remove(username)
        print(f"You are now connected with {ALL_STUDENT_ACCOUNTS[friend_username]['firstName']} {ALL_STUDENT_ACCOUNTS[friend_username]['lastName']}!")
    else:
        print("Friend request not found.")

# Function to reject a friend request
def rejectFriendRequest(username, friend_username):
    if username in PENDING_REQUESTS.get(friend_username, []):
        PENDING_REQUESTS[friend_username].remove(username)
        print(f"Friend request from {ALL_STUDENT_ACCOUNTS[friend_username]['firstName']} {ALL_STUDENT_ACCOUNTS[friend_username]['lastName']} has been rejected.")
    else:
        print("Friend request not found.")

# Function to disconnect from a friend
def disconnectFromFriend(username, friend_username):
    if friend_username in ALL_STUDENT_ACCOUNTS[username]['friends']:
        ALL_STUDENT_ACCOUNTS[username]['friends'].remove(friend_username)
        ALL_STUDENT_ACCOUNTS[friend_username]['friends'].remove(username)
        print(f"You have disconnected from {ALL_STUDENT_ACCOUNTS[friend_username]['firstName']} {ALL_STUDENT_ACCOUNTS[friend_username]['lastName']}.")
    else:
        print("Friend not found in your list.")

