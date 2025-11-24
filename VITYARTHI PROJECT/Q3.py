import time, tracemalloc 
def mean_of_digits(n): 
 digits = [int(d) for d in str(abs(n))] 
 return sum(digits) / len(digits) 
start = time.time() 
tracemalloc.start() 
num = int(input("Enter a number: ")) 
mean = mean_of_digits(num) 
end = time.time() 
current, peak = tracemalloc.get_traced_memory() 
tracemalloc.stop() 
print(f"Mean of digits: {mean}") 
print(f"Time taken: {end - start:.6f} seconds") 
print(f"Memory used: {current / 1024:.2f} KB (peak: {peak / 1024:.2f} KB)") 