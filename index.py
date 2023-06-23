from src.service import Service

def lambda_handler(event, context):
  service = Service()
  
  print("Test function........")
  
  return service.run()
 
# lambda_handler("", "")