import os
import sys
import dill

import numpy as np
import pandas as pd

from src.logger import logging
from src.exception import CustomException


def save_object(file_path, obj):
    """
    Saves an object to a file using dill library

    Args:
        file_path (str): path to the file where the object will be saved
        obj: object to be saved

    Raises:
        CustomException: if there is an error during the process
    """
    try:
        # create directory if it does not exist
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        # create file object and save the object using dill library
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        # raise an exception with the error message and the system information
        raise CustomException(e, sys)
