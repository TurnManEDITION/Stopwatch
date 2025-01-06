import os, time
from edit import *

i = 0
times = "00:00:00"
times = start_edit_stopwatch(times)
while True:
    local_data = edit_data(time.asctime().split())
    local_data = " | ".join(local_data)
    print(local_data)

    print(f"Stopwatch - {times}")
    time.sleep(1)
    times = times.split(":")
    times = work_stopwatch(times)
    times = check_stopwatch(times)
    times = edit_stopwatch(times)
    os.system("cls")
 


    