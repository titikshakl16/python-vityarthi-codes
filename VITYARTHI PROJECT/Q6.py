import time
import tracemalloc

def is_deficient(n):
    
    s = 1 if n > 1 else 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
    return s < n


n = int(input("Enter a number: "))

tracemalloc.start()
start = time.time()

result = is_deficient(n)

end = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Is {n} deficient? {result}")
print(f"Time taken: {end - start:.6f} seconds")
print(f"Memory used: {current / 1024:.2f} KB; Peak: {peak / 1024:.2f} KB")