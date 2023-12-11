''' Challenge Write a Python script to:
1.Display all the prime numbers between 1 to 250.
2.Store the results in a results.txt file.
3.Test the script. Verify that it produced the expected results in the results.txt file.'''

def is_prime(n):
# n: An integer number. Returns: True if the number is prime, False otherwise. 
# A number is prime if it has exactly two factors: 1 and itself.
  if n <= 1:
    return False
  
  for i in range(2, int(n**0.5) + 1 ):
    if n % i == 0:
      return False
    
  return True

# Open results file for writing
with open("results.txt", "w") as file:
  for num in range(1, 251):
    if is_prime(num):
      file.write(str(num) + "\n")

print("Finish")