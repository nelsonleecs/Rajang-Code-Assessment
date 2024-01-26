from datetime import date, datetime

#Serialize one employee data
def employeeSerializer(employee) -> dict:
  #For those who have date of leaving
  if employee["dateLeft"] != None:
    return {
      '_id':str(employee["_id"]),
      'fullName': employee["fullName"],
      'dateOfBirth': employee["dateOfBirth"].date(),
      'dateJoined': employee["dateJoined"].date(),
      'dateLeft': employee["dateLeft"].date(),
      'nric': employee["nric"],
      'department': employee["department"],
      'salary': employee["salary"],
      'remark': employee["remark"]
    }
  #For those who don't have date of leaving
  else :
     return {
      '_id':str(employee["_id"]),
      'fullName': employee["fullName"],
      'dateOfBirth': employee["dateOfBirth"].date(),
      'dateJoined': employee["dateJoined"].date(),
      'dateLeft': None,
      'nric': employee["nric"],
      'department': employee["department"],
      'salary': employee["salary"],
      'remark': employee["remark"]
    }

#Serialize multiple employees data
def employeesSerializer(employees) -> list:
  if employees:
    return [employeeSerializer(employee) for employee in employees]