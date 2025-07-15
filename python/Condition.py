# Write a Python program to check if a number is positive or negative.

# Check if a given number is even or odd using if-else.

# Take input marks and print if the student passed or failed (pass mark = 35).

# Write a program to find the greatest of two numbers.

# Check if a number is divisible by both 3 and 5.

# Write a program to check if a year is a leap year.

# Check if the given character is a vowel or consonant.

# Take a number from the user and check if it’s a single-digit, double-digit, or more.

# Write a program to categorize temperature (cold, normal, hot).

# Check if a person is eligible to vote (age ≥ 18).


# Take a number from the user and check if it’s a single-digit, double-digit, or more.
a = int(input("Enter the number: "))

# Convert to positive in case of negative number
num_digits = len(str(abs(a)))

if num_digits == 1:
    print("The entered number is a single-digit number!")
elif num_digits == 2:
    print("The entered number is a double-digit number!")
else:
    print("The entered number has more than two digits.")



# Check if the given character is a vowel or consonant.
chr=input("enter the letter :-")

chr=chr.lower()
if chr in['a','e','i','o','u']:
    print("is a vowel")
else:
    print("is a consonant")
# Take input marks and print if the student passed or failed (pass mark = 35).
marks=int(input("enter the marks:"))

if marks>=35:
    print("you pass!")
else:
    print("failed!")


# Write a Python program to check if a number is positive or negative.

x=int(input("enter the number:"))
if x>-0:
    print(" it is the positive number")
else:
    print("it si the negative number")



# Check if a given number is even or odd using if-else.

x=int(input("enter the number:"))
if x%2==0:
    print(" it is the even number")
else:
    print("it si the odd number")