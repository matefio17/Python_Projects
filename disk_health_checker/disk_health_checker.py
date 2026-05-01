# DISK HEALTH CHECKER

import time
import shutil
import logging


# Data

DISK_PATH = "/"

MIN_FREE_PCT_WARNING = 20
MIN_FREE_PCT_CRITICAL = 5

CHECK_INTERVAL_SECONDS = 120

# Logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    handlers=[
        logging.FileHandler("disk_health.log"),
        logging.StreamHandler()
    	]
)


# Functions

def get_disk_usage():
    total, used, free = shutil.disk_usage(DISK_PATH)
    
    gb = 1024 ** 3
    
    free_space_pct = ((free / total) * 100)
    free_space_gb = free / gb
		  
    return free_space_pct, free_space_gb   
    

def check_logging_conditions(free_space_pct):
    if free_space_pct < MIN_FREE_PCT_CRITICAL:
        status = "CRITICAL" 
    elif free_space_pct < MIN_FREE_PCT_WARNING:
        status = "WARNING"    
    else: 
        status = "OK"
    return status 
        
def logging_process(status, free_space_pct, free_space_gb):
    match status:
        case "CRITICAL":
            logging.critical("Disk almost full. Only %.2f%%, (%.2fGB) of free space left.", free_space_pct, free_space_gb)
        case "WARNING":
            logging.warning("Low disk space. Only %.2f%% (%.2fGB) of free space left.", free_space_pct, free_space_gb)
        case _:
            logging.info("Disk space OK. %.2f%% (%.2fGB) of free space left.", free_space_pct, free_space_gb)
        
# Main loop

try:
    while True:
        free_space_pct, free_space_gb = get_disk_usage()
        status = check_logging_conditions(free_space_pct)
        logging_process(status, free_space_pct, free_space_gb)
        time.sleep(CHECK_INTERVAL_SECONDS)
except FileNotFoundError:
    logging.info("ERROR: Missing file.")
except KeyboardInterrupt:
    logging.info("Program stopped by user.")
except Exception:
    logging.error("Unexpected error.")
    
