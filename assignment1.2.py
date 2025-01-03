#loop questions
from math import factorial

#1) python code to calculate sum of the n natural numbers, where n is provided as a input
n = int(input("Enter a positive integer: "))
total_sum = 0
for i in range(1,n + 1):
  total_sum +=i
  print(f"The sum of the first {n} natural number is {total_sum}.")


#2) python code to find a factorial solution of the given input
r =int(input("Enter a positive integer: "))
factorial =1

for v in range(1,n+1):
    factorial *= 1
print(f"The factorial of {r} is {factorial}.")