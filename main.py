'''Create a login page using MySQL that allows the user to create an account, login, edit account details and view account information'''

#import needed packages
from dotenv import load_dotenv
import os
import mysql.connector
import bcrypt

#connect to MySQL server
mydb = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

#print a welcome screen for the user
print('Welcome to account settings! Please select an option below.')
print('1. Create an account.')
print('2. Login to your account.')
print('3. Change your username.')
print('4. Change your password.')
print('5. Quit')

#allow user to select an option
while True:
    try:
        user_selection = int(input())
        break
    except:
        print('Please select one of the available options')

#set database cursor
cursor = mydb.cursor()

def account_creation():
    while True:
        username_select = input('Choose a username: ')
        result = username_finder(username_select)

        if result:
            print('This username is taken')
        else:
            break

    user_password = input("Choose a password: ").encode('utf-8')
    #hash and salt password
    salt = bcrypt.gensalt()
    hashedpassword = bcrypt.hashpw(user_password, salt)
    sql = "insert into credentials (username, password) values (%s, %s)"
    cursor.execute(sql, (username_select, hashedpassword))
    mydb.commit()
    print('account created')

#create username search function
def username_finder(username):
    cursor.execute("Select username from credentials where username = %s", (username,))
    result = cursor.fetchone()
    return result

#create function that allows user to create an account
def account_login():
    while True:
        username = input('Enter your username: ')
        result = username_finder(username)

        if result:
            entered_password = input('Enter your password: ').encode('utf-8')
            cursor.execute("Select password from credentials where username = %s", (username,))
            password_result = cursor.fetchone()

            if bcrypt.checkpw(entered_password, password_result[0].encode('utf-8') if isinstance(password_result[0], str) else password_result[0]):
                print("Login successful")
                return username
            else:
                print('Incorrect password')
        else:
            print('This account does not exist')

#create function that allows user to change username
def change_username():
    print('Login to change your username')
    current_username = account_login()

    while True:
        new_username = input('Enter a new username: ')
        if username_finder(new_username):
            print('This username is taken. Try another.')
        else:
            cursor.execute('update credentials set username = %s where username = %s', (new_username, current_username))
            mydb.commit()
            print('Your username has been updated.')
            break

def change_password():
    print('Login to change your password')
    current_username = account_login()

    new_password = input("Choose a new password: ").encode('utf-8')

    #hash and salt password
    salt = bcrypt.gensalt()
    new_hashed_password = bcrypt.hashpw(new_password, salt)

    sql = "update credentials set password = %s where username = %s"
    cursor.execute(sql, (new_hashed_password, current_username))
    mydb.commit()
    print('Password Updated.')



#allow user to create an account
if user_selection == 1:
    account_creation()

#allow user to login to an account
elif user_selection == 2:
    account_login()
 
#allow user to change username as long as username is not taken
elif user_selection == 3:
    change_username()

elif user_selection == 4:
    change_password()

elif user_selection == 5:
    quit

else:
    print('Please select one of the options.')