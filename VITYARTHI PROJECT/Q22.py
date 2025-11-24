import time 
import tracemalloc 
 
def mod_inverse(a, m): 
     
    def extended_gcd(a, b): 
        if b == 0: 
            return a, 1, 0 
        gcd, x1, y1 = extended_gcd(b, a % b) 
        x, y = y1, x1 - (a // b) * y1 
        return gcd, x, y 
 
    gcd, x, _ = extended_gcd(a, m) 
    if gcd != 1: 
        return None   
    return x % m 
 
def crt(remainders, moduli): 
     
 
     
    start_time = time.time() 
    tracemalloc.start() 
 
     
    M = 1 
    for m in moduli: 
        M *= m 
 
     
    total = 0 
    for r, m in zip(remainders, moduli): 
        Mi = M // m 
        inv = mod_inverse(Mi, m) 
        if inv is None: 
            tracemalloc.stop() 
            return None   
        total += r * Mi * inv 
 
    result = total % M 
 
     
    current, peak = tracemalloc.get_traced_memory() 
    tracemalloc.stop() 
    end_time = time.time() 
 
    print(f"Time taken: {end_time - start_time:.6f} seconds") 
    print(f"Memory used: {current / 1024:.2f} KB; Peak: {peak / 1024:.2f} KB") 
 
    return result 
 
# Example  
remainders = [2, 3, 2] 
moduli = [3, 5, 7] 
print("Solution:", crt(remainders, moduli))