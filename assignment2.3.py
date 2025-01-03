#Enumerate list

#1) write a python code that to use enumerate to print the index and value in the list. Create a list of element by your own.
my_list = ["apple", "ps5", "nissan", "coffee", "pizza"]

# Use enumerate to get index and value
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")


#2) use the same list and now the indexing should start from 1
my_list = ["apple", "ps5", "nissan", "coffee", "pizza"]
for index, value in enumerate(my_list, start=1):
    print(f"Index: {index}, Value: {value}")