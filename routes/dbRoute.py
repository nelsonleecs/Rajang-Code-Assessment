from fastapi import APIRouter, Request, HTTPException
from schemas.employeeSchema import Employee
from serialize.employeeSerialize import *
from serialize.logSerialize import *
from config.db import *
from bson import ObjectId
from datetime import datetime

route = APIRouter()

def logging(operation: str, ipAddress: str, document: str):
  log = {"operation": operation, "timestamp": datetime.now(), "ipAddress": ipAddress, "document": document}
  logCollection.insert_one(log)


#For creating a new employee data
@route.post("/")
async def createEmployee(employee: Employee, request: Request):
  #Check if the nric is unique
  nricCheck = employeeCollection.find_one({"nric":employee.nric})
  if nricCheck:
    raise HTTPException(status_code=400, detail="NRIC is not unique.")

  else:
    # Convert the input date into a datetime object
    dateOfBirth = datetime.combine(employee.dateOfBirth, datetime.min.time())
    dateJoined = datetime.combine(employee.dateJoined, datetime.min.time())
    
    #Insert the employee data based on dateLeft
    if employee.dateLeft:
      dateLeft = datetime.combine(employee.dateLeft, datetime.min.time())
      data = {
        "fullName": employee.fullName,
        "dateOfBirth": dateOfBirth,
        "dateJoined": dateJoined,
        "dateLeft": dateLeft,
        "nric": employee.nric,
        "department": employee.department,
        "salary": employee.salary,
        "remark": employee.remark
      }
    else:
      data = {
        "fullName": employee.fullName,
        "dateOfBirth": dateOfBirth,
        "dateJoined": dateJoined,
        "dateLeft": None,
        "nric": employee.nric,
        "department": employee.department,
        "salary": employee.salary,
        "remark": employee.remark
      }
    document = employeeCollection.insert_one(data)

    #Log the attempt
    logging("Create", str(request.client.host), str(document.inserted_id))

    #Return success message
    employee = employeeSerializer(employeeCollection.find_one({"_id": document.inserted_id}))
    return {"status": "OK", "data": employee}


#To read data of all employee
@route.get("/")
async def readAllEmployee():
  #Check if the employees exists in the database
  employees = employeesSerializer(employeeCollection.find())
  return {"status": "OK", "data": employees}


#To read data of one of the employee by _id
@route.get("/{id}")
async def readOneEmployee(id: str):
  #Check if the id exists in the database
  if employeeCollection.find_one({"_id": ObjectId(id)}):
    employee = employeeSerializer(employeeCollection.find_one({"_id": ObjectId(id)}))
    return {"status": "OK", "data": employee}
  else :
    raise HTTPException(status_code=400, detail="No such employee id in database.")


#To update one of the employees data
@route.put("/{id}")
async def updateEmployee(id: str, employee: Employee, request: Request):
    #Check if the id exists in the database
    if employeeCollection.find_one({"_id": ObjectId(id)}):
      # Convert the input date into a datetime object
      dateOfBirth = datetime.combine(employee.dateOfBirth, datetime.min.time())
      dateJoined = datetime.combine(employee.dateJoined, datetime.min.time())

      #Update the employee data based on dateLeft
      if employee.dateLeft:
        dateLeft = datetime.combine(employee.dateLeft, datetime.min.time())
        employeeCollection.find_one_and_update(
          {
            "_id": ObjectId(id)
          }, 
          {
          "$set": {
            "fullName": employee.fullName,
            "dateOfBirth": dateOfBirth,
            "dateJoined": dateJoined,
            "dateLeft": dateLeft,
            "nric": employee.nric,
            "department": employee.department,
            "salary": employee.salary,
            "remark": employee.remark
            }
          })
      else:
        employeeCollection.find_one_and_update(
          {
            "_id": ObjectId(id)
          }, 
          {
          "$set": {
            "fullName": employee.fullName,
            "dateOfBirth": dateOfBirth,
            "dateJoined": dateJoined,
            "dateLeft": None,
            "nric": employee.nric,
            "department": employee.department,
            "salary": employee.salary,
            "remark": employee.remark
            }
          })
      
      #Log the attempt
      logging("Update", str(request.client.host), str(id))

      #Return success message
      employee = employeeSerializer(employeeCollection.find_one({"_id": ObjectId(id)}))
      return {"status": "Ok","data": employee}
    
    else:
      raise HTTPException(status_code=400, detail="No such employee id in database.")
    

#To delete one of the employees data
@route.delete("/{id}")
async def deleteEmployee(id: str, request: Request):
   #Check if the id exists in the database
    if employeeCollection.find_one({"_id": ObjectId(id)}):
      employeeCollection.find_one_and_delete({"_id": ObjectId(id)})

      #Log the attempt
      logging("Delete", str(request.client.host), str(id))

      #Return success message
      return {"status": "Ok","deletedID": id}

    else:
      raise HTTPException(status_code=400, detail="No such employee id in database.")


#To read all of the logs
@route.get("/log/")
async def readAllLog():
  log = logsSerializer(logCollection.find())
  return {"status": "OK", "data": log}


#To read one of the logs
@route.get("/log/{id}")
async def readOneLog(id: str):
  log = logSerializer(logCollection.find_one({"_id": ObjectId(id)}))
  #Check if the id exists in the database
  if log:
    return {"status": "OK", "data": log}
  else:
    raise HTTPException(status_code=400, detail="No such log id in database.")