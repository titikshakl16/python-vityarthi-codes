import time
import tracemalloc

def is_harshad(n):
    digit_sum = sum(int(d) for d in str(n))
    return n % digit_sum == 0


n = int(input("Enter a number: "))

tracemalloc.start()
start = time.time()

result = is_harshad(n)

end = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Is {n} a Harshad number? {result}")
print(f"Time taken: {end - start:.6f} seconds")
print(f"Memory used: {current/1024:.2f} KB; Peak: {peak/1024:.2f} KB")