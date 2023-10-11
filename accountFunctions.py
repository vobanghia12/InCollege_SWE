# Dictionary with key as username and value as a dictionary containing password, firstName, and lastName
ALL_STUDENT_ACCOUNTS = {}

# Constants
MAX_STUDENT_ACCOUNTS = 10

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
        'university': university,
        'major': major,
        'friends': [],
        'friendRequests': [],
        'Language': 'English',
        'SMS': True,
        'Email': True,
        'Advertising': True
    }
    print("Your Account has been created!\n")
    return firstName, lastName

def checkUser(username, password):
    return username in ALL_STUDENT_ACCOUNTS and ALL_STUDENT_ACCOUNTS[username]['password'] == password

def checkUniqueUsername(username):
    return username in ALL_STUDENT_ACCOUNTS

def checkValidPassword(password):
    if 8 <= len(password) <= 12:
        checkDigit = any(char.isdigit() for char in password)
        checkSpecialCharacter = any(char in "!@#$%^&*()_+[]:;<>,.?~" for char in password)
        checkUpperCase = any(char.isupper() for char in password)

        return checkUpperCase and checkDigit and checkSpecialCharacter
    return False

def checkForName(firstName, lastName):
    return any(info['firstName'] == firstName and info['lastName'] == lastName for _, info in ALL_STUDENT_ACCOUNTS.items())

def sendConnectionRequest(sender_username, receiver_username):
    if receiver_username not in ALL_STUDENT_ACCOUNTS[sender_username]['friends'] and receiver_username not in ALL_STUDENT_ACCOUNTS[sender_username]['friendRequests']:



        if sender_username in ALL_STUDENT_ACCOUNTS[receiver_username]['friendRequests']:
            ALL_STUDENT_ACCOUNTS[sender_username]['friends'].append(receiver_username)
            ALL_STUDENT_ACCOUNTS[receiver_username]['friends'].append(sender_username)
            ALL_STUDENT_ACCOUNTS[receiver_username]['friendRequests'].remove(sender_username)
            print(f"You are now connected with {ALL_STUDENT_ACCOUNTS[receiver_username]['firstName']} {ALL_STUDENT_ACCOUNTS[receiver_username]['lastName']}!")
        else:
            ALL_STUDENT_ACCOUNTS[receiver_username]['friendRequests'].append(sender_username)
            print(f"Connection request sent to {ALL_STUDENT_ACCOUNTS[receiver_username]['firstName']} {ALL_STUDENT_ACCOUNTS[receiver_username]['lastName']}!")
    else:
        print("User not found or already connected.")

def searchByCriteria(criteria, value):
    return [info for _, info in ALL_STUDENT_ACCOUNTS.items() if info[criteria] == value]


def pendingFriendRequests(username):
    if username in ALL_STUDENT_ACCOUNTS:
        return ALL_STUDENT_ACCOUNTS[username]['friendRequests']
    return []

def acceptFriendRequest(sender_username, receiver_username):
    if sender_username in ALL_STUDENT_ACCOUNTS[receiver_username]['friendRequests']:
        ALL_STUDENT_ACCOUNTS[receiver_username]['friends'].append(sender_username)
        ALL_STUDENT_ACCOUNTS[receiver_username]['friendRequests'].remove(sender_username)
        ALL_STUDENT_ACCOUNTS[sender_username]['friends'].append(receiver_username)

def declineFriendRequest(sender_username, receiver_username):
    if sender_username in ALL_STUDENT_ACCOUNTS[receiver_username]['friendRequests']:
        ALL_STUDENT_ACCOUNTS[receiver_username]['friendRequests'].remove(sender_username)

def disconnectFriend(sender_username, receiver_username):
    if receiver_username in ALL_STUDENT_ACCOUNTS[sender_username]['friends']:
        ALL_STUDENT_ACCOUNTS[sender_username]['friends'].remove(receiver_username)
        ALL_STUDENT_ACCOUNTS[receiver_username]['friends'].remove(sender_username)
