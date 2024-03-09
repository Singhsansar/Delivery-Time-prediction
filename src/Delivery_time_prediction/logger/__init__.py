import logging
import os
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = "logfile.log"

LOG_FILE_PATH = os.path.join(os.getcwd(), LOG_DIR)
os.makedirs(LOG_FILE_PATH, exist_ok=True)

# Get the current timestamp
CURRENT_TIME_STAMP = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
FILE_NAME = f"log_{CURRENT_TIME_STAMP}.log"  # Modified timestamp format

# Construct the full path to the log file
log_file_path = os.path.join(LOG_FILE_PATH, FILE_NAME)

logging.basicConfig(
    filename=log_file_path,
    filemode="a",  # Append mode to avoid overwriting existing logs
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger("Delivery_time_predection logger")
