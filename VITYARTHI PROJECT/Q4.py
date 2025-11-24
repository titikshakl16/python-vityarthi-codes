import time, tracemalloc 
def digital_root(n): 
 while n >= 10: 
  n = sum(int(d) for d in str(n)) 
 return n 
start = time.time() 
tracemalloc.start() 
num = int(input("Enter a number: ")) 
root = digital_root(num) 
end = time.time() 
current, peak = tracemalloc.get_traced_memory() 
tracemalloc.stop() 
print(f"Digital root of {num} is {root}") 
print(f"Time taken: {end - start:.6f} seconds") 
print(f"Memory used: {current / 1024:.2f} KB (peak: {peak / 1024:.2f} KB)")