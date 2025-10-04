from datetime import datetime
import time

for i in range(5):
    print(datetime.now().strftime("%H:%M:%S"))
    time.sleep(1)