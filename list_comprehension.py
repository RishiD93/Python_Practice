# List comprehension example
# Create a list of squares for numbers 1 to 10
squares =[x**2 for x in range(1,11)]
print(f"Squares from 1 to 10 are : {squares}")


# Create a list of even numbers from 1 to 20
even_numbers =[ x for x in range(1,21) if x % 2 ==0]
print(f"even numbers from 1 to 20 are : {even_numbers}")

# Create a list of words longer than 3 characters from a given list
words = ["cat", "elephant", "dog", "tiger"]
long_words = [word for word in words if len(word) > 3]
print(f"Words longer than 3 characters: {long_words}")