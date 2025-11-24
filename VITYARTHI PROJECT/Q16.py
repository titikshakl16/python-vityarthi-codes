import time
import psutil
import os
def aliquot_sum(n):
    if n <= 1:
        return 0
    total = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            total = total + i
            j = n // i
            if j != i:
                total = total + j
        i = i + 1
    return total
def main():
    try:
        n_str = input("Enter a positive integer (n): ")
        n = int(n_str)
    except:
        print("Invalid input. Please enter an integer.")
        return
    process = psutil.Process(os.getpid())
    start_time = time.time()
    initial_memory = process.memory_info().rss
    aliquot = aliquot_sum(n)
    end_time = time.time()
    final_memory = process.memory_info().rss
    execution_time = end_time - start_time
    memory_used = final_memory
    print("The sum of proper divisors of", n, "is:", aliquot)
    print("Execution Time:", execution_time, "seconds")
    print("Memory Utilization (Resident Set Size):", memory_used, "bytes")
if __name__ == "__main__":
    main()