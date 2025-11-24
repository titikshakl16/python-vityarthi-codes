import time
import tracemalloc
def sumdiv(n):
    s = 1
    if n == 1:
        return 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            s = s + i
            if i * i != n:
                s = s + n // i
        i = i + 1
    return s
def are_amicable(a, b):
    sum_a = sumdiv(a)
    sum_b = sumdiv(b)
    return sum_a == b and sum_b == a
tracemalloc.start()
start_time = time.time()
initial_memory, peak_memory = tracemalloc.get_traced_memory()
try:
    n1_str = input("Enter the first number (a): ")
    n2_str = input("Enter the second number (b): ")
    num1 = int(n1_str)
    num2 = int(n2_str)
    if num1 <= 0 or num2 <= 0:
        print("Please enter positive integers.")
        result = False
    elif num1 == num2:
        print(f"The numbers {num1} and {num2} are the same.")
        result = False
    else:
        result = are_amicable(num1, num2)
        print(f"Result: Are {num1} and {num2} amicable? {result}")
except ValueError:
    print("Invalid input. Please enter valid integers.")
end_time = time.time()
final_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()
time_taken = end_time - start_time
memory_change_kb = (final_memory - initial_memory) / 1024
print(f"Execution Time: {time_taken:.6f} seconds")
print(f"Memory Utilisation: {memory_change_kb:.4f} KiB")