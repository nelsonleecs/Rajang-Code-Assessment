# A simple REST API for MongoDB and FastAPI
Some python scripts to act as api provider using FastAPI for operating CRUD functions on a Company database containing Employee and Log collections, running on MongoDB.

## Requisites
- Python 3.11
- MongoDB database
- Python packages: 
  - PyMongo 4.6.1 
  - FastAPI 0.109.0 
  - Uvicorn 0.27.0

## Instructions to Run
1. Run the python virtual environment from ``venv`` folder:
   ```
   # For linux and mac
   $ source venv/bin/activate

   # For Windows
   > venv/bin/activate

   ```
2. Run the mongoDB database.
    - The API will connect to ``mongodb://localhost:27017``.
    -  If the database isn't running on localhost or different port number, adjust accordingly in ``db.py`` under ``config`` folder.
3. Run ``uvicorn`` using the following command:
   ```
   uvicorn server:app --reload
   ``` 
   - If the ``uvicorn`` command isn't recognised, try install the packages from ``requirements.txt``:
      ```
      pip install -r requirements.txt
      ```
4. The API will be running. You may interact it with Swagger UI in any browser through ``http://localhost:8000/docs#`` or other API application such as Postman.
    - The ``uvicorn`` will be running on port ``8000``. If it's in another port number, adjust the address accordingly.

## MongoDB Schema
``` 
Company
  * Employee
    - _id: ObjectID
    - fullName: String
    - dateOfBirth: DateTime
    - dateJoined: DateTime
    - dateLeft: DateTime, optional
    - nric: String, 12 numeric characters, unique
    - department: String, enumerated: 
      (“admin”|”engineering”|”management”|”sales”|”qc”)
    - salary: Float
    - remark: String

  * DBLogs
    - _id: ObjectID
    - operation: String
    - timestamp: DateTime
    - ipAddress: String
    - document: String
```

## API Documentation

### 1. Create Employee

For creating a new employee entry under ``Employee`` collection. This action will be logged.
- **HTTP Method**: POST 
- **URL**: .../
- **Payload**:
    - Request body in ``JSON`` format: 
      ```
      {
      "fullName": "string",
      "dateOfBirth": "2024-01-26",
      "dateJoined": "2024-01-26",
      "dateLeft": "2024-01-26",
      "nric": "397779111567",
      "department": "admin",
      "salary": 0,
      "remark": "string"
      }
      ```
- **Expected Result**:
  
  Return HTTP code 200 and following body: 
  ```
  {
  "status": "OK",
  "data": {
    "_id": ObjectID,
    "fullName": "string",
    "dateOfBirth": "2024-01-26",
    "dateJoined": "2024-01-26",
    "dateLeft": "2024-01-26",
    "nric": "397779111567",
    "department": "admin",
    "salary": 0,
    "remark": "string"
    }
  }
  ```

### 2. Read All Employee

To view all employee data entries under ``Employee`` collection.
- **HTTP Method**: GET 
- **URL**: .../
- **Payload**: None
- **Expected Result**:
  
  Return HTTP code 200 and following body: 
  ```
  {
  "status": "OK",
  "data": [
      {
      "_id": ObjectID,
      "fullName": "string",
      "dateOfBirth": "2024-01-26",
      "dateJoined": "2024-01-26",
      "dateLeft": "2024-01-26",
      "nric": "397779111567",
      "department": "admin",
      "salary": 0,
      "remark": "string"
      }
      ...
    ]
  }
  ```

### 3. Read One Employee

To view one of the employee data entries under ``Employee`` collection.
- **HTTP Method**: GET 
- **URL**: .../{id}
- **Payload**:
  - Parameter: 
    - ObjectID - String
- **Expected Result**:
  
  Return HTTP code 200 and following body: 
  ```
  {
  "status": "OK",
  "data": {
    "_id": ObjectID,
    "fullName": "string",
    "dateOfBirth": "2024-01-26",
    "dateJoined": "2024-01-26",
    "dateLeft": "2024-01-26",
    "nric": "397779111567",
    "department": "admin",
    "salary": 0,
    "remark": "string"
    }
  }
  ```

### 4. Update Employee

To update one of the employee data entries under ``Employee`` collection. This action will be logged.
- **HTTP Method**: PUT 
- **URL**: .../{id}
- **Payload**:
  - Parameter: 
    - ObjectID - String
  - Request body in ``JSON`` format: 
      ```
      {
      "fullName": "string",
      "dateOfBirth": "2024-01-26",
      "dateJoined": "2024-01-26",
      "dateLeft": "2024-01-26",
      "nric": "397779111567",
      "department": "admin",
      "salary": 0,
      "remark": "string"
      }
      ```
- **Expected Result**:
  
  Return HTTP code 200 and following body: 
  ```
  {
  "status": "OK",
  "data": {
    "_id": ObjectID,
    "fullName": "string",
    "dateOfBirth": "2024-01-26",
    "dateJoined": "2024-01-26",
    "dateLeft": "2024-01-26",
    "nric": "397779111567",
    "department": "admin",
    "salary": 0,
    "remark": "string"
    }
  }
  ```

### 4. Update Employee

To update one of the employee data entries under ``Employee`` collection. This action will be logged.
- **HTTP Method**: PUT 
- **URL**: .../{id}
- **Payload**:
  - Parameter: 
    - ObjectID - String
  - Request body in ``JSON`` format: 
      ```
      {
      "fullName": "string",
      "dateOfBirth": "2024-01-26",
      "dateJoined": "2024-01-26",
      "dateLeft": "2024-01-26",
      "nric": "397779111567",
      "department": "admin",
      "salary": 0,
      "remark": "string"
      }
      ```
- **Expected Result**:
  
  Return HTTP code 200 and following body: 
  ```
  {
  "status": "OK",
  "data": {
    "_id": ObjectID,
    "fullName": "string",
    "dateOfBirth": "2024-01-26",
    "dateJoined": "2024-01-26",
    "dateLeft": "2024-01-26",
    "nric": "397779111567",
    "department": "admin",
    "salary": 0,
    "remark": "string"
    }
  }
  ```