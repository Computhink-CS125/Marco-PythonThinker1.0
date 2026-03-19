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


# num_of_days = int(input("How many days have you borrowed a book?\n"))
# if num_of_days > 25:
#     print("Remember to return your book!")

# # Task 4: Apple Shop
# **Task 4a**:
# Draw out the flowchart (on a piece of paper) of a program for
# the user to buy apples and calculate the price.

# Each apple costs $1

# 1. Ask the user how many apples they want to buy
# 2. If the user wants to buy more than 10 apples:
#    print "You will get a 10% discount for buying that many
#    apples!"
# 4. Print the price of the purchase
# num_apples = int(input("How many apples do you want to buy?\n"))
# if num_apples > 10:
#     print("You will get a 10% discount for buying that many apples!")
#     price = num_apples * 0.9
# else:
#     price = num_apples * 1
# print(f"The price of your purchase is ${price:.2f}")

#  Task 5: Fruits Shop
# **Task 5a**:
# Draw out the flowchart (on a piece of paper) of a program for
# the fruit shop, "FruitiFresh". FruitiFresh sells 2 fruits,
# Apple & Orange with the following pricing scheme:

# Apple:
# 1 Apple = 60 cents
# If buy more than 5 apples, get 10% discount for all apples

# Orange:
# 1 Orange = 90 cents
# If buy more than 5 oranges, get 10% discount for all oranges

# You want to create a program that:
# 1. Asks the user for the number of apples and oranges they
#    want to buy.
# 2. Print total price of the fruits

input()