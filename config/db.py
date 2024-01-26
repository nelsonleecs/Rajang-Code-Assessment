#For creating connection to the database
from pymongo import MongoClient

dbConnection = MongoClient("mongodb://localhost:27017")
db = dbConnection.Company
employeeCollection = db["Employee"]
logCollection = db["DBLogs"]