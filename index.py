from src.service import Service

def lambda_handler():
  service = Service()  
  
  return service.run()
 
# lambda_handler()