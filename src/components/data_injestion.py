
import pandas as pd
from sklearn.model_selection import train_test_split

import os
import sys
from dataclasses import dataclass

from src.logger import logging
from src.exception import CustomException


class DataIngestionConfig():
  train_data_path = os.path.join("artifact", "train.csv")
  test_data_path = os.path.join("artifact", "test.csv")
  raw_data_path = os.path.join("artifact", "raw.csv")



class DataIngestion():
  def __init__(self):
    self.ingestion_config = DataIngestionConfig()

  def initiate_data_ingestion(self):
    try:
      df = pd.read_csv(os.path.join("notebooks/data/cleandata.csv"))

      os.makedir(os.path.dirname(self.injestion_config.raw_data_path), exist_ok = True)

      df.to_csv(self.injestion_config.raw_data_path)

      train_set, test_set = train_test_split(df,test_size=0.25, random_state=42)
      train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
      test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)

    except Exception as ex:
      raise Exception