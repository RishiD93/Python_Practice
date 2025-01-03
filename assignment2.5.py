#lambda functions

#1) create a list of tuples and write a lambda function to sort the list by second element of each tuple

tuple_list = [(1, 'banana'), (3, 'apple'), (2, 'cherry'), (4, 'date')]

sorted_list = sorted(tuple_list, key=lambda x: x[1])

print(f"Original list: {tuple_list}")
print(f"Sorted list by second element: {sorted_list}")


#2) filter odd numbers from the list using lambda function.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

# Print the result
print(f"Original list: {numbers}")
print(f"Odd numbers: {odd_numbers}")