import time 
import tracemalloc 
 
def is_quadratic_residue(a, p): 
     
 
     
    start_time = time.time() 
    tracemalloc.start() 
 
     
    a = a % p 
    if a == 0: 
        result = True   
    else: 
         
        exp = (p - 1) // 2 
        check = pow(a, exp, p) 
        result = (check == 1) 
 
     
    current, peak = tracemalloc.get_traced_memory() 
    tracemalloc.stop() 
    end_time = time.time() 
 
    print(f"Time taken: {end_time - start_time:.6f} seconds") 
    print(f"Memory used: {current / 1024:.2f} KB; Peak: {peak / 1024:.2f} KB") 
 
    return result