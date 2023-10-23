import sys
import os

from src.utils import load_model
from src.logger import logging
from src.exception import CustomException

import pandas as pd

class PredictPipeline:
  def __init__(self):
    pass

  def predict(self, data):
    try:
      preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
      model_path = os.path.join("artifacts", "model.pkl")
      
      preprocessor = load_model(preprocessor_path)
      model = load_model(model_path)

      data_scaled = preprocessor.transform(data)
      pred = model.predict(data_scaled)

      return pred

    except Exception as e :
      logging.info("Error in prediction")
      logging.error(CustomException(e, sys))
      CustomException(e, sys)

class CustomData:
  def __init__(self, carat:float, depth:float, table:float, x:float, y:float, z:float, cut:str, color:str, clarity:str):
    self.carat = carat
    self.depth=depth
    self.table=table
    self.x=x
    self.y=y
    self.z=z
    self.cut = cut
    self.color = color
    self.clarity = clarity

  def get_data_as_dataframe(self):
    try:
      custom_data_input_dict = {'carat':[self.carat],
                                'cut':[self.cut],
                                'color':[self.color],
                                'clarity':[self.clarity],
                                'depth':[self.depth], 
                                'table':[self.table],
                                'x':[self.x],
                                'y':[self.y],
                                'z':[self.z],}
      
      df= pd.DataFrame(custom_data_input_dict)
      logging.info("Dataframe gathered")
      return df

    except Exception as e:
      logging.info("Exception in prediction pipeline")
      logging.error(CustomException(e, sys))
      CustomException(e, sys)


if __name__ == "__main__":
  test = CustomData(carat=2.2, depth=59, table=60.0, x=8.8, y=8.9, z=5.0, cut='Premium', color='F', clarity='VS2')
  df1= test.get_data_as_dataframe()
  print(df1)