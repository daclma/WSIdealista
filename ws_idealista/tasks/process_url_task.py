import schedule
import time
import requests
from datetime import datetime

# URL API Call
URL = "http://127.0.0.1:5000/processUrl?url=https://www.idealista.com/alquiler-viviendas/barcelona/horta-guinardo/?ordenado-por=fecha-publicacion-desc"

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
