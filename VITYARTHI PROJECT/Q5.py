import time 
import tracemalloc 
def is_abundant(n): 
  return sum(i for i in range(1, n//2 + 1) if n % i == 0) > n 
n = int(input("Enter a number: ")) 
tracemalloc.start() 
start = time.time() 
result = is_abundant(n) 
end = time.time() 
current, peak = tracemalloc.get_traced_memory() 
tracemalloc.stop() 
print(f"Is {n} abundant? {result}") 
print(f"Time taken: {end - start:.6f} seconds") 
print(f"Memory used: {current / 1024:.2f} KB (Peak: {peak / 1024:.2f} KB)")