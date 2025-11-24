import time
import tracemalloc

def is_automorphic(n):
    return str(n*n).endswith(str(n))

n = int(input("Enter a number: "))

tracemalloc.start()
start = time.time()

result = is_automorphic(n)

end = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Is {n} automorphic? {result}")
print(f"Time taken: {end - start:.6f} seconds")
print(f"Memory used: {current/1024:.2f} KB; Peak: {peak/1024:.2f} KB")