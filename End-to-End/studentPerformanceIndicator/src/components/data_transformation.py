# This module is responsible for performing data transformation on the data

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from dataclasses import dataclass
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object


@dataclass
class DataTransformationConfig:
    """
    Data class for storing config parameters
    """
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")
    

class DataTransformation:
    """
    Class responsible for data transformation
    """
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        
    def _create_numerical_pipeline(self) -> Pipeline:
        """
        Creates a pipeline for numerical features
        """
        return Pipeline(
            steps=[
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler(with_mean=False))
            ]
        )

    def _create_categorical_pipeline(self) -> Pipeline:
        """
        Creates a pipeline for categorical features
        """
        return Pipeline(
            steps=[
                ("imputer", SimpleImputer(strategy='most_frequent')),
                ("OneHotEncoder", OneHotEncoder()),
                ("scaler", StandardScaler(with_mean=False))
            ]
        ) 
        
    def get_data_transformer_obj(self) -> Pipeline:
        """
        Returns a pipeline object for data transformation
        """
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            num_pipeline = self._create_numerical_pipeline()
            
            logging.info(f"Numerical features {numerical_columns}: Standard Scaling completed !")
            
            cat_pipeline = self._create_categorical_pipeline()
            
            logging.info(f"Categorical featuree {categorical_columns}: encoding completed !")
            
            
            preprocessor = ColumnTransformer(
                transformers=[                                   
                    ("numerical_pipeline", num_pipeline, numerical_columns),
                    ("categorical_pipeline", cat_pipeline, categorical_columns)              
                ]
            )
            
            return preprocessor            
            
        except Exception as e:
            raise CustomException(e, sys)
        
           
    def initiate_data_transformation(self, train_path, test_path):
        """
        This function is responsible for data transformation
        """
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            logging.info("Reading the train and test datasets is completed !")
            
            
            logging.info("Obtaining Preprocessing object")
            preprocessing_obj = self.get_data_transformer_obj()
            
            target_feature = 'math_score'
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
            
            # Split data into input features and target feature
            
            input_feature_train_df = train_df.drop(columns=[target_feature], axis=1)
            target_feature_train_df = train_df[target_feature]
            target_feature_test_df = test_df[target_feature]
            
            # Apply preprocessing object to training data
            input_feature_train_arr = preprocessing_obj.fit_transform(train_df.drop(columns=[target_feature], axis=1))
            logging.info("Apply preprocessing object to training data")
            
            # Apply preprocessing object to testing data
            input_feature_test_arr = preprocessing_obj.transform(test_df.drop(columns=[target_feature], axis=1))
            logging.info("Applied preprocessing object to testing data")

            
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]
            
            logging.info("Preprocessing complete")
            
            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessing_obj
            )
            
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )         
            
        except Exception as e:
            raise CustomException(e, sys)
        

