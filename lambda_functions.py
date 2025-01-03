# Lambda function examples

# Lambda to add two numbers
add = lambda x, y: x + y
print(f"Sum of 5 and 3: {add(5, 3)}")

# Lambda to find the square of a number
square = lambda x: x**2
print(f"Square of 4: {square(4)}")

# Lambda with filter to find even numbers in a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")