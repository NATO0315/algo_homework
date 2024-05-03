import time
import numpy as np
import matplotlib.pyplot as plt

start_time = time.time()
fibonacci_list = [0]*100
time_list = [0]*100

for i in range(100):
    if i < 2:
        fibonacci_list[i] = 1
    else:
        fibonacci_list[i] = fibonacci_list[i-1] + fibonacci_list[i-2]
    time_list[i] = time.time() - start_time

print(fibonacci_list)
print(time_list)

x = range(1, 101)
y = time_list
plt.plot(x, y)
plt.xlabel('f(i)')
plt.ylabel('runtime')
plt.show()
