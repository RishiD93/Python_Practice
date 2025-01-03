#List Comprehension

#1) write a list comprehension to create a list of square numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]
print(f"Squares from 1 to 10: {squares}")

#2) write a list comprehension to convert a list of strings to uppercase.
# Original list of strings
words = ["risha", "best", "babe", "red"]
uppercase_words = [word.upper() for word in words]
print(f"Uppercase words: {uppercase_words}")