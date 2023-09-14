from pymongo import MongoClient

db_client = MongoClient().local#Without specification it connects local.
""" DB in production set up
db_client = MongoClient(*insert here url to connect to database including info regarding
user password*).*dbremota*
"""