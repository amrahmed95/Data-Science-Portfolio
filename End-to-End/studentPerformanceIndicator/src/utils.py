import os
import sys

import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def save_object(file_path, obj):
    """
    Saves an object to a file.

    Args:
        file_path (str): The path to the file.
        obj (object): The object to be saved.

    Raises:
        CustomException: If there is an error while saving the object.
    """
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    """
    Evaluates multiple models on the given training and testing data.

    Args:
        X_train (numpy.ndarray): The training input data.
        y_train (numpy.ndarray): The training target data.
        X_test (numpy.ndarray): The testing input data.
        y_test (numpy.ndarray): The testing target data.
        models (dict): A dictionary of models to be evaluated.
        param (dict): A dictionary of parameters for each model.

    Returns:
        dict: A dictionary containing the test score for each model.

    Raises:
        CustomException: If there is an error while evaluating the models.
    """
    try:
        report = {}  # Dictionary to store the test score for each model

        for i in range(len(list(models))):
            model = list(models.values())[i]  # Get the model
            para = param[list(models.keys())[i]]  # Get the parameters for the model

            gs = GridSearchCV(model, para, cv=3)  # Perform grid search to find the best parameters
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)  # Set the best parameters for the model
            model.fit(X_train, y_train)  # Train the model

            y_train_pred = model.predict(X_train)  # Predict the target values for the training data

            y_test_pred = model.predict(X_test)  # Predict the target values for the testing data

            train_model_score = r2_score(y_train, y_train_pred)  # Calculate the R^2 score for the training data

            test_model_score = r2_score(y_test, y_test_pred)  # Calculate the R^2 score for the testing data

            report[list(models.keys())[i]] = test_model_score  # Store the test score for the model

        return report

    except Exception as e:
        raise CustomException(e, sys)
