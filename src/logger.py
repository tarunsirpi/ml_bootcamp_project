import logging
from datetime import datetime
import os

LOG_FILE = f"{datetime.now().strftime('%b_%d_%Y_%H:%M:%S')}.log"

log_path = os.path.join(os.getcwd(),"logs", LOG_FILE)

print(LOG_FILE )
print(log_path)
os.makedirs(os.path.join(os.getcwd(),"logs"), exist_ok=True)


LOG_FILE_PATH=os.path.join(log_path)

logging.basicConfig(filename= LOG_FILE_PATH , level = logging.INFO, format="[%(asctime)s]%(lineno)d %(name)s - %(levelname)s %(message)s")

print(LOG_FILE_PATH )
