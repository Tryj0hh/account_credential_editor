from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv(dotenv_path="vars/.env")

def connect_to_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
)