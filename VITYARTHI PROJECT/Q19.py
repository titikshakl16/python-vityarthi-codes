import time
import tracemalloc
def c(k):
    o = 0
    i = 1
    while i * i <= k:
        if k % i == 0:
            if i * i == k:
                o += 1
            else:
                o += 2
        i += 1
    return o
def h(n):
    if n <= 0:
        return False
    dn = c(n)
    m = 1
    while m < n:
        if c(m) >= dn:
            return False
        m += 1
    return True
tracemalloc.start()
t1 = time.time()
try:
    N = int(input("Enter an integer (N > 0): "))
except:
    N = 0
if N <= 0:
    print("Invalid input, N must be a positive integer.")
else:
    R = h(N)
    t2 = time.time()
    p, c_ = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print("Result:", R)
    print("Time:", t2 - t1, "s")
    print("Memory:", p / 1024, "KB")