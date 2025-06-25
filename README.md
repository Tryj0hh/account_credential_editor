A Python-based application that connects to a MySQL database allowing users to:
1. Create an account
2. Login to an account
3. Change account username
4. Change account password

Features:
1. Password hashing and salting using 'bcrypt'
2. MySQL database integration using 'mysql-connector-python'
3. Username availability checker
4. Input validation and error handling

Technologies:
1. Python 3
2. MySQL
3. 'bcrypt' - password hashing and salting
4. 'mysql-connector-python' - database connection

In order to connect to the database correctly, create a folder titled 'vars'. Inside this folder,
create a .env file and fill in the following lines:

```DB_HOST=<---> DB_USER=<---> DB_PASSWORD=<---> DB_NAME=<--->```


File structure: 

├──src 

│ ├──__init__.py 

│ ├──auth.py 

│ ├──cli.py 

│ ├──database.py 

│ ├──utilities.py 

├──vars

│ ├──.env

├──.gitignore 

├──main.py 

├──README.md 

├──requirements.txt
