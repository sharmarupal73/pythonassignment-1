 #1.program for two numbers as inputs and print their sum
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate the sum
sum = num1 + num2

# Print the result
print("The sum is:", sum)





# 2.program to check whether a given number is even or odd
num = int(input("Enter a number: "))

# Check if the number is even or odd
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")






#3.program to calculate factorial of a given number
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)


    num = int(input("Enter a number: "))
    result = factorial(num)
    print("The factorial of", num, "is", result)





 # 4.program that asks the user for their name and then prints a greeting message
    name = input("What is your name? ")

    # Print a greeting message
    print("Hello, " + name + "! It's nice to meet you.")







#5.program that takes a string input from the user and writes it to a text file
input_string = input("Enter a string to write to a file: ")

# Open a file for writing
with open("output.txt", "w") as f:
    # Write the user's input to the file
    f.write(input_string)

# Print a message to the console
print("The string has been written to output.txt")





#6.program that reads the content of a text file and prints it to the console
# Open a file for writing
with open("output.txt", "w") as f:
    # Write the user's input to the file
    f.write(input_string)

# Print a message to the console
print(contents)






#7. program that takes a string as input and returns its length
input_string = input("Enter a string: ")

# Calculate the length of the string
length = len(input_string)

# Print the length to the console
print("The length of the string is:", length)






#8.program that concatenates two strings and return the result
# Get the user's input
input_string = input("Enter a string: ")

# Calculate the length of the string
length = len(input_string)

# Print the length to the console
print("The length of the string is:", length)





#9.program that checks if a substring is present in a given string
def check_substring(string, substring):
    """Check if a substring is present in a given string."""
    if substring in string:
        return True
    else:
        return False

# Get the string and substring from the user
string = input("Enter a string: ")
substring = input("Enter a substring: ")

# Check if the substring is present in the string
result = check_substring(string, substring)

# Print the result to the console
if result:
    print(f"The substring '{substring}' is present in the string '{string}'.")
else:
    print(f"The substring '{substring}' is not present in the string '{string}'.")






   #10.program that converts a given string to uppercase
    def convert_to_uppercase(string):
        """Convert a given string to uppercase."""
        return string.upper()


    # Get the string from the user
    string = input("Enter a string: ")

    # Convert the string to uppercase
    uppercase_string = convert_to_uppercase(string)

    # Print the result to the console
    print(f"The uppercase string is: {uppercase_string}")





#11.program that generates the first n numbers in the fibonacci sequence
def fibonacci(n):
    """Generate the first n numbers in the Fibonacci sequence."""
    sequence = []
    a, b = 0, 1
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Get the number of terms from the user
n = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence
fib_seq = fibonacci(n)

# Print the sequence to the console
print("The first", n, "numbers in the Fibonacci sequence are:")
print(fib_seq)






#12.program that calculates the sum of digits of a given number
def sum_of_digits(number):
    """Calculate the sum of digits of a given number."""
    return sum(int(digit) for digit in str(number))

# Get the number from the user
number = int(input("Enter a number: "))

# Calculate the sum of digits
sum_of_digits = sum_of_digits(number)

# Print the result to the console
print("The sum of digits of", number, "is:", sum_of_digits)




#13.program that asks the user for their birth year and calculates their age
import datetime

def calculate_age(birth_year, birth_month, birth_day):
    """Calculate the age of a person based on their birth year, month, and day."""
    today = datetime.date.today()
    birth_date = datetime.date(birth_year, birth_month, birth_day)
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# Get the birth year, month, and day from the user
birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day (1-31): "))

# Calculate the age
age = calculate_age(birth_year, birth_month, birth_day)

# Print the result to the console
print("You are", age, "years old.")





#14.program that reads multiple lines of input from user
# Create an empty list to store the input lines
lines = []

# Read input lines from the user until they enter an empty line
while True:
    line = input("Enter a line (or press Enter to finish): ")
    if line == "":
        break
    lines.append(line)

# Print all the input lines
print("You entered:")
for line in lines:
    print(line)




#15. program that reads data from a CSV file and prints it to console
# import csv
# Open the CSV file
with open('example.csv', 'r') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)

    # Print the header row (if present)
    header = next(reader, None)
    if header:
        print(','.join(header))

    # Print each row of data
    for row in reader:
        print(','.join(row))




#16. program in python that counts the frequency of each character in a string
def char_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

# Test the function
s = "hello world"
print("Character frequencies:")
for char, freq in char_frequency(s).items():
    print(f"{char}: {freq}")





#17.program that converts a given string to title case
def to_title_case(s):
    words = s.split()
    for i, word in enumerate(words):
        words[i] = word.capitalize()
    return " ".join(words)

# Test the function
s = "hello world, this is a test."
print("Original string:")
print(s)
print("Title case:")
print(to_title_case(s))




#18.program that checks if two strings are anagrams of each other
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

# Test the function
s1 = "listen"
s2 = "silent"
print(f"Are '{s1}' and '{s2}' anagrams? {are_anagrams(s1, s2)}")

s1 = "hello"
s2 = "world"
print(f"Are '{s1}' and '{s2}' anagrams? {are_anagrams(s1, s2)}")




#19.program that removes all punctuation from a given string
import string

def remove_punctuation(s):
    translator = str.maketrans('', '', string.punctuation)
    return s.translate(translator)

# Test the function
s = "Hello, World! This is a test string."
print("Original string:")
print(s)
print("String without punctuation:")
print(remove_punctuation(s))



#20. program that takes a list of numbers and returns their sum
def sum_numbers(numbers):
    return sum(numbers)

# Test the function
numbers = [1, 2, 3, 4, 5]
print("Sum of numbers:", sum_numbers(numbers))

numbers = [10, 20, 30, 40, 50]
print("Sum of numbers:", sum_numbers(numbers))




#21.program that counts the occurrences of a specific element in a list
def count_occurrences(lst, elem):
    return lst.count(elem)

# Test the function
lst = [1, 2, 2, 3, 4, 2, 5, 2]
elem = 2
print("List:", lst)
print("Element:", elem)
print("Occurrences:", count_occurrences(lst, elem))

lst = ["apple", "banana", "apple", "orange", "apple", "banana"]
elem = "apple"
print("List:", lst)
print("Element:", elem)
print("Occurrences:", count_occurrences(lst, elem))





#22. program that returns the minimum and maximum values in a list of numbers
def find_min_max(lst):
    return min(lst), max(lst)

# Test the function
lst = [3, 1, 4, 1, 5, 9, 2, 6]
print("List:", lst)
min_val, max_val = find_min_max(lst)
print("Minimum value:", min_val)
print("Maximum value:", max_val)

lst = [-10, 0, 10, 20, 30]
print("List:", lst)
min_val, max_val = find_min_max(lst)
print("Minimum value:", min_val)
print("Maximum value:", max_val)




#23.program that converts temperature from celsius to fahrenhite and viceversa def celsius_to_fahrenheit(celsius):
   
   
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Test the functions
celsius = 30
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")

fahrenheit = 86
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit}°F is equal to {celsius}°C")





#24.program that acts as a simple calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def main():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)
        else:
            raise ValueError(f"Invalid operator: {operator}")

        print(f"Result: {result}")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()




#25. program that copies the contents of one text file to another
def copy_file(src_file, dest_file):
    try:
        with open(src_file, 'r') as src:
            with open(dest_file, 'w') as dest:
                dest.write(src.read())
        print(f"Copied contents of {src_file} to {dest_file}")
    except FileNotFoundError:
        print(f"Error: {src_file} not found")
    except IOError as e:
        print(f"Error: {e}")

# Example usage:
src_file = "source.txt"
dest_file = "destination.txt"
copy_file(src_file, dest_file)




#26.program that checks if a string starts with a given prefix or ends with a given suffix
def check_prefix_suffix(string, prefix, suffix):
    if string.startswith(prefix):
        print(f"'{string}' starts with '{prefix}'")
    else:
        print(f"'{string}' does not start with '{prefix}'")

    if string.endswith(suffix):
        print(f"'{string}' ends with '{suffix}'")
    else:
        print(f"'{string}' does not end with '{suffix}'")

# Example usage:
string = "hello world"
prefix = "hello"
suffix = "world"
check_prefix_suffix(string, prefix, suffix)




#27.program that converts a string into a list of its characters
def string_to_list(s):
    return list(s)

# Example usage:
string = "hello"
char_list = string_to_list(string)
print(char_list)