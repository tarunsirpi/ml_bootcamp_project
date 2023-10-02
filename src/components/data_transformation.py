import os
import sys
from dataclasses import dataclass

print(os.getcwd())

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder,StandardScaler
from src.components.data_ingestion import DataIngestion

from src.exception import CustomException
from src.logger import logging

from src.utils import save_model

@dataclass
class DataTransformationConfig:
  preprocessor_obj_file = os.path.join("artifacts","preprocessor.pkl")

class DataTransformation:
  def __init__(self):
    self.data_transformation_config=DataTransformationConfig()

def get_data_transformation_object(self):
  try:
    logging.info('Data Transformation initiated')

    categorical_cols = ['cut', 'color','clarity']
    numerical_cols = ['carat', 'depth','table', 'x', 'y', 'z']
    
    cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
    color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
    clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']
    
    logging.info('Pipeline Initiated')

    num_pipeline=Pipeline(
        steps=[
        ('imputer',SimpleImputer(strategy='median')),
        ('scaler',StandardScaler())

        ]

    )

    cat_pipeline=Pipeline(
        steps=[
        ('imputer',SimpleImputer(strategy='most_frequent')),
        ('ordinalencoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
        ('scaler',StandardScaler())
        ]
    )

    preprocessor=ColumnTransformer([
    ('num_pipeline',num_pipeline,numerical_cols),
    ('cat_pipeline',cat_pipeline,categorical_cols)
    ])
    
    return preprocessor

    logging.info('Pipeline Completed')

  except Exception as e:
      logging.info("Error in Data Trnasformation")
      raise CustomException(e,sys)

if __name__=='__main__':
  obj=DataIngestion()
  train_data_path, test_data_path=obj.initiate_data_ingestion()
  data_transformation = DataTransformation()
  train_arr,test_arr,_=data_transformation.initaite_data_transformation(train_data_path, test_data_path)
