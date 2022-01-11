import time
import test
from scipy.integrate import quad
from scipy import LowLevelCallable as llc

def f2(x):
    return 1/(x * x)

n = 100

# total time to run integral of f2 with Python n times
t_sum = 0
for i in range(n):
    t1 = time.time()
    quad(f2, 0.5, 4)
    t2 = time.time()
    t_sum += (t2 - t1)

# total time to run integral of f2 with Cython n times
t_sum2 = 0
f_py = llc.from_cython(test, 'f2')
for i in range(n):
    t1 = time.time()
    quad(f_py, 0.5, 4)
    t2 = time.time()
    t_sum2 += (t2 - t1)

# average time for the two methods:
avg1 = t_sum/n
avg2 = t_sum2/n

print("The integral of f2 was called with Python " + str(n) + " times, and took on average " + str(avg1) + " seconds.")
print("The integral of f2 was called with Cython " + str(n) + " times, and took on average " + str(avg2) + " seconds.")
