import sys
import logging
import os
from datetime import datetime

def get_error_message(error, error_details:sys):
    _,_,exc_tb = error_details.exc_info()
      
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name = exc_tb.tb_frame.f_code.co_filename,
        line_number = exc_tb.tb_lineno,
        error_message = str(error)      
    )
         

    # Configure logging to log the error message to a file
    logging.basicConfig(
        filename='error.log',  # Log file name
        format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
        level=logging.ERROR  # Log level
    )
    
    # Log the error message
    logging.error(error_message)
       
    return error_message
 
 
 
 
class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)   
        self.error_message = get_error_message(error_message, error_details=error_details) 
        
    def __str__(self) -> str:
        return self.error_message
    
    
    
# if __name__ == "__main__":    
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info("Divide by zero")
#         raise CustomException(e, sys)
        