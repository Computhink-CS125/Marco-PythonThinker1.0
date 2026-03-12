# Recap 1: Dice Roll Simulator
# Generate and print 3 random numbers between 1 and 6, followed
# by an output of 'True' if all 3 numbers are either even or odd.

# Example:
# 1st number: 6
# 2nd number: 4
# 3rd number: 6
# All numbers are even/odd: True

# 1. Import the 'random' library
# 2. Create 3 variables to hold a random number that is between
#    1 and 6, generated using 'random.randint()'
# 3. Using string concatenation, print the generated number for
#    each of the 3 numbers
# 4. Using the '%' and '==' operator, check if each number is
#    divisible by 2 (remainder = 0)
# 5. Using multiple '==' operators, a new variable 'all_even_odd'
#    should be assigned 'True' if all 3 numbers are either all
#    even or all odd numbers.
# 6. Print if "All numbers are even/odd" is 'True' or 'False'

# import random
# num1 = random.randint(1, 6)
# num2 = random.randint(1, 6)
# num3 = random.randint(1, 6)
# print("1st number:" + str(num1))
# print("2st number:" + str(num2))
# print("3st number:" + str(num3))
# even1 = num1 % 2 ==0
# even2 = num2 % 2 ==0
# even3 = num3 % 2 ==0
# all_even_odd = even1 == even2 == even3
# print("All numbers are even/odd " + str(all_even_odd))
# find is_num1_even , is_num2_even , is_num3_even


num_of_days = int(input("How many days have you borrowed a book?\n"))
if num_of_days > 25:
    print("Remember to return your book!")
