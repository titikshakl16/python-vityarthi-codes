import time 
from functools import lru_cache 
@lru_cache(maxsize=None) 
def is_palindrome(n): 
 return str(n) == str(n)[::-1] 
num = int(input("Enter a number: ")) 
start_time = time.time() 
if is_palindrome(num): 
 print(f"{num} is a palindrome.") 
else: 
 print(f"{num} is not a palindrome.") 
end_time = time.time() 
print(f"Checked in {end_time - start_time:.6f} seconds.") 