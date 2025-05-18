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

Project Structure:
account_credential_editor
├── backend/
│   ├── auth.py          Handles account creation, login, update functions
│   ├── database.py      Handles DB connection logic
│   └── utils.py         Helper function (not yet implemented)
├── frontend/
│   ├── cli.py           Command line intergace
│   └── web_app.py       Future web interface with Flask/FastAPI (not yet implemented)
├── .env                 DB credentials
├── requirements.txt
└── main.py
