import time
import tracemalloc

def count_divisors(n):
    if n == 0:
        return 0
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
        i += 1
    return count

start_time = time.time()
tracemalloc.start()

num = int(input("Enter a positive integer: "))
result = count_divisors(num)
print(f"Number of divisors of {num} =", result)

current, peak = tracemalloc.get_traced_memory()
end_time = time.time()

print(f"\nTime taken: {end_time - start_time:.6f} seconds")
print(f"Current memory usage: {current / 1024:.2f} KB")
print(f"Peak memory usage: {peak / 1024:.2f} KB")

tracemalloc.stop()
