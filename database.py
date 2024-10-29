from pymongo import MongoClient

host = "ocdb.app"
port = 5050
database = "db_42vjh6bg4" # your database
username = "user_42vjh6bg4" # your username
password = "p42vjh6bg4" # your password

connection_str = f"mongodb://{username}:{password}@{host}:{port}/{database}"

my_client = MongoClient(connection_str)
my_db = my_client[database]
results = my_db["results"]

def insert_data(raw):
    results.insert_one(raw)
    return "Data Inserted :)"

def delete_data(raw):
    results.delete_one(raw)
    return "Data Deleted :("