from src.service import Service

def lambda_handler(event, context):
  service = Service()  
  
  return service.run()
 
# lambda_handler("", "")