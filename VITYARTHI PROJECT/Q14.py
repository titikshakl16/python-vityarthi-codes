import time
import tracemalloc

start_time = time.time()
tracemalloc.start()

a = int(input("Enter a non-negative integer: "))

for i in range(2, a - 1):
    f = int(i ** 0.5)
    for j in range(2, f + 1):
        if i % j == 0:
            break
    else:
        g = int((i + 2) ** 0.5)
        for k in range(2, g + 1):
            if (i + 2) % k == 0:
                break
        else:
            print(i, i + 2)

current, peak = tracemalloc.get_traced_memory()
end_time = time.time()

print(f"\nTime taken: {end_time - start_time:.6f} seconds")
print(f"Current memory usage: {current / 1024:.2f} KB")
print(f"Peak memory usage: {peak / 1024:.2f} KB")

tracemalloc.stop()
