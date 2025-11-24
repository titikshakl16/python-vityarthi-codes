import time
import tracemalloc

def is_pronic(n):
    k = int(n**0.5)   
    return k * (k + 1) == n


n = int(input("Enter a number: "))

tracemalloc.start()
start = time.time()

result = is_pronic(n)

end = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Is {n} pronic? {result}")
print(f"Time taken: {end - start:.6f} seconds")
print(f"Memory used: {current/1024:.2f} KB; Peak: {peak/1024:.2f} KB")