import time
import tracemalloc

def prime(n):
    for i in range(2, n + 1):
        f = int(i ** 0.5)
        for j in range(2, f + 1):
            if i % j == 0:
                break
        else:
            p = 0
            c = 0
            while p <= n:
                c += 1
                p = i ** c
                if p == n:
                    print("TRUE", i, "to power", c)
                    return n
    print("FALSE")

start_time = time.time()
tracemalloc.start()

n = int(input("Enter a number: "))
prime(n)

current, peak = tracemalloc.get_traced_memory()
end_time = time.time()

print(f"\nTime taken: {end_time - start_time:.6f} seconds")
print(f"Current memory usage: {current / 1024:.2f} KB")
print(f"Peak memory usage: {peak / 1024:.2f} KB")

tracemalloc.stop()
