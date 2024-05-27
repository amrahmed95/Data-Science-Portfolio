import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor


from src.logger import logging
from src.exception import CustomException
from src.utils import save_object, evaluate_model

from dataclasses import dataclass


@dataclass
class ModelTrainerConfig:
    """
    Dataclass to store the configuration for ModelTrainer
    """
    trained_model_file_path = os.path.join("artifacts", "base_model.pkl")


class ModelTrainer:
    """
    Class to train and save the model
    """
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def Initiate_ModelTrainer(self, train_array, test_array):
        """
        Method to train and save the model

        Args:
            train_array (numpy.ndarray): Training data
            test_array (numpy.ndarray): Testing data

        Returns:
            tuple: Best model and R2 score
        """
        try:
            # Split train and test input data
            logging.info("Splitting train and test input data")
            X_train, y_train, X_test, y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            # Define the models to be trained
            models = {
                "Linear Regression": LinearRegression(),
                "Lasso": Lasso(),
                "Ridge": Ridge(),
                "K-Neighbors Regressor": KNeighborsRegressor(),
                "Decision Tree Regressor": DecisionTreeRegressor(),
                "Random Forest Regressor": RandomForestRegressor(),
                "AdaBoost Regressor": AdaBoostRegressor(),
                "Gradient Boosting Regressor": GradientBoostingRegressor()
            }

            # Evaluate the models on the training and testing data
            model_report: dict = evaluate_model(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, models=models)

            # Get the best model score from the dictionary
            logging.info(f"Model Report: {model_report}")
            best_model_score = max(sorted(model_report.values()))

            # Get the name of the best model
            best_model_name = list(models.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            # Get the best model
            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No best model found")

            logging.info(f"Best model found on both training and testing dataset: {best_model}")

            # Save the best model
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            # Make predictions using the best model
            predicted = best_model.predict(X_test)

            # Calculate the R2 score
            #r2_square = r2_score(y_test, predicted) * 100
            r2_square = round(r2_score(y_test, predicted) * 100, 3)

            return (
                best_model,
                r2_square
            )

        except Exception as e:
            raise CustomException(e, sys)



