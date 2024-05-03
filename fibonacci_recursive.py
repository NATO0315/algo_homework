import time
import numpy as np
import matplotlib.pyplot as plt

start_time = time.time()
time_list = [0]*50
cal_times = 0
times_list = [0]*50

def fibonacci(i):
    global cal_times
    if i < 2:
        return 1
    elif i >= 2:
        if i == 4:
            cal_times += 1
        return fibonacci(i-1) + fibonacci(i-2)

for i in range(50):
    num = fibonacci(i)
    print(num)
    time_list[i] = time.time() - start_time
    times_list[i] = cal_times

print(time_list)

x = range(1, 51)
y = time_list
plt.plot(x, y)
plt.xlabel('f(i)')
plt.ylabel('runtime')
plt.show()

x = range(1, 51)
y = times_list
plt.plot(x, y)
plt.xlabel('f(i)')
plt.ylabel('cal_times')
plt.show()
