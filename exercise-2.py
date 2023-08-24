### :heavy_plus_sign: Task 1 - comparison operators

# Your task is to write a program which asks the user three times about two integer numbers to compare. 
# >Hint: Use `while` loop to perform the same operation more than once!  

# Use both comparison and logical operators, for example use logical comparison between two or more comparison operators:  

# Create **at least ten** comparisons!

## Comparison 1
a = 1234
b = 5432
a = int(input("Enter the first number: ", ))
b = int(input("Enters the second number: ", ))
while a != b:
    print("The umbers are not equal.")
    break

## Comparison 2
a = 1234
b = 5432
a = int(input("Enter the first number: ", ))
b = int(input("Enters the second number: ", ))
while b > a:
    print("Second number is greater than first number.")
    break

## Comparison 3
a = 1234
b = 5432
a = int(input("Enter the first number: ", ))
b = int(input("Enters the second number: ", ))
while b >= a:
    print("Second number is greater than or equal to first number.")
    break

## Comparison 4
a = 1234
b = 5432
list = [1234, 5432]
a = int(input("Enter the first number: ", ))
b = int(input("Enters the second number: ", ))
if a > 1000 and b > 1000:
    print("Both numbers are big!")
else:
    print("Both numbers are not big")
    
## Comparison 5
### Big numbers a set of True
#firs_big_number = 1234
#second_big_number = 5432
big_numbers = {1234, 5432}
big_number1 = int(input("Enter the first big_number: ", ))
big_number2 = int(input("Enters the second big_number: ", ))
if big_number1 > 1000 and big_number2 > 1000:
    print("big_numbers is a set of True.")
else:
    print("big_numbers is not a set of True")
    
## Comparison 6
first_number = 23
second_number = 4567
first_number = int(input("Enter the first number: ", ))
second_number = int(input("Enters the second number: ", ))
while first_number != second_number:
    print("The umbers are not equal.")
    break

## Comparison 7
first_number = 23
second_number = 4567
first_number = int(input("Enter the first number: ", ))
second_number = int(input("Enters the second number: ", ))
while second_number > first_number:
    print("Second number is greater than first number.")
    break

## Comparison 8
first_number = 23
second_number = 4567
first_number = int(input("Enter the first number: ", ))
second_number = int(input("Enters the second number: ", ))
while second_number >= first_number:
    print("Second number is greater than or equal to first number.")
    break

## Comparison 9
first_number = 23
second_number = 4567
first_number = int(input("Enter the first number: ", ))
second_number = int(input("Enters the second number: ", ))
if first_number > 1000 and second_number > 1000:
    print("Both numbers are big!")
else:
    print("Both numbers are not big!")
    
## Comparison 10
big_numbers = {23, 4567}
big_number1 = int(input("Enter the first big_number: ", ))
big_number2 = int(input("Enters the second big_number: ", ))
if big_number1 > 1000 and big_number2 > 1000:
    print("big_numbers is a set of True.")
else:
    print("big_numbers is a set of False.")


### :heavy_plus_sign: Task 2 - Conversion month name to a number of days

#Your task is to write a Python program to convert month name to a number of days. 
#>Hint: Print list of months at the beginning.  

#User should be prompted to enter name of the month and the output should be the number of days in given month.

print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
month_name = input("Write the name of Month: ")
if month_name == "February":
    print("Number of days: 28/29 days.")
elif month_name in ("April", "June", "September", "November"):
    print("Number of days: 30 days.")
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
    print("Number of days: 31 days.")
else:
    print("Wrong month name.")
