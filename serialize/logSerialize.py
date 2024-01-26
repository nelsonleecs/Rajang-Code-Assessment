#Serialize one log
def logSerializer(log) -> dict:
  return {
    '_id':str(log["_id"]),
    'operation': log["operation"],
    'timestamp': log["timestamp"],
    'ipAddress': log["ipAddress"],
    'document': log["document"]
  }

#Serialize multiple logs
def logsSerializer(logs) -> list:
  if logs:
    return [logSerializer(log) for log in logs]