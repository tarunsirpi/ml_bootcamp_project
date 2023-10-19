import os
import sys
import pickle
import numpy as np 
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

from src.exception import CustomException
from src.logger import logging


def load_model(file_path):
  try:
    with open(file_path, 'rb') as file_obj:
      return pickle.load(file_obj)
  except Exception as e:
    logging.info("Exception occured in load_model function in utils")
    raise CustomException(e,sys)
  
def save_model(file_path, obj):
  try:
    dir_path = os.path.dirname(file_path)
    os.makedirs(dir_path, exist_ok=True)

    with open(file_path, 'wb') as file_obj:
      pickle.dump(obj, file_obj)

  except Exception as e:
    logging.info("Exception in save_model utils function")
    raise CustomException(e,sys)
  
def evaluate_model(X_train, y_train, X_test, y_test, models:dict ):
  try:
    report = {}
    for i in models.keys():
      model = models[i]
      model.fit(X_train, y_train)

      y_pred = model.predict(X_test)

      # mae = mean_absolute_error(y_test, y_pred)
      # rmse = mean_squared_error(y_test, y_pred, squared=False)
      r2 = r2_score(y_test, y_pred)

      report[i] = r2
    return report

  except Exception as e:
    logging.info("error in evaluate_model utils function")
    raise CustomException(e,sys)
