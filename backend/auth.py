import bcrypt
from backend.database import connect_to_db

mydb = connect_to_db()
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