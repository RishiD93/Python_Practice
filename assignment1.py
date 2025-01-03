#if else
#1) write a python code that takes a integer as a value input and prints whether the number is even or odd
number = int(input("Enter an integer : "))

if number % 2 ==0:
    print(f"The number{number} is even.")
else:
    print(f"The number{number} is odd")


#2) write a python code to check any given year as a input is leap year or not. Leap year is calculated if it is divisible by 4
year = int(input("Enter a year : "))
if year % 4 ==0:
    print(f"The Year{year} is Leap year. ")
else:
    print(f"The Year{year} is not Leap year.")



    