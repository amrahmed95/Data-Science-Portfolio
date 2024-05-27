import os
import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    """
    Class for predicting the target variable using a trained model
    """
    def __init__(self):
        """
        Initializes the PredictPipeline class
        """
        pass

    def predict(self, features):
        """
        Predicts the target variable using a trained model

        Args:
            features (DataFrame): Features to predict

        Returns:
            np.ndarray: Predicted target variable
        """
        try:
            # Load the trained model and preprocessor
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            print("Before Loading")
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            print("After Loading")

            # Scale the features using the preprocessor
            data_scaled = preprocessor.transform(features)

            # Predict the target variable using the model
            preds = model.predict(data_scaled)
            return preds

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    """
    Class for storing custom data as a DataFrame
    """
    def __init__(  self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):
        """
        Initializes the CustomData class

        Args:
            gender (str): Gender
            race_ethnicity (str): Race or ethnicity
            parental_level_of_education: Parental level of education
            lunch (str): Lunch option
            test_preparation_course (str): Test preparation course
            reading_score (int): Reading score
            writing_score (int): Writing score
        """
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        """
        Returns custom data as a DataFrame

        Returns:
            DataFrame: Custom data as a DataFrame
        """
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
