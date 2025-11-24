import time 
import tracemalloc 
import math 
 
def order_mod(a, n): 
     
 
    start_time = time.time() 
    tracemalloc.start() 
 
     
    if math.gcd(a, n) != 1: 
        tracemalloc.stop() 
        print("No order exists since gcd(a, n) != 1") 
        return None 
 
     
    k = 1 
    value = a % n 
    while value != 1: 
        k += 1 
        value = (value * a) % n 
 
    result = k 
 
     
    current, peak = tracemalloc.get_traced_memory() 
    tracemalloc.stop() 
    end_time = time.time() 
 
    print(f"Time taken: {end_time - start_time:.6f} seconds") 
    print(f"Memory used: {current / 1024:.2f} KB; Peak: {peak / 1024:.2f} KB") 
 
    return result 
 
# Example  
print("Order of 2 mod 7:", order_mod(2, 7))    
print("Order of 3 mod 10:", order_mod(3, 10))  
print("Order of 5 mod 11:", order_mod(5, 11))