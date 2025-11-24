import time
import tracemalloc

start_time = time.time()
tracemalloc.start()

a = int(input("Enter a number: "))
c = 0

for i in range(2, a + 1):
    if a % i == 0:
        f = int(i ** 0.5)
        for j in range(2, f + 1):
            if i % j == 0:
                break
        else:
            print(i)
            c += 1

print("Total number of prime factors are", c)

current, peak = tracemalloc.get_traced_memory()
end_time = time.time()

print(f"\nTime taken: {end_time - start_time:.6f} seconds")
print(f"Current memory usage: {current / 1024:.2f} KB")
