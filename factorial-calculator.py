# Tanner McDaniel
# COMP 141 Fall 2015
# Lab 1
# May 12, 2019

# This program determines the factorial of a number.  If the input is negative, it ends the
# program.  If it is positive, the factorial() function proceeds.

# Main function
def main():
    print("The factorial of 5 is 120.")
    print("The factorial of 12 is 479001600.")
    # Get user input
    fact = int(input("Whose factorial shall we calculate? "))
    # Print calculation
    print(factorial(fact))

# factorial() calculates the factorial of a positive integer
def factorial (n: int) -> int:
    # Check if input is negative
    if n < 0:
        print("User number is negative.")
    # Check if factorial is at the end
    elif n == 0:
        return 1
    # Calculate factorial
    else:
        return n * factorial(n - 1)

# Call main
main()
