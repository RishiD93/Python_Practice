#Def functions


#1) create a function which take two numbers and perform addition and return their sum.
def add_numbers(a, b):
    """
    This function takes two numbers as input, adds them, and returns their sum.
    """
    return a + b
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = add_numbers(num1, num2)

# Print the result
print(f"The sum of {num1} and {num2} is {result}.")


#2) create a function which take a number as a input and return its factorial

def factorial(n):
    """
    This function takes a positive integer as input
    and returns its factorial.
    """
    # Initialize the result
    result2 = 1

    # Calculate factorial using a for loop
    for i in range(1, n + 1):
        result2 *= i

    return result2

num = int(input("Enter a positive integer: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    
    print(f"The factorial of {num} is {factorial(num)}.")