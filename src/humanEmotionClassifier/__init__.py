import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"                                           # These 3 lines will create the logging file where we will store the logs
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(                          
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),  #This will print the logs in the logging file
        logging.StreamHandler(sys.stdout)   #This will print the logs into the Terminal
    ]
)

logger = logging.getLogger("humanEmotionClassifierLogger")   # Naming the log
