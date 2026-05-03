# DISK HEALTH CHECKER

import time
import shutil
import logging
import socket
import platform



# Data

DISK_PATH = "/" if platform.system() != "Windows" else r"C:\\"

MIN_FREE_PCT_WARNING = 20
MIN_FREE_PCT_CRITICAL = 5
GB = 1024 ** 3
CHECK_INTERVAL_SECONDS = 120
LOG_FILE = "disk_health.log"
HOSTNAME = socket.gethostname()

# Logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    handlers=[
        logging.FileHandler(LOG_FILE),
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

def build_message(status, used_space_gb, total_space_gb, free_space_gb, free_space_pct):

    match status:
        case "CRITICAL":
           note = "Disk almost full"
        case "WARNING":
            note = "Low disk space"
        case _:
            note = "Disk space OK"

    message = "STATUS: %s | HOSTNAME: %s | DISK: %s | NOTE: %s | USED: %.2fGB/%.2fGB | FREE: %.2fGB (%.2f%%)" %(status, HOSTNAME, DISK_PATH, note, used_space_gb, total_space_gb, free_space_gb, free_space_pct)


    return message

        
def log_status(status, used_space_gb, total_space_gb, free_space_pct, free_space_gb, message):

    match status:
        case "CRITICAL":
            logging.critical(message)
        case "WARNING":
            logging.warning(message)
        case _:
            logging.info(message)
        
# Main loop
def main():
    previous_status = None
    try:
        while True:
            used_space_gb, total_space_gb, free_space_pct, free_space_gb = get_disk_usage()
            status = check_status(free_space_pct)
            message = build_message(status, used_space_gb, total_space_gb, free_space_gb, free_space_pct)
            if previous_status is None or status != previous_status:
                log_status(status, used_space_gb, total_space_gb, free_space_pct, free_space_gb, message)
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
    except Exception as e:
        logging.error("ERROR: Unexpected error: %s", e)


if __name__ == "__main__":
    main()
    
