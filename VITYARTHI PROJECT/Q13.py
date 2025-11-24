import time
import tracemalloc

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_mersenne_prime(p):
    if p <= 1:
        return False
    mersenne_num = (2**p) - 1

    return is_prime(mersenne_num)
try:
    num = int(input("Enter a prime number (p): "))
    tracemalloc.start()
    start_time = time.perf_counter_ns()
    
    result = is_mersenne_prime(num)
    
    end_time = time.perf_counter_ns()
    memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print(f"Is 2^{num} - 1 a prime number? {result}")
    print(f"Time used: {end_time - start_time} nanoseconds")
    print(f"Memory used: {memory[1]} bytes")

except ValueError:
    print("Invalid input. Please enter an integer.")
