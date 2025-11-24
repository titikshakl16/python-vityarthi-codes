import time
import tracemalloc
def mod_exp(base, exponent, modulus):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result
print("Enter base, exponent, and modulus separated by spaces (e.g., 2 10 5):")
try:
 user_input = input()
 base, exponent, modulus = map(int, user_input.split())
except:
 print("Error: Invalid input. Please enter three integers separated by spaces.")
 exit()
 tracemalloc.start()
start_time = time.perf_counter()
final_result = mod_exp(base, exponent, modulus)
end_time = time.perf_counter()
current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()
execution_time = end_time - start_time
peak_memory_kib = peak_memory / 1024
print("Result:")
print(final_result)
print("Execution Time:")
print(f"{execution_time:.6f} seconds")
print("Peak Memory Usage:")
print(f"{peak_memory_kib:.2f} KiB")