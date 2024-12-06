import schedule
import time
import requests
from datetime import datetime
from dotenv import load_dotenv
import os

# URL API Call
load_dotenv()
URL = os.getenv("URL_IDEALISTA")

def execute_process():
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            print(f"Process succeed: {response.json()}")
        else:
            print(f"Error executing process. Code: {response.status_code}")
    except Exception as e:
        print(f"Error during execution process: {e}")

# Schedules the process to execute every 1 minute
schedule.every(1).minutes.do(execute_process)

if __name__ == "__main__":
    print("Initializing automated execution...")
    while True:
        print("Process started at time: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        schedule.run_pending()
        time.sleep(60)
