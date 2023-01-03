import logging
import os
from datetime import datetime

log_file_name=f"{datetime.now().strftime('%m%d_%Y__%H_%M_%S')}.log"


log_file_dir=os.path.join(os.getcwd(),"logs")


os.makedirs(log_file_dir,exist_ok=True)

log_file_path=os.path.join(log_file_dir,log_file_name)

logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s]  %(lineno)d %(name)s %(levelname)s %(message)s",
    level=logging.INFO
)
