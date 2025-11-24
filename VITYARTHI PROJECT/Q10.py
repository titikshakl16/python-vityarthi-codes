import time
import tracemalloc

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
    if n > 1:  
        factors.append(n)
    return factors

n = int(input("Enter a number: "))

tracemalloc.start()
start = time.time()

result = prime_factors(n)

end = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Prime factors of {n}: {result}")
print(f"Time taken: {end - start:.6f} seconds")
print(f"Memory used: {current/1024:.2f} KB; Peak: {peak/1024:.2f} KB")