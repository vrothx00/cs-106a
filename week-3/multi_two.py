"""
Program: multiply two numbers
--------------------
This program asks the user for two
integers and prints the value of the first number
multiplied with the second
"""

def main():
    print("This program multiplies two numbers.")
    # your code here
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    multi = num1 * num2
    print(multi)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
