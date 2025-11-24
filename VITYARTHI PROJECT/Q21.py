import time 
import tracemalloc 
 
def mod_inverse(a, m): 
    
 
     
    start_time = time.time() 
    tracemalloc.start() 
 
    def extended_gcd(a, b): 
        
        if b == 0: 
            return a, 1, 0 
        gcd, x1, y1 = extended_gcd(b, a % b) 
        x, y = y1, x1 - (a // b) * y1 
        return gcd, x, y 
 
    gcd, x, _ = extended_gcd(a, m) 
 
    if gcd != 1: 
        result = None   
    else: 
        result = x % m   
 
    
    current, peak = tracemalloc.get_traced_memory() 
    tracemalloc.stop() 
    end_time = time.time() 
 
    print(f"Time taken: {end_time - start_time:.6f} seconds") 
    print(f"Memory used: {current / 1024:.2f} KB; Peak: {peak / 1024:.2f} KB") 
 
    return result 
 
# Example  
print("Inverse of 3 mod 11:", mod_inverse(3, 11))   
print("Inverse of 10 mod 17:", mod_inverse(10, 17))  
print("Inverse of 6 mod 9:", mod_inverse(6, 9))  