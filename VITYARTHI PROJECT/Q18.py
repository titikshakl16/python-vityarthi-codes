import time
import tracemalloc
def calculate_digit_product(n):
    product = 1
    s = str(n)
    for digit in s:
        product *= int(digit)
    return product
def find_persistence(n):
    steps = 0
    current_num = n
    while current_num >= 10:
        steps += 1
        current_num = calculate_digit_product(current_num)
    return steps
def main():
    try:
        user_input = input("Enter a positive integer (n): ")
        n = int(user_input)
        if n < 0:
            print("Input must be a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    tracemalloc.start()
    start_time = time.perf_counter()
    result = find_persistence(n)
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    execution_time = end_time - start_time
    memory_peak_kb = peak / 1024
    print("Multiplicative Persistence:", result)
    print("Execution Time:", execution_time, "seconds")
    print("Peak Memory Utilization:", memory_peak_kb, "KiB")
if __name__ == "__main__":
    main()