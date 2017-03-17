import time

start_time = time.time()
elapsed_time = time.time() - start_time
if (elapsed_time > 2):
    return Lose
elif 0 <= elapsed_time <= 1:
    mang +=1
    return Continue
elif elapsed_time >1:
    return Continue


