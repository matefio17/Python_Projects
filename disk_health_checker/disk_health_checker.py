# DISK HEALTH CHECKER

import time
import shutil
import logging



# Data

DISK_PATH = "C:\\"

MIN_FREE_PCT_WARNING = 20
MIN_FREE_PCT_CRITICAL = 5
GB = 1024 ** 3
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

    
    free_space_pct = ((free / total) * 100)
    free_space_gb = free / GB
    total_space_gb = total / GB
    used_space_gb = used / GB
		  
    return used_space_gb, total_space_gb, free_space_pct, free_space_gb
    

def check_status(free_space_pct):
    if free_space_pct < MIN_FREE_PCT_CRITICAL:
        status = "CRITICAL" 
    elif free_space_pct < MIN_FREE_PCT_WARNING:
        status = "WARNING"    
    else: 
        status = "OK"
    return status


        
def logging_process(status, used_space_gb, total_space_gb, free_space_pct, free_space_gb):
    match status:
        case "CRITICAL":
            logging.critical("%s - Disk almost full. == Current usage - %.2fGB/%.2fGB. == Only %.2f%%, (%.2fGB) of free space left.", DISK_PATH, used_space_gb, total_space_gb, free_space_pct, free_space_gb)
        case "WARNING":
            logging.warning("%s - Low disk space. == Current usage - %.2fGB/%.2fGB. == Only %.2f%% (%.2fGB) of free space left.", DISK_PATH, used_space_gb, total_space_gb, free_space_pct, free_space_gb)
        case _:
            logging.info("%s - Disk space OK. == Current usage - %.2fGB/%.2fGB. == %.2f%% (%.2fGB) of free space left.", DISK_PATH, used_space_gb, total_space_gb, free_space_pct, free_space_gb)
        
# Main loop
def main():
    previous_status = None
    try:
        while True:
            used_space_gb, total_space_gb, free_space_pct, free_space_gb = get_disk_usage()
            status = check_status(free_space_pct)
            if previous_status is None or status != previous_status:
                logging_process(status, used_space_gb, total_space_gb, free_space_pct, free_space_gb)
                previous_status = status
            time.sleep(CHECK_INTERVAL_SECONDS)
    except FileNotFoundError:
        logging.error("ERROR: Missing file.")
    except PermissionError:
        logging.error("ERROR: Permission Error.")
    except OSError:
        logging.error("ERROR: OS-related problem.")
    except ZeroDivisionError:
        logging.error("ERROR: Problem with metric collection (total capacity).")
    except KeyboardInterrupt:
        logging.info("Program stopped by user.")
    except Exception:
        logging.error("ERROR: Unexpected error.")


if __name__ == "__main__":
    main()
    
