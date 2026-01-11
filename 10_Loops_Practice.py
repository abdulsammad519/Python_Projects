# Exponential Backoff Strategy
# Solution:

import time
max_tries=5
wait_time=1
attempts=0


while attempts< max_tries:
    print("Attempt ", attempts+1,"-wait time", wait_time)
    time.sleep(wait_time)
    wait_time*=2
    attempts+=1