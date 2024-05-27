import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging

from src.components.data_transformation import DataTransformation, DataTransformationConfig

# Input files
@dataclass
class DataIngestionConfig:
    """
    Data class for storing config parameters
    """
    train_data_path:str = os.path.join('artifacts', 'train.csv')
    test_data_path:str = os.path.join('artifacts', 'test.csv')
    raw_data_path:str = os.path.join('artifacts', 'data.csv')
    

# Data Ingestion Class
# ---------------------------
# This class is responsible for reading data from a source, splitting it into
# train and test sets, and exporting the corresponding paths.

class DataIngestion():    
    
    def __init__(self):
        """
        Initializes the DataIngestion class
        """
        self.Data_ingestion_config = DataIngestionConfig()
                
    def initiate_data_ingestion(self):
        """
        Reads data from a source, splits it into train and test sets, and exports the corresponding paths.
        """
        logging.info("Initiating Data Ingestion Config method")
        try:
            # Reading the Data
            logging.info("Reading the dataset from the source")
            df = pd.read_csv('notebook\data\study.csv') 
            
            # Export the Data to artifacts dir
            os.makedirs(name= os.path.dirname(self.Data_ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.Data_ingestion_config.raw_data_path, index=0, header=True)
            
            # Splitting the Data
            logging.info("Splitting the dataset into train and test sets")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=0)  
            
            # Exporting the corresponding paths            
            train_set.to_csv(self.Data_ingestion_config.train_data_path, index=0, header=True)
            test_set.to_csv(self.Data_ingestion_config.test_data_path, index=0, header=True)
            
            logging.info("Data Ingestion is completed !")  
            
            return (
                self.Data_ingestion_config.train_data_path, 
                self.Data_ingestion_config.test_data_path
            )
            
        except Exception as e:
            raise CustomException(e, sys)
        
        
        
if __name__ == "__main__":
    # Instantiate the DataIngestion class
    data_ingestion = DataIngestion()
    
    # Initiate the data ingestion process
    train_path, test_path = data_ingestion.initiate_data_ingestion()
    print(f'Training Data path: {train_path}')
    print(f'Test Data path: {test_path}')
    
    # Instantiate the DataTransformation class
    data_transformation = DataTransformation()
    
    # Initiate the data transformation process
    data_transformation.initiate_data_transformation(train_path, test_path)
